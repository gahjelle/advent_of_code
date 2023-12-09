defmodule AOC2023.Day09 do
  @moduledoc """
  Advent of Code 2023, day 9: Mirage Maintenance.
  """
  require AOC

  @doc """
  Parse input.
  """
  def parse(puzzle_input) do
    puzzle_input
    |> String.split("\n", trim: true)
    |> Enum.map(fn line -> String.split(line) |> Enum.map(&String.to_integer/1) end)
  end

  @doc """
  Solve part 1.
  """
  def part1(data) do
    data |> Enum.map(fn numbers -> numbers |> Enum.reverse() |> extrapolate() end) |> Enum.sum()
  end

  @doc """
  Solve part 2.
  """
  def part2(data) do
    data |> Enum.map(&extrapolate/1) |> Enum.sum()
  end

  @doc """
  Extrapolate sequence to find the previous element.

  Extrapolate to the left, since it's easier to work with the head of a list in
  Elixir.

  ## Example:

      iex> extrapolate([0, 2, 5, 9, 14])
      -1
  """
  def extrapolate(numbers), do: extrapolate(numbers, numbers |> hd())

  def extrapolate(numbers, prev_value) do
    if Enum.all?(numbers, &(&1 == 0)) do
      prev_value
    else
      diff =
        numbers
        |> Enum.chunk_every(2, 1, :discard)
        |> Enum.map(fn [second, first] -> second - first end)

      extrapolate(diff, prev_value + (diff |> hd()))
    end
  end

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
