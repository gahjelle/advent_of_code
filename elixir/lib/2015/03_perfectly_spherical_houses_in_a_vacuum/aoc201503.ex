defmodule AOC2015.Day03 do
  @moduledoc """
  Advent of Code 2015, day 3: Perfectly Spherical Houses in a Vacuum
  """
  require AOC

  @steps %{"^" => {0, 1}, ">" => {1, 0}, "v" => {0, -1}, "<" => {-1, 0}}

  @doc """
  Parse input
  """
  def parse(puzzle_input) do
    puzzle_input |> String.split("", trim: true) |> Enum.map(fn c -> @steps[c] end)
  end

  @doc """
  Solve part 1
  """
  def part1(input) do
    input |> visit() |> Enum.count()
  end

  @doc """
  Solve part 2
  """
  def part2(input) do
    santa = input |> Enum.take_every(2) |> visit()
    robosanta = input |> tl |> Enum.take_every(2) |> visit()
    MapSet.union(santa, robosanta) |> Enum.count()
  end

  @doc """
  Visit houses according to instructions, return positions visited

  ## Example:

      iex> visit([{0, 1}, {1, 0}, {0, -1}, {1, 0}])
      MapSet.new([{0, 0}, {0, 1}, {1, 1}, {1, 0}, {2, 0}])
  """
  def visit(houses) do
    houses
    |> Enum.reduce({MapSet.new([{0, 0}]), 0, 0}, fn {dx, dy}, {pos, x, y} ->
      {MapSet.put(pos, {x + dx, y + dy}), x + dx, y + dy}
    end)
    |> elem(0)
  end

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
