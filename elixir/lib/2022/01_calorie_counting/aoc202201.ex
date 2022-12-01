defmodule AOC2022.Day01 do
  @moduledoc """
  Advent of Code 2022, day 1: Calorie Counting
  """
  require AOC

  @doc """
  Parse input.
  """
  def parse(puzzle_input), do: puzzle_input |> String.split("\n\n") |> Enum.map(&parse_elf/1)

  @doc """
  Parse input for one elf.

  ## Example:

      iex> parse_elf("2022\\n12\\n1")
      [2022, 12, 1]
  """
  def parse_elf(line), do: line |> String.split("\n") |> Enum.map(&String.to_integer/1)

  @doc """
  Solve part 1.
  """
  def part1(calories), do: calories |> Enum.map(&Enum.sum/1) |> Enum.max()

  @doc """
  Solve part 2.
  """
  def part2(calories),
    do: calories |> Enum.map(&Enum.sum/1) |> Enum.sort(:desc) |> Enum.take(3) |> Enum.sum()

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
