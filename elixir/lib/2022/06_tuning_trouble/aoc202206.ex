defmodule AOC2022.Day06 do
  @moduledoc """
  Advent of Code 2022, day 6: Tuning Trouble.
  """
  require AOC

  @doc """
  Parse input.
  """
  def parse(puzzle_input), do: puzzle_input |> String.to_charlist()

  @doc """
  Solve part 1.
  """
  def part1(data), do: data |> find_marker(4)

  @doc """
  Solve part 2.
  """
  def part2(data), do: data |> find_marker(14)

  @doc """
  Find the first marker of the given length.

  A marker of length N is a sequence of N characters that are all different.

  ## Examples:

      iex> find_marker('geirarne', 3)
      3
      iex> find_marker('abcdefghijklmnopqrstuvwxyz', 20)
      20
      iex> find_marker('aaaaaaaaaabccccccc', 3)
      12
  """
  def find_marker(sequence, length) do
    sequence
    |> Enum.chunk_every(length, 1, :discard)
    |> Enum.find_index(fn marker -> marker |> MapSet.new() |> MapSet.size() == length end)
    |> then(&(&1 + length))
  end

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
