defmodule AOC2022.Day15 do
  @moduledoc """
  Advent of Code 2022, day 15: Beacon Exclusion Zone.
  """
  require AOC

  @doc """
  Parse input.
  """
  def parse(puzzle_input),
    do: puzzle_input |> String.split("\n", trim: true) |> Enum.map(&parse_line/1)

  @doc """
  Parse one line of input.

  ## Example:

      iex> parse_line("Sensor at x=2, y=18: closest beacon is at x=-2, y=15")
      {{2, 18}, {-2, 15}}
  """
  def parse_line(line) do
    %{"sx" => sx, "sy" => sy, "bx" => bx, "by" => by} =
      Regex.named_captures(
        ~r/Sensor at x=(?<sx>-?\d+), y=(?<sy>-?\d+): closest beacon is at x=(?<bx>-?\d+), y=(?<by>-?\d+)/,
        line
      )
      |> Enum.into(%{}, fn {key, pos} -> {key, String.to_integer(pos)} end)

    {{sx, sy}, {bx, by}}
  end

  @doc """
  Solve part 1.
  """
  def part1(sensors, row \\ 2_000_000) do
    coverage = sensors |> row_coverage(row) |> hd |> then(&Range.size(&1))

    beacons =
      sensors
      |> Enum.map(&elem(&1, 1))
      |> Enum.filter(&(elem(&1, 1) == row))
      |> Enum.into(%MapSet{}, &elem(&1, 0))
      |> MapSet.size()

    coverage - beacons
  end

  @doc """
  Solve part 2.
  """
  def part2(sensors, space \\ 4_000_000) do
    sensors |> find_hole(space) |> tuning_frequency()
  end

  @doc """
  Find sensor coverage for a given row.

  ## Example:

      6  ......211111111B..
      7  .....222111111111.
      8  ....2222211S111111
      9  ...222S2221111111.
      10 ....222221111111..
      11 .....2221111111...
      12 ......B..11111....

      iex> row_coverage([{{11, 8}, {15, 6}}, {{6, 9}, {6, 12}}], 12)
      [6..6, 9..13]
  """
  def row_coverage(sensors, row) do
    sensors
    |> Enum.map(fn {{sx, sy} = sensor, beacon} ->
      {sx, manhattan(sensor, beacon) - abs(row - sy)}
    end)
    |> Enum.reject(&(elem(&1, 1) < 0))
    |> Enum.map(fn {x, coverage} -> (x - coverage)..(x + coverage)//1 end)
    |> union()
  end

  @doc """
  Find a hole in the coverage.

  ## Example:

      TODO: Create a proper example
      5  ...........1......
      6  ......2...11B.....
      7  .....222.11111....
      8  ....2222211S111...
      9  ...222S2221111....
      10 ....22222.111.....
      11 .....222...1......
      12 ......B...........

      iex> find_hole([{{11, 8}, {12, 6}}, {{6, 9}, {6, 12}}], 20)
      {7, 6}
  """
  def find_hole(sensors, space) do
    distances = Enum.map(sensors, fn {sensor, beacon} -> {sensor, manhattan(sensor, beacon)} end)

    0..space
    |> Enum.find_value(fn row ->
      coverage =
        distances
        |> Enum.reject(fn {{_, sy}, distance} -> abs(row - sy) > distance end)
        |> Enum.map(fn {{sx, sy}, distance} ->
          max(0, sx - (distance - abs(row - sy)))..min(space, sx + (distance - abs(row - sy)))
        end)
        |> union()

      if length(coverage) > 1, do: {coverage |> hd |> then(&(&1.last + 1)), row}
    end)
  end

  # Slower because distances are calculated repeatedly
  # def find_hole(sensors, space) do
  #   0..space
  #   |> Enum.find_value(fn row ->
  #     coverage = row_coverage(sensors, row)
  #     if length(coverage) > 1, do: {coverage |> hd |> then(&(&1.last + 1)), row}
  #   end)
  # end

  @doc """
  Union of ranges.

  ## Examples:

      iex> union(2..4, 4..7)
      [2..7]
      iex> union(2..4, 5..7)
      [2..7]
      iex> union(-1..5, 8..12)
      [-1..5, 8..12]
      iex> union([-1..5, 8..12], 3..9)
      [-1..12]
      iex> union([-1..5, 8..12], 14..19)
      [-1..5, 8..12, 14..19]
      iex> union([])
      []
      iex> union([1..3])
      [1..3]
      iex> union([2..2, 9..9, 13..13, 14..14, 2..14, 2..2, -2..2, 16..24, 17..17])
      [-2..14, 16..24]
  """
  def union([]), do: []
  def union([range | ranges]), do: union(ranges, range)
  def union(one, two), do: _union(one, two) |> Enum.reverse()

  defp _union(ranges, range) when is_list(ranges) do
    [range | ranges]
    |> Enum.sort(fn one, two -> one.first <= two.first end)
    |> Enum.reduce([], fn
      range, [] -> [range]
      two, [one | ranges] -> _union(one, two) ++ ranges
    end)
  end

  defp _union(one, two) do
    if one.last + 1 < two.first or two.last + 1 < one.first,
      do: [two, one],
      else: [min(one.first, two.first)..max(one.last, two.last)]
  end

  @doc """
  Calculate the Manhattan distance between two points.

  ## Examples:

      iex> manhattan({3, 7}, {1, 11})
      6 = 2 + 4
      iex> manhattan({-2, 123}, {456, -12})
      593 = 458 + 135
  """
  def manhattan({x1, y1}, {x2, y2}), do: abs(x2 - x1) + abs(y2 - y1)

  @doc """
  Calculate tuning frequency.

  The tuning frequency can be found by multiplying the x coordinate by 4000000
  and then adding the y coordinate.

  ## Example:

      iex> tuning_frequency({14, 11})
      56_000_011
  """
  def tuning_frequency({x, y}), do: x * 4_000_000 + y

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
