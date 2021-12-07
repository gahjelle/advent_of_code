defmodule AOC2021.Day07 do
  @moduledoc """
  Advent of Code 2021, day 7: The Treachery of Whales
  """
  require AOC

  @doc """
  Parse input
  """
  def parse(puzzle_input) do
    puzzle_input |> String.split(",") |> Enum.map(&String.to_integer/1)
  end

  @doc """
  Solve part 1
  """
  def part1(input), do: input |> optimize_fuel(&linear_fuel/2)

  @doc """
  Solve part 2
  """
  def part2(input), do: input |> optimize_fuel(&triangular_fuel/2)

  @doc """
  Find best position in terms of fuel use to move to

  ## Example:

      iex> optimize_fuel([0, 1, 1, 2, 8], &linear_fuel/2)
      1 + 0 + 0 + 1 + 7
  """
  def optimize_fuel(crab_pos, fuel_func) do
    1..length(crab_pos)
    |> Enum.reduce_while(fuel_func.(crab_pos, 0), fn pos, best_fuel ->
      pos_fuel = fuel_func.(crab_pos, pos)
      if pos_fuel < best_fuel, do: {:cont, pos_fuel}, else: {:halt, best_fuel}
    end)
  end

  @doc """
  Calculate fuel needed when 1 step costs 1 fuel

  ## Example:

      iex> linear_fuel([0, 1, 1, 2, 8], 5)
      5 + 4 + 4 + 3 + 3
  """
  def linear_fuel(crab_pos, pos), do: crab_pos |> Enum.map(&abs(pos - &1)) |> Enum.sum()

  @doc """
  Calculate fuel needed when each step costs 1 additional fuel

  ## Example:

      iex> triangular_fuel([0, 1, 1, 2, 8], 3)
      (1 + 2 + 3) + (1 + 2) + (1 + 2) + (1) + (1 + 2 + 3 + 4 + 5)
  """
  def triangular_fuel(crab_pos, pos) do
    crab_pos |> Enum.map(&div(abs(pos - &1) * (abs(pos - &1) + 1), 2)) |> Enum.sum()
  end

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
