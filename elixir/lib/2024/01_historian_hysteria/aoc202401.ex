defmodule AOC2024.Day01 do
  @moduledoc """
  Advent of Code 2024, day 1: Historian Hysteria.
  """
  require AOC

  @doc """
  Parse input.
  """
  def parse(puzzle_input) do
    puzzle_input
    |> String.split("\n", trim: true)
    |> Enum.map(fn line ->
      line
      |> String.split()
      |> Enum.map(&String.to_integer/1)
      |> then(fn [left, right] -> {left, right} end)
    end)
    |> Enum.unzip()
  end

  @doc """
  Solve part 1.
  """
  def part1({left, right}) do
    Enum.zip(Enum.sort(left), Enum.sort(right))
    |> Enum.map(fn {first, second} -> abs(second - first) end)
    |> Enum.sum()
  end

  @doc """
  Solve part 2.
  """
  def part2({left, right}) do
    counts = Enum.frequencies(right)

    left
    |> Enum.map(fn number -> number * Map.get(counts, number, 0) end)
    |> Enum.sum()
  end

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
