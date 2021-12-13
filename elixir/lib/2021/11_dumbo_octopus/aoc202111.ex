defmodule AOC2021.Day11 do
  @moduledoc """
  Advent of Code 2021, day 11: Dumbo Octopus
  """
  require AOC

  @doc """
  Parse input
  """
  def parse(puzzle_input) do
    puzzle_input
    |> String.split("\n")
    |> Enum.with_index()
    |> Enum.map(fn {line, row} ->
      line
      |> String.split("", trim: true)
      |> Enum.map(&String.to_integer/1)
      |> Enum.with_index()
      |> Enum.map(fn {level, col} -> {{row, col}, level} end)
    end)
    |> Enum.concat()
    |> Enum.into(%{})
  end

  @doc """
  Solve part 1
  """
  def part1(input) do
    {_, num_flashes} =
      1..100
      |> Enum.reduce({input, 0}, fn _, {energies, done_flashes} ->
        {new_energies, new_flashes} = energies |> step()
        {new_energies, done_flashes + new_flashes}
      end)

    num_flashes
  end

  @doc """
  Solve part 2
  """
  def part2(input) do
    input |> synchronize()
  end

  @doc """
  Do one step of energy increase

  ## Examples:

      35   -->   57
      79         90

      iex> step(%{{0, 0} => 3, {0, 1} => 5, {1, 0} => 7, {1, 1} => 9})
      {%{{0, 0} => 5, {0, 1} => 7, {1, 0} => 9, {1, 1} => 0}, 1}

      11111         34543
      19991         40004
      19191   -->   50005
      19991         40004
      11111         34543

      iex> step(%{
      ...>     {0, 0} => 1, {0, 1} => 1, {0, 2} => 1, {0, 3} => 1, {0, 4} => 1,
      ...>     {1, 0} => 1, {1, 1} => 9, {1, 2} => 9, {1, 3} => 9, {1, 4} => 1,
      ...>     {2, 0} => 1, {2, 1} => 9, {2, 2} => 1, {2, 3} => 9, {2, 4} => 1,
      ...>     {3, 0} => 1, {3, 1} => 9, {3, 2} => 9, {3, 3} => 9, {3, 4} => 1,
      ...>     {4, 0} => 1, {4, 1} => 1, {4, 2} => 1, {4, 3} => 1, {4, 4} => 1})
      {%{{0, 0} => 3, {0, 1} => 4, {0, 2} => 5, {0, 3} => 4, {0, 4} => 3,
         {1, 0} => 4, {1, 1} => 0, {1, 2} => 0, {1, 3} => 0, {1, 4} => 4,
         {2, 0} => 5, {2, 1} => 0, {2, 2} => 0, {2, 3} => 0, {2, 4} => 5,
         {3, 0} => 4, {3, 1} => 0, {3, 2} => 0, {3, 3} => 0, {3, 4} => 4,
         {4, 0} => 3, {4, 1} => 4, {4, 2} => 5, {4, 3} => 4, {4, 4} => 3}, 9}
  """
  def step(energies), do: energies |> add_one(Map.keys(energies)) |> flash()

  @doc """
  Add 1 to the given positions, ignore invalid positions

  ## Example:

     (3) (5) ( )  -->   4 6
     (7)  9             8 9

     iex> add_one(%{{0, 0} => 3, {0, 1} => 5, {1, 0} => 7, {1, 1} => 9}, [{0, 0}, {0, 1}, {0, 2}, {1, 0}])
     %{{0, 0} => 4, {0, 1} => 6, {1, 0} => 8, {1, 1} => 9}
  """
  def add_one(energies, positions) do
    positions
    |> Enum.reduce(energies, fn pos, acc -> acc |> Map.replace(pos, Map.get(acc, pos, 0) + 1) end)
  end

  @doc """
  Perform flashes for the given energies

  ## Example:

      0 7    -->   2 9
      9 10         0 0

      iex> flash(%{{0, 0} => 0, {0, 1} => 7, {1, 0} => 9, {1, 1} => 10})
      {
        %{{0, 0} => 2, {0, 1} => 9, {1, 0} => 0, {1, 1} => 0},
        2
      }
  """
  def flash(energies), do: flash(energies, [])

  def flash(energies, already_flashed) do
    flash(
      energies,
      Map.keys(energies) |> Enum.filter(fn pos -> Map.get(energies, pos) > 9 end),
      already_flashed
    )
  end

  def flash(energies, [], already_flashed) do
    flashed_energies =
      Enum.reduce(already_flashed, energies, fn pos, acc ->
        Map.update!(acc, pos, fn _ -> 0 end)
      end)

    if flashed_energies |> Map.values() |> Enum.all?(&(&1 <= 9)) do
      {flashed_energies, already_flashed |> length()}
    else
      flash(
        flashed_energies,
        Map.keys(flashed_energies)
        |> Enum.filter(fn pos -> Map.get(flashed_energies, pos) > 9 end),
        already_flashed
      )
    end
  end

  def flash(energies, [next | to_flash], already_flashed) do
    flash(energies |> add_one(next |> neighbors()), to_flash, [next | already_flashed])
  end

  @doc """
  Find all possible neighbors of an octopus position, including invalid ones

  ## Example:

      iex> neighbors({0, 3})
      [{-1, 2}, {0, 2}, {1, 2}, {-1, 3}, {1, 3}, {-1, 4}, {0, 4}, {1, 4}]
  """
  def neighbors({x, y}) do
    [
      {x - 1, y - 1},
      {x, y - 1},
      {x + 1, y - 1},
      {x - 1, y},
      {x + 1, y},
      {x - 1, y + 1},
      {x, y + 1},
      {x + 1, y + 1}
    ]
  end

  @doc """
  Count steps until all octopuses flash synchronously

  ## Example:

      5 6   -->   6 7   -->   0 0
      7 8         8 9         0 0

      iex> synchronize(%{{0, 0} => 5, {0, 1} => 6, {1, 0} => 7, {1, 1} => 8})
      2
  """
  def synchronize(energies), do: synchronize(energies, 0)

  def synchronize(energies, steps) do
    if energies |> Map.values() |> Enum.all?(&(&1 == 0)),
      do: steps,
      else: synchronize(energies |> step() |> elem(0), steps + 1)
  end

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
