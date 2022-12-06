defmodule AOC2017.Day03 do
  @moduledoc """
  Advent of Code 2017, day 3: Spiral Memory
  """
  require AOC

  @doc """
  Parse input.
  """
  def parse(puzzle_input), do: puzzle_input |> String.to_integer()

  @doc """
  Solve part 1.
  """
  def part1(square), do: generate_coords() |> Enum.at(square - 1) |> manhattan()

  @doc """
  Solve part 2.
  """
  def part2(square),
    do: generate_sums() |> Enum.find(fn sum -> sum > square end)

  @doc """
  Generate consecutive spiral xy-coordinates.

  ## Example:

      17 16 15 14 13
      18  5  4  3 12
      19  6  1  2 11 ...
      20  7  8  9 10 27
      21 22 23 24 25 26

      iex> generate_coords() |> Enum.take(11)
      [{0, 0}, {1, 0}, {1, 1}, {0, 1}, {-1, 1}, {-1, 0}, {-1, -1}, {0, -1},
       {1, -1}, {2, -1}, {2, 0}]
  """
  def generate_coords() do
    Stream.resource(
      fn -> {{0, 0}, 1, :right, 1} end,
      fn {{x, y} = xy, spiral, direction, steps} ->
        case {direction, steps} do
          {:right, 1} -> {[xy], {{x + 1, y}, spiral + 1, :up, 2 * spiral - 1}}
          {:right, _} -> {[xy], {{x + 1, y}, spiral, :right, steps - 1}}
          {:up, 1} -> {[xy], {{x, y + 1}, spiral, :left, 2 * (spiral - 1)}}
          {:up, _} -> {[xy], {{x, y + 1}, spiral, :up, steps - 1}}
          {:left, 1} -> {[xy], {{x - 1, y}, spiral, :down, 2 * (spiral - 1)}}
          {:left, _} -> {[xy], {{x - 1, y}, spiral, :left, steps - 1}}
          {:down, 1} -> {[xy], {{x, y - 1}, spiral, :right, 2 * spiral - 1}}
          {:down, _} -> {[xy], {{x, y - 1}, spiral, :down, steps - 1}}
        end
      end,
      fn _ -> nil end
    )
  end

  @doc """
  Generate consecutive spiral xy-coordinates.

  ## Example:

      147 142 133 122  59
      304   5   4   2  57
      330  10   1   1  54  ...
      351  11  23  25  26 1968
      362 747 806 880 931  957

      iex> generate_sums() |> Enum.take(11)
      [1, 1, 2, 4, 5, 10, 11, 23, 25, 26, 54]
  """
  def generate_sums() do
    Stream.resource(
      fn -> {{0, 0}, %{{0, 0} => 1}, 1, :right, 1} end,
      fn {{x, y} = xy, sums, spiral, direction, steps} ->
        sum = xy |> neighbors() |> Enum.map(&Map.get(sums, &1, 0)) |> Enum.sum()
        new_sums = Map.put_new(sums, xy, sum)

        case {direction, steps} do
          {:right, 1} -> {[sum], {{x + 1, y}, new_sums, spiral + 1, :up, 2 * spiral - 1}}
          {:right, _} -> {[sum], {{x + 1, y}, new_sums, spiral, :right, steps - 1}}
          {:up, 1} -> {[sum], {{x, y + 1}, new_sums, spiral, :left, 2 * (spiral - 1)}}
          {:up, _} -> {[sum], {{x, y + 1}, new_sums, spiral, :up, steps - 1}}
          {:left, 1} -> {[sum], {{x - 1, y}, new_sums, spiral, :down, 2 * (spiral - 1)}}
          {:left, _} -> {[sum], {{x - 1, y}, new_sums, spiral, :left, steps - 1}}
          {:down, 1} -> {[sum], {{x, y - 1}, new_sums, spiral, :right, 2 * spiral - 1}}
          {:down, _} -> {[sum], {{x, y - 1}, new_sums, spiral, :down, steps - 1}}
        end
      end,
      fn _ -> nil end
    )
  end

  @doc """
  Manhattan distance to a point.

  ## Examples:

      iex> manhattan({3, 6})
      9
      iex> manhattan({-13, 33})
      46
  """
  def manhattan({x, y}), do: abs(x) + abs(y)

  @doc """
  List neighbors of a coordinate.

  ## Example:

      iex> neighbors({6, -3})
      [{5, -4}, {5, -3}, {5, -2}, {6, -4}, {6, -3}, {6, -2}, {7, -4}, {7, -3}, {7, -2}]
  """
  def neighbors({x, y}), do: for(dx <- -1..1, dy <- -1..1, do: {x + dx, y + dy})

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
