defmodule AOC2015.Day03 do
  @moduledoc """
  Advent of Code 2015, day 3: Perfectly Spherical Houses in a Vacuum
  """
  require AOC

  @steps %{"^" => {0, 1}, ">" => {1, 0}, "v" => {0, -1}, "<" => {-1, 0}}

  def step({dx, dy}, {pos, {x, y}}), do: {MapSet.put(pos, {x + dx, y + dy}), {x + dx, y + dy}}
  def visit(houses), do: houses |> Enum.reduce({MapSet.new([{0, 0}]), {0, 0}}, &step/2) |> elem(0)

  def every_second([]), do: []
  def every_second([first]), do: [first]
  def every_second([first, _second | rest]), do: [first | every_second(rest)]

  def parse(puzzle_input) do
    puzzle_input |> String.split("", trim: true) |> Enum.map(fn c -> @steps[c] end)
  end

  def part1(input) do
    input |> visit() |> Enum.count()
  end

  def part2(input) do
    santa = input |> every_second() |> visit()
    robosanta = input |> tl |> every_second() |> visit()
    MapSet.union(santa, robosanta) |> Enum.count()
  end

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
