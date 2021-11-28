defmodule AOC2020.Day01 do
  @moduledoc """
  Advent of Code 2020, day 1: Report Repair
  """
  require AOC

  @doc """
  Parse input
  """
  def parse(puzzle_input) do
    puzzle_input
    |> String.split("\n")
    |> Enum.map(&String.to_integer/1)
    |> MapSet.new()
  end

  @doc """
  Solve part 1
  """
  def part1(input) do
    input |> find_summands() |> Enum.product()
  end

  @doc """
  Solve part 2
  """
  def part2(input) do
    input
    |> Enum.find_value(fn first ->
      case find_summands(input, 2020 - first) do
        [0, _] -> nil
        [second, third] -> [first, second, third]
      end
    end)
    |> Enum.product()
  end

  @doc """
  Find the two numbers in the list that sum to target

  ## Examples:

      iex> find_summands([1721, 979, 299])
      [1721, 299]

      iex> find_summands([1721, 979, 299], 2021)
      [0, 2021]
  """
  def find_summands(numbers, target \\ 2020) do
    numbers
    |> Enum.find(0, fn first -> (target - first) in numbers end)
    |> then(fn first -> [first, target - first] end)
  end

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
