defmodule AOC2017.Day02 do
  @moduledoc """
  Advent of Code 2017, day 2: Corruption Checksum
  """
  require AOC

  @doc """
  Parse input
  """
  def parse(puzzle_input) do
    puzzle_input |> String.split("\n") |> Enum.map(&parse_row/1)
  end

  @doc """
  Parse one row in the spreadsheet

  ## Example:

      iex> parse_row("2017 12 2")
      [2017, 12, 2]
  """
  def parse_row(row), do: row |> String.split() |> Enum.map(&String.to_integer/1)

  @doc """
  Solve part 1
  """
  def part1(input) do
    input |> Enum.map(&find_min_max_difference/1) |> Enum.sum()
  end

  @doc """
  Find the difference between the smallest and largest number

  ## Example:

      iex> find_min_max_difference([5, 1, 9, 5])
      8
  """
  def find_min_max_difference(numbers) do
    {min, max} = numbers |> Enum.min_max()
    max - min
  end

  @doc """
  Solve part 2
  """
  def part2(input) do
    input |> Enum.map(&find_division/1) |> Enum.sum()
  end

  @doc """
  Find the two numbers that divide evenly and return their ratio

  ## Example:

      iex> find_division([5, 9, 2, 8])
      4
  """
  def find_division(numbers) do
    [first | rest] = numbers |> Enum.sort()
    find_division(first, rest)
  end

  def find_division(divisor, [next | numbers]) do
    dividend = [next | numbers] |> Enum.find(-1, fn dividend -> rem(dividend, divisor) == 0 end)
    if dividend == -1, do: find_division(next, numbers), else: div(dividend, divisor)
  end

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
