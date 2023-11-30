defmodule AOC2020.Day05 do
  @moduledoc """
  Advent of Code 2020, day 5: Binary Boarding.
  """
  require AOC

  @doc """
  Parse input.
  """
  def parse(puzzle_input) do
    puzzle_input
    |> String.replace("F", "0")
    |> String.replace("B", "1")
    |> String.replace("L", "0")
    |> String.replace("R", "1")
    |> String.split("\n", trim: true)
    |> Enum.map(&String.to_integer(&1, 2))
    |> MapSet.new()
  end

  @doc """
  Solve part 1.
  """
  def part1(tickets), do: Enum.max(tickets)

  @doc """
  Solve part 2.
  """
  def part2(tickets) do
    seats = Enum.min(tickets)..Enum.max(tickets) |> MapSet.new()
    MapSet.difference(seats, tickets) |> MapSet.to_list() |> hd
  end

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
