defmodule AOC2023.Day02 do
  @moduledoc """
  Advent of Code 2023, day 2: Cube Conundrum.
  """
  require AOC

  @doc """
  Parse input.
  """
  def parse(puzzle_input) do
    puzzle_input
    |> String.split("\n", trim: true)
    |> Enum.map(&find_max_cubes/1)
  end

  @doc """
  Find the maximum number of cubes in each color.

  Return a tuple in the order {red, green, blue}. We don't need to care about
  the difference between , and ; to find the maximum.

  ## Example:

      iex> find_max_cubes("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green")
      {6, 3, 2}
  """
  def find_max_cubes(line) do
    [_, cubes] = String.split(line, ":")

    cubes
    |> String.split(~r/[,;]/)
    |> Enum.map(fn cube ->
      [num, color] = String.split(cube)
      {color, String.to_integer(num)}
    end)
    |> Enum.reduce(%{}, fn {color, num}, acc ->
      Map.update(acc, color, num, &max(&1, num))
    end)
    |> then(fn %{"red" => red, "green" => green, "blue" => blue} -> {red, green, blue} end)
  end

  @doc """
  Solve part 1.
  """
  def part1(data) do
    data
    |> Enum.with_index(1)
    |> Enum.filter(fn {{red, green, blue}, _} -> red <= 12 && green <= 13 && blue <= 14 end)
    |> Enum.map(fn {_, game_id} -> game_id end)
    |> Enum.sum()
  end

  @doc """
  Solve part 2.
  """
  def part2(data) do
    data
    |> Enum.map(fn {red, green, blue} -> red * green * blue end)
    |> Enum.sum()
  end

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
