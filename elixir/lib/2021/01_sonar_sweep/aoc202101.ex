defmodule AOC2021.Day01 do
  @moduledoc """
  Advent of Code 2021, day 1: Sonar Sweep
  """
  require AOC

  @doc """
  Parse input
  """
  def parse(puzzle_input) do
    puzzle_input |> String.split("\n") |> Enum.map(&String.to_integer/1)
  end

  @doc """
  Solve part 1
  """
  def part1(input) do
    input
    |> calculate_differences()
    |> Enum.count(fn diff -> diff > 0 end)
  end

  @doc """
  Solve part 2
  """
  def part2(input) do
    input
    |> sum_of_threes()
    |> calculate_differences()
    |> Enum.count(fn diff -> diff > 0 end)
  end

  @doc """
  Calculate the differences between consecutive elements

  ## Example:

      iex> calculate_differences([20, 21, 12, 1, 1])
      [1, -9, -11, 0]

      iex> calculate_differences(1..10 |> Enum.to_list()) |> length()
      9
  """
  def calculate_differences([initial | numbers]) do
    numbers
    |> Enum.reduce({[], initial}, fn num, {diffs, prev} -> {[num - prev | diffs], num} end)
    |> elem(0)
    |> Enum.reverse()
  end

  @doc """
  Calculate the rolling sum of each three consecutive elements

  ## Example:

      iex> sum_of_threes([20, 21, 12, 1, 1])
      [53, 34, 14]

      iex> sum_of_threes(1..10 |> Enum.to_list()) |> length()
      8
  """
  def sum_of_threes([prev, current | numbers]) do
    numbers
    |> Enum.reduce({[], prev, current}, fn next, {sums, prev, current} ->
      {[prev + current + next | sums], current, next}
    end)
    |> elem(0)
    |> Enum.reverse()
  end

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
