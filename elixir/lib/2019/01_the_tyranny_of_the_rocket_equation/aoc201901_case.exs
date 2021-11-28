defmodule AOC2019.Day01 do
  @moduledoc """
  Advent of Code 2019, day 1: The Tyranny of the Rocket Equation
  """
  require AOC

  def parse(puzzle_input) do
    puzzle_input
    |> String.split("\n")
    |> Enum.map(&String.to_integer/1)
  end

  def part1(input) do
    input |> Enum.map(&fuel/1) |> Enum.sum()
  end

  def part2(input) do
    input |> Enum.map(&all_fuel/1) |> Enum.sum()
  end

  defp fuel(mass) do
    div(mass, 3) - 2
  end

  defp all_fuel(mass) do
    case fuel(mass) do
      fuel when fuel <= 0 -> 0
      fuel -> fuel + all_fuel(fuel)
    end
  end

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
