defmodule AOC2019.Day01 do
  @moduledoc """
  Advent of Code 2019, day 1: The Tyranny of the Rocket Equation
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
  def part1(input) do
    input |> Enum.map(&fuel/1) |> Enum.sum()
  end

  @doc """
  Solve part 2
  """
  def part2(input) do
    input |> Enum.map(&all_fuel/1) |> Enum.sum()
  end

  @doc """
  Calculate necessary fuel for the given mass

  ## Example:

      iex> fuel(1969)
      654
  """
  def fuel(mass) do
    div(mass, 3) - 2
  end

  @doc """
  Calculate necessary fuel for the given mass, accounting for the added weight of the fuel itself

  ## Example:

      iex> all_fuel(1969)
      966
  """
  def all_fuel(mass) do
    case fuel(mass) do
      fuel when fuel <= 0 -> 0
      fuel -> fuel + all_fuel(fuel)
    end
  end

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
