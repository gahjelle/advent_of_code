defmodule AOC2015.Day01 do
  @moduledoc """
  Advent of Code 2015, day 1: Not Quite Lisp
  """
  require AOC

  @steps %{"(" => 1, ")" => -1}

  def parse(puzzle_input) do
    puzzle_input
    |> String.split("", trim: true)
    |> Enum.map(fn c -> @steps[c] end)
  end

  def part1(input) do
    input |> Enum.sum()
  end

  def part2(input) do
    1 + (input |> Enum.scan(&(&1 + &2)) |> Enum.find_index(&(&1 < 0)))
  end

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
