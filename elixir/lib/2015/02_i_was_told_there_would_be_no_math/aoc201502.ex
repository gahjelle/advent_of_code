defmodule AOC2015.Day02 do
  @moduledoc """
  Advent of Code 2015, day 2: I Was Told There Would Be No Math
  """
  require AOC

  def parse(puzzle_input) do
    puzzle_input
    |> String.split("\n")
    |> Enum.map(&parse_line/1)
  end

  def parse_line(line) do
    line
    |> String.split("x")
    |> Enum.map(&String.to_integer/1)
    |> Present.from_list()
  end

  def part1(input) do
    input |> Enum.map(&(Present.surface(&1) + Present.smallest_area(&1))) |> Enum.sum()
  end

  def part2(input) do
    input |> Enum.map(&(Present.smallest_perimeter(&1) + Present.volume(&1))) |> Enum.sum()
  end

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end

defmodule Present do
  defstruct length: 0, width: 0, height: 0

  def from_list([length, width, height]) do
    struct(__MODULE__, %{:length => length, :width => width, :height => height})
  end

  def surface(present) do
    (present.length * present.width + present.length * present.height +
       present.width * present.height) * 2
  end

  def sides(present), do: present |> Map.from_struct() |> Map.values()
  def volume(present), do: present |> sides() |> Enum.product()
  def sum_of_sides(present), do: present |> sides() |> Enum.sum()
  def longest_side(present), do: present |> sides() |> Enum.max()
  def smallest_area(present), do: div(volume(present), longest_side(present))
  def smallest_perimeter(present), do: (sum_of_sides(present) - longest_side(present)) * 2
end
