defmodule AOC2018.Day01 do
  @moduledoc """
   Advent of Code 2018, day 1: Chronal Calibration
  """
  require AOC

  @doc """
  Parse input
  """
  def parse(puzzle_input) do
    puzzle_input
    |> String.split("\n")
    |> Enum.map(&String.to_integer/1)
  end

  @doc """
  Solve part 1
  """
  def part1(input), do: input |> Enum.sum()

  @doc """
  Solve part 2
  """
  def part2(input), do: input |> Stream.cycle() |> first_repeat()

  @doc """
  Find first repeated number in an infinite stream of diffs

  ## Examples:

      iex> first_repeat([1, -1, 1, -1])
      0

      iex> first_repeat(Stream.cycle([3, 2, 1, -5]))
      6

      iex> first_repeat(Stream.cycle([7, 7, -2, -7, -4]))
      14
  """
  def first_repeat(diffs) do
    Enum.reduce_while(diffs, {0, MapSet.new()}, fn freq_change, {frequency, seen} ->
      case frequency in seen do
        true -> {:halt, frequency}
        false -> {:cont, {frequency + freq_change, MapSet.put(seen, frequency)}}
      end
    end)
  end

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
