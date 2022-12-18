defmodule AOC2022.Day17 do
  @moduledoc """
  Advent of Code 2022, day 17: Pyroclastic Flow.
  """
  require AOC

  @doc """
  Parse input.
  """
  def parse(puzzle_input) do
    puzzle_input
    |> String.split("", trim: true)
    |> Enum.map(fn
      ">" -> :right
      "<" -> :left
    end)
    |> create_infinite()
  end

  @doc """
  Solve part 1.
  """
  def part1(jets), do: find_tower_height(jets, 2022)

  @doc """
  Solve part 2.
  """
  def part2(jets), do: find_tower_height(jets, 1_000_000_000_000)

  @doc """
  Find the tower height after dropping a given number of rocks.

  ## Example:

      iex> jets = create_infinite([:left])  # Stack everything toward the left wall
      iex> find_tower_height(jets, 1)
      1
      iex> find_tower_height(jets, 2)
      4
      iex> find_tower_height(jets, 5)
      11
      iex> find_tower_height(jets, 5555)
      12221 = 11 * 1111
      iex> find_tower_height(jets, 5557)
      12225
  """
  def find_tower_height(jets, number_of_rocks) do
    floor = 0..6 |> Enum.into(%MapSet{}, fn x -> {x, 0} end)

    # Warm up, drop a few rocks to blur out the effect of the floor
    warm_up = min(200, number_of_rocks)

    {jets, tower, warm_up_height} =
      1..warm_up |> Enum.reduce({jets, floor, 0}, &simulate_rock_fall/2)

    if warm_up == number_of_rocks do
      warm_up_height
    else
      # Drop rocks until pattern repeats
      initial = {jets, tower, warm_up_height, 0, %{}}

      {jets, tower, height, period, _} =
        (warm_up + 1)..number_of_rocks
        |> Enum.reduce_while(initial, fn kind, {jets, tower, height, _, seen} ->
          {new_jets, new_tower, new_height} = simulate_rock_fall(kind, {jets, tower, height})
          position = {rem(kind, 5), peek_index(jets)}

          if Map.has_key?(seen, position),
            do: {:halt, {jets, tower, height, kind - seen[position], seen}},
            else: {:cont, {new_jets, new_tower, new_height, 1, Map.put(seen, position, kind)}}
        end)

      num_periods = div(number_of_rocks - warm_up, period)
      period_height = height - warm_up_height

      # Drop the left-over rocks at the top of the tower
      {_, _, height} =
        (warm_up + num_periods * period + 1)..number_of_rocks//1
        |> Enum.reduce({jets, tower, height}, &simulate_rock_fall/2)

      # Add in the non-dropped periodic chunks
      height + (num_periods - 1) * period_height
    end
  end

  @doc """
  Simulate one rock falling.

  ## Example:

      iex> simulate_rock_fall(5, {create_infinite([:right]), MapSet.new([{6, 0}]), 0})
      {{[:right], 0, 1}, MapSet.new([{5, 1}, {5, 2}, {6, 0}, {6, 1}, {6, 2}]), 2}
  """
  def simulate_rock_fall(kind, {jets, tower, height}) do
    {jets, rock} =
      Stream.cycle([nil])
      |> Enum.reduce_while({jets, start_rock(kind, height + 4)}, fn _, {jets, rock} ->
        {jet, jets} = get_next(jets)
        blown_rock = rock |> blow_rock(jet, tower)
        dropped_rock = blown_rock |> drop_rock()

        if not_touch(tower, dropped_rock),
          do: {:cont, {jets, dropped_rock}},
          else: {:halt, {jets, blown_rock}}
      end)

    {jets, add_rock(tower, rock), tower_height(height, rock)}
  end

  @doc """
  Check if a rock overlaps any part of the tower.

  ## Examples:

      iex> tower = MapSet.new([{0, 0}, {1, 1}, {2, 0}])
      iex> not_touch(tower, [{2, 1}, {2, 2}, {3, 1}, {3, 2}])
      true
      iex> not_touch(tower, [{1, 1}, {1, 2}, {2, 1}, {2, 2}])
      false
  """
  def not_touch(tower, rock),
    do: rock |> Enum.all?(fn stone -> not MapSet.member?(tower, stone) end)

  @doc """
  Add a rock to the tower.

  ## Example:

      iex> add_rock(MapSet.new([{0, 0}, {0, 2}]), [{0, 1}, {0, 2}, {1 , 1}, {1, 2}])
      MapSet.new([{0, 0}, {0, 2}, {0, 1}, {0, 2}, {1 , 1}, {1, 2}])
  """
  def add_rock(tower, rock), do: MapSet.union(tower, Enum.into(rock, %MapSet{}))

  @doc """
  Update the tower height when placing a new rock.

  ## Examples:

      iex> tower_height(1, MapSet.new([{4, 1}, {4, 2}, {5, 1}, {5, 2}]))
      2
      iex> tower_height(4, MapSet.new([{4, 1}, {4, 2}, {5, 1}, {5, 2}]))
      4
  """
  def tower_height(height, rock),
    do: max(height, rock |> Enum.map(fn {_, y} -> y end) |> Enum.max())

  @doc """
  Wrap an enumerable to simulate an infinite stream of cycled elements.

  We could use Stream.cycle() for this, but streams are best for one-pass
  operations. Here, we want to continously take 1 element.

  ## Example:

      iex> create_infinite(1..3)
      {1..3, 0, 3}
  """
  def create_infinite(stream), do: {stream, 0, stream |> Enum.to_list() |> length}

  @doc """
  Get next element in an infinite stream.

  ## Example:

      iex> stream = create_infinite([4, 2])
      iex> {next, stream} = get_next(stream)
      iex> next
      4
      iex> {next, stream} = get_next(stream)
      iex> next
      2
      iex> {next, _} = get_next(stream)
      iex> next
      4
  """
  def get_next({stream, idx, len}), do: {Enum.at(stream, idx), {stream, rem(idx + 1, len), len}}

  @doc """
  Get number of elements in one cycle of the infinite stream.

  ## Example:

      iex> stream = create_infinite([4, 1, 8, 0, 6])
      iex> num_elements(stream)
      5
  """
  def num_elements({_, _, len}), do: len

  @doc """
  Peek at the index of the next element.

  ## Example:

      iex> stream = create_infinite([4, 1, 8, 0, 6])
      iex> {_, stream} = get_next(stream)
      iex> {_, stream} = get_next(stream)
      iex> peek_index(stream)
      2
      iex> {_, stream} = get_next(stream)
      iex> {_, stream} = get_next(stream)
      iex> {_, stream} = get_next(stream)
      iex> {_, stream} = get_next(stream)
      iex> peek_index(stream)
      1
  """
  def peek_index({_, idx, _}), do: idx

  @doc """
  Coordinates to one new rock as it starts falling.

  Each rock appears so that its left edge is two units away from the left wall
  and its bottom edge is three units above the highest rock in the room (or the
  floor, if there isn't one).

  The rocks cycle through the following five patterns.

                        #
          .#.    ..#    #
          ###    ..#    #    ##
  ####    .#.    ###    #    ##

  ## Examples:

      iex> start_rock(1, 0)
      [{2, 0}, {3, 0}, {4, 0}, {5, 0}]
      iex> start_rock(4, 3)
      [{2, 3}, {2, 4}, {2, 5}, {2, 6}]
      iex> start_rock(5, 9)
      [{2, 9}, {2, 10}, {3, 9}, {3, 10}]
      iex> start_rock(2, 7) === start_rock(132, 7)
      true
      iex> start_rock(2, 7) === start_rock(123, 7)
      false
      iex> start_rock(2, 7) === start_rock(432, 8)
      false
  """
  def start_rock(1, y), do: [{2, y}, {3, y}, {4, y}, {5, y}]
  def start_rock(2, y), do: [{2, y + 1}, {3, y}, {3, y + 1}, {3, y + 2}, {4, y + 1}]
  def start_rock(3, y), do: [{2, y}, {3, y}, {4, y}, {4, y + 1}, {4, y + 2}]
  def start_rock(4, y), do: [{2, y}, {2, y + 1}, {2, y + 2}, {2, y + 3}]
  def start_rock(5, y), do: [{2, y}, {2, y + 1}, {3, y}, {3, y + 1}]
  def start_rock(number, y), do: start_rock(rem(number - 1, 5) + 1, y)

  @doc """
  Blow the rock one unit to the left or right.

  The tower walls are to the left of 0 and to the right of 6, with the tower being 7 unit wide.

  ## Examples:

      iex> blow_rock([{2, 0}, {2, 1}, {3, 0}, {3, 1}], :left, %MapSet{})
      [{1, 0}, {1, 1}, {2, 0}, {2, 1}]
      iex> blow_rock([{3, 2}, {4, 2}, {5, 2}, {6, 2}], :right, %MapSet{})
      [{3, 2}, {4, 2}, {5, 2}, {6, 2}]
  """
  def blow_rock(rock, :right, tower) do
    if Enum.any?(rock, fn {x, _} -> x >= 6 end),
      do: rock,
      else: Enum.map(rock, fn {x, y} -> {x + 1, y} end) |> avoid_collision(tower, rock)
  end

  def blow_rock(rock, :left, tower) do
    if Enum.any?(rock, fn {x, _} -> x <= 0 end),
      do: rock,
      else: Enum.map(rock, fn {x, y} -> {x - 1, y} end) |> avoid_collision(tower, rock)
  end

  defp avoid_collision(rock, tower, original_rock),
    do: if(MapSet.disjoint?(tower, rock |> Enum.into(%MapSet{})), do: rock, else: original_rock)

  @doc """
  Drop the rock one unit down.

  ## Example:

      iex> drop_rock([{4, 3}, {4, 4}, {5, 3}, {5, 4}])
      [{4, 2}, {4, 3}, {5, 2}, {5, 3}]
  """
  def drop_rock(rock), do: Enum.map(rock, fn {x, y} -> {x, y - 1} end)

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
