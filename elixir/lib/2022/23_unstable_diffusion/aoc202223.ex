defmodule AOC2022.Day23 do
  @moduledoc """
  Advent of Code 2022, day 23: Unstable Diffusion.
  """
  require AOC

  @directions [:north, :south, :west, :east, :north, :south, :west]

  @doc """
  Parse input.
  """
  def parse(puzzle_input) do
    puzzle_input
    |> String.split("\n", trim: true)
    |> Enum.with_index()
    |> Enum.map(fn {line, row} ->
      String.to_charlist(line)
      |> Enum.with_index()
      |> Enum.map(fn {char, col} -> {{row, col}, char} end)
    end)
    |> Enum.flat_map(& &1)
    |> Enum.filter(fn {_, char} -> char == ?# end)
    |> Enum.into(%MapSet{}, fn {coord, _} -> coord end)
  end

  @doc """
  Solve part 1.
  """
  def part1(elves) do
    positions = 1..10 |> Enum.reduce(elves, &move_elves/2)
    {min_row, max_row} = positions |> Enum.map(&elem(&1, 0)) |> Enum.min_max()
    {min_col, max_col} = positions |> Enum.map(&elem(&1, 1)) |> Enum.min_max()
    (max_row - min_row + 1) * (max_col - min_col + 1) - MapSet.size(elves)
  end

  @doc """
  Solve part 2.
  """
  def part2(elves) do
    1..9_999
    |> Enum.reduce_while(elves, fn round, elves ->
      case move_elves(round, elves) do
        ^elves -> {:halt, round}
        elves -> {:cont, elves}
      end
    end)
  end

  @doc """
  Move all elves one step.

  ## Example:

      iex> elves = MapSet.new([{1, 2}, {1, 3}, {2, 2}, {4, 2}, {4, 3}])
      iex> move_elves(1, elves)
      MapSet.new([{0, 2}, {0, 3}, {2, 2}, {4, 2}, {3, 3}])
  """
  def move_elves(round, elves) do
    directions = @directions |> Enum.drop(rem(round - 1, 4)) |> Enum.take(4)
    proposed = elves |> Enum.into(%{}, &{&1, propose_move(&1, elves, directions)})

    valid =
      proposed
      |> Map.values()
      |> Enum.frequencies()
      |> Map.reject(fn {_, count} -> count >= 2 end)
      |> Map.keys()
      |> Enum.into(%MapSet{})

    elves
    |> Enum.into(%MapSet{}, fn elf ->
      if MapSet.member?(valid, proposed[elf]), do: proposed[elf], else: elf
    end)
  end

  @doc """
  Propose where one elf should move.

  ## Example:

      iex> directions = [:north, :south, :west, :east]
      iex> propose_move({2, 2}, MapSet.new([{1, 2}, {1, 3}, {2, 2}]), directions)
      {3, 2}
  """
  def propose_move(elf, elves, directions) do
    neighbors = find_neighbors(elf, elves)

    if MapSet.size(neighbors) == 0,
      do: elf,
      else: directions |> Enum.find(&check_direction(&1, neighbors)) |> then(&move_elf(elf, &1))
  end

  @doc """
  Find the neighbors of one elf.

  ## Example:

      iex> find_neighbors({2, 3}, MapSet.new([{1, 2}, {1, 3}, {2, 2}]))
      MapSet.new([:north, :northwest, :west])
  """
  def find_neighbors({row, col}, elves) do
    [
      northwest: {row - 1, col - 1},
      north: {row - 1, col},
      northeast: {row - 1, col + 1},
      west: {row, col - 1},
      east: {row, col + 1},
      southwest: {row + 1, col - 1},
      south: {row + 1, col},
      southeast: {row + 1, col + 1}
    ]
    |> Enum.filter(fn {_, pos} -> MapSet.member?(elves, pos) end)
    |> Enum.into(%MapSet{}, fn {direction, _} -> direction end)
  end

  @doc """
  Check if elf can move in the given direction.

  ## Examples:

      iex> check_direction(:south, MapSet.new([:north, :northwest, :west]))
      true
      iex> check_direction(:south, MapSet.new([:southeast, :north]))
      false
  """
  def check_direction(:north, neighbors),
    do: neighbors |> MapSet.disjoint?(MapSet.new([:northwest, :north, :northeast]))

  def check_direction(:south, neighbors),
    do: neighbors |> MapSet.disjoint?(MapSet.new([:southwest, :south, :southeast]))

  def check_direction(:west, neighbors),
    do: neighbors |> MapSet.disjoint?(MapSet.new([:northwest, :west, :southwest]))

  def check_direction(:east, neighbors),
    do: neighbors |> MapSet.disjoint?(MapSet.new([:northeast, :east, :southeast]))

  @doc """
  Move one elf.

  ## Examples:

      iex> move_elf({4, 5}, :north)
      {3, 5}

      iex> move_elf({1, 1}, :east)
      {1, 2}

      iex> move_elf({-1, 3}, nil)
      {-1, 3}
  """
  def move_elf({row, col}, :north), do: {row - 1, col}
  def move_elf({row, col}, :south), do: {row + 1, col}
  def move_elf({row, col}, :west), do: {row, col - 1}
  def move_elf({row, col}, :east), do: {row, col + 1}
  def move_elf(elf, nil), do: elf

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
