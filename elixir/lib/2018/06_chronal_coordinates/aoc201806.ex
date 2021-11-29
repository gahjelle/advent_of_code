defmodule AOC2018.Day06 do
  @moduledoc """
  Advent of Code 2018, day 6: Chronal Coordinates
  """
  require AOC

  @doc """
  Parse input
  """
  def parse(puzzle_input), do: puzzle_input |> String.split("\n") |> Enum.map(&parse_coordinate/1)

  @doc """
  Parse one coordinate

  ## Example

      iex> parse_coordinate("7, 11")
      {7, 11}
  """
  def parse_coordinate(coordinate),
    do: coordinate |> String.split(", ") |> Enum.map(&String.to_integer/1) |> List.to_tuple()

  @doc """
  Solve part 1
  """
  def part1(input),
    do: input |> finite_closest_grid() |> count_area() |> Map.values() |> Enum.max()

  @doc """
  Find the ranges that contain all the coordinates

  ## Example:

      iex> ranges([{2, 4}, {5, 9}, {7, 3}])
      {2..7, 3..9}
  """
  def ranges(coordinates) do
    {{min_x, _}, {max_x, _}} = coordinates |> Enum.min_max_by(&elem(&1, 0))
    {{_, min_y}, {_, max_y}} = coordinates |> Enum.min_max_by(&elem(&1, 1))
    {min_x..max_x, min_y..max_y}
  end

  @doc """
  Calculate the Manhattan (L1) distance between two points

  ## Example:

      iex> distance({5, 1}, {2, 7})
      9
  """
  def distance({x1, y1}, {x2, y2}), do: abs(x2 - x1) + abs(y2 - y1)

  @doc """
  Calculate the closest coordinate for one point

  ## Examples:

      A..       Aa.
      ...  -->  a.b
      ..B       .bB

      iex> closest_point([{1, 1}, {3, 3}], {1, 2})
      {1, 1}

      iex> closest_point([{1, 1}, {3, 3}], {1, 3})
      nil
  """
  def closest_point(coordinates, point) do
    coordinates
    |> Enum.map(fn coordinate -> {distance(point, coordinate), coordinate} end)
    |> Enum.sort()
    |> case do
      [{distance, _}, {distance, _} | _] -> nil
      [{_, coordinate} | _] -> coordinate
    end
  end

  @doc """
  Calculate which coordinate is closest to each point in the grid

  ## Example:

      A....       Aaa.b
      .....  -->  aa.bb
      ....B       a.bbB

      iex> closest_grid([{1, 1}, {5, 3}], 1..5, 1..3)
      %{{1, 1} => {1, 1}, {2, 1} => {1, 1}, {3, 1} => {1, 1}, {4, 1} =>    nil, {5, 1} => {5, 3},
        {1, 2} => {1, 1}, {2, 2} => {1, 1}, {3, 2} =>    nil, {4, 2} => {5, 3}, {5, 2} => {5, 3},
        {1, 3} => {1, 1}, {2, 3} =>    nil, {3, 3} => {5, 3}, {4, 3} => {5, 3}, {5, 3} => {5, 3},
      }
  """
  def closest_grid(coordinates, x_range, y_range) do
    x_range
    |> Task.async_stream(fn x ->
      for y <- y_range, do: {{x, y}, closest_point(coordinates, {x, y})}, into: %{}
    end)
    |> Stream.flat_map(fn {:ok, points} -> points end)
    |> Enum.into(%{})
  end

  @doc """
  Filter out coordinates that are on the border, as they give infinite area

  ## Example:

      A...       A...
      .B..  -->  .Bb.
      ....       .b.c
      ...C       ..cC

      iex> finite_closest_grid([{1, 1}, {2, 2}, {4, 4}])
      %{{2, 2} => {2, 2}, {3, 2} => {2, 2}, {2, 3} => {2, 2}}
  """
  def finite_closest_grid(coordinates) do
    {x_range, y_range} = ranges(coordinates)

    grid =
      coordinates
      |> closest_grid(x_range, y_range)

    infinite_top_bottom =
      for x <- x_range,
          y <- [y_range.first, y_range.last],
          do: Map.get(grid, {x, y}, nil)

    infinite_left_right =
      for x <- [x_range.first, x_range.last],
          y <- y_range,
          do: Map.get(grid, {x, y}, nil)

    infinites = MapSet.new(infinite_top_bottom ++ infinite_left_right)

    grid
    |> Enum.reject(fn {_, coordinate} -> is_nil(coordinate) or coordinate in infinites end)
    |> Enum.into(%{})
  end

  @doc """
  Count the area each coordinate controls in the given grid

  ## Example:

      iex> count_area(%{{1, 1} => {1, 1}, {2, 2} => {2, 2}, {2, 3} => {2, 2}})
      %{{1, 1} => 1, {2, 2} => 2}
  """
  def count_area(grid) do
    grid
    |> Enum.reduce(%{}, fn {_, coordinate}, acc -> Map.update(acc, coordinate, 1, &(&1 + 1)) end)
  end

  @doc """
  Solve part 2
  """
  def part2(input, max_distance \\ 10_000), do: input |> safe_points(max_distance) |> length()

  @doc """
  Find the safe points whose total distance to the coordinates is less than the max distance

  ## Example:

      AB.  -->  434  -->  434
      ..C       545       .4.

      iex> safe_points([{1, 1}, {2, 1}, {3, 2}], 5)
      [{1, 1}, {2, 1}, {2, 2}, {3, 1}]
  """
  def safe_points(coordinates, max_distance) do
    {x_range, y_range} = ranges(coordinates)

    for x <- x_range,
        y <- y_range,
        sum_distance(coordinates, {x, y}) < max_distance,
        do: {x, y}
  end

  @doc """
  Calculate the total distance from all coordinates to a point

  ## Example:

      iex> sum_distance([{1, 1}, {2, 1}, {3, 2}], {1, 2})
      5
  """
  def sum_distance(coordinates, point),
    do: coordinates |> Enum.map(&distance(&1, point)) |> Enum.sum()

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
