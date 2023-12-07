defmodule AOC2023.Day06 do
  @moduledoc """
  Advent of Code 2023, day 6: Wait For It.
  """
  require AOC

  @doc """
  Parse input.
  """
  def parse(puzzle_input) do
    part1 =
      puzzle_input
      |> String.split("\n", trim: true)
      |> Enum.map(fn line ->
        line |> String.split() |> Enum.drop(1) |> Enum.map(&String.to_integer/1)
      end)
      |> Enum.zip()

    part2 =
      puzzle_input
      |> String.split("\n", trim: true)
      |> Enum.map(fn line ->
        line
        |> String.split(":")
        |> Enum.drop(1)
        |> hd
        |> String.replace(" ", "")
        |> String.to_integer()
      end)
      |> List.to_tuple()

    {part1, part2}
  end

  @doc """
  Solve part 1.
  """
  def part1({data, _}), do: data |> Enum.map(&find_num_records/1) |> Enum.product()

  @doc """
  Solve part 2.
  """
  def part2({_, data}) do
    data |> find_num_records()
  end

  @doc """
  Find the number of ways to beat the given record.

  Use that distance is given by d(t) = t * (T - t) where T = time. We use binary
  search to find the smallest integer t such that d(t) > distance.

  The number of records is found by the symmetry of d(t).

  ## Example:

      iex> find_num_records({8, 12})
      3
  """
  def find_num_records({time, distance}),
    do: find_num_records({time, distance}, 0, Integer.floor_div(time, 2))

  def find_num_records({time, _distance}, low, t) when low == t - 1 do
    time + 1 - 2 * t
  end

  def find_num_records({time, distance}, low, high) do
    mid = Integer.floor_div(low + high, 2)

    if mid * (time - mid) > distance,
      do: find_num_records({time, distance}, low, mid),
      else: find_num_records({time, distance}, mid, high)
  end

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
