defmodule AOC2016.Day03 do
  @moduledoc """
  Advent of Code 2016, day 3: Squares With Three Sides
  """
  require AOC

  @doc """
  Parse input
  """
  def parse(puzzle_input), do: puzzle_input |> String.split("\n") |> Enum.map(&parse_row/1)

  @doc """
  Parse one row of integers

  ## Examples:

      iex> parse_row("1 14 311 ")
      [1, 14, 311]
  """
  def parse_row(row), do: row |> String.split() |> Enum.map(&String.to_integer/1)

  @doc """
  Solve part 1
  """
  def part1(input), do: input |> Enum.count(&is_triangle?/1)

  @doc """
  Solve part 2
  """
  def part2(input), do: input |> transpose() |> Enum.count(&is_triangle?/1)

  @doc """
  Check if the sides can represent a triangle

  Let a, b, c represent the sides of the triangle, such that a <= b <= c. Then
  we want to check that a + b > c, or equivalently, that a + b + c > 2c.

  ## Examples:

      iex> is_triangle?([3, 4, 5])
      true

      iex> is_triangle?([5, 10, 25])
      false

      iex> is_triangle?([25, 10, 5])
      false

      iex> is_triangle?([1, 2, 3])
      false
  """
  def is_triangle?(sides), do: Enum.sum(sides) > 2 * Enum.max(sides)

  @doc """
  Transpose 3x3 blocks in the list of data

  ## Examples:

      iex> transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
      [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
  """
  def transpose(data) do
    data
    |> Enum.chunk_every(3)
    |> Enum.flat_map(fn [[a1, a2, a3], [b1, b2, b3], [c1, c2, c3]] ->
      [[a1, b1, c1], [a2, b2, c2], [a3, b3, c3]]
    end)
  end

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
