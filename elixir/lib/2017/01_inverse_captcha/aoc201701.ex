defmodule AOC2017.Day01 do
  @moduledoc """
  Advent of Code 2017, day 1: Inverse Captcha
  """
  require AOC
  require Integer

  @doc """
  Parse input
  """
  def parse(puzzle_input) do
    puzzle_input
    |> String.to_integer()
    |> Integer.digits()
  end

  @doc """
  Solve part 1
  """
  def part1(input) do
    input
    |> prepend_last()
    |> Enum.reduce({nil, 0}, &compare_consecutive/2)
    |> elem(1)
  end

  @doc """
  Solve part 2
  """
  def part2(input) do
    half_length = input |> length() |> div(2) |> trunc()

    input
    |> Enum.chunk_every(half_length)
    |> Enum.zip()
    |> Enum.filter(fn {first, second} -> first == second end)
    |> Enum.map(fn {first, second} -> first + second end)
    |> Enum.sum()
  end

  @doc """
  Add last digit in front of list

  ## Example:

      iex> prepend_last([1, 2, 3])
      [3, 1, 2, 3]
  """
  def prepend_last(digits), do: [digits |> Enum.reverse() |> hd | digits]

  @doc """
  Add number to running total if it's equal to the previous number

  ## Examples:

      iex> compare_consecutive(3, {3, 42})
      {3, 45}

      iex> compare_consecutive(3, {4, 42})
      {3, 42}
  """
  def compare_consecutive(current, {current, total}), do: {current, total + current}
  def compare_consecutive(current, {_previous, total}), do: {current, total}

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
