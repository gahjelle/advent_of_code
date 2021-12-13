defmodule AOC2021.Day09 do
  @moduledoc """
  Advent of Code 2021, day 9: Smoke Basin
  """
  require AOC
  alias AOC2021.Day09.HeightMap

  @doc """
  Parse input
  """
  def parse(puzzle_input) do
    puzzle_input |> HeightMap.from_str()
  end

  @doc """
  Solve part 1
  """
  def part1(height_map) do
    height_map
    |> HeightMap.to_list()
    |> Enum.filter(&HeightMap.low_point?(height_map, &1))
    |> Enum.map(&(height_map.heights[&1] + 1))
    |> Enum.sum()
  end

  @doc """
  Solve part 2
  """
  def part2(height_map) do
    basin_sources =
      height_map |> HeightMap.to_list() |> Enum.filter(&HeightMap.low_point?(height_map, &1))

    basin_sources
    |> Enum.map(fn source -> HeightMap.fill_basin(height_map, source) |> length() end)
    |> Enum.sort(:desc)
    |> Enum.take(3)
    |> Enum.product()
  end

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end

defmodule AOC2021.Day09.HeightMap do
  @moduledoc """
  Struct representing a map with heights, useful as a means of creating positions set only once
  """
  defstruct heights: nil, positions: nil

  @doc """
  Create a HeightMap from a string

  ## Example:

      iex> from_str("09\\n55")
      %HeightMap{
        heights: %{{0, 0} => 0, {0, 1} => 9, {1, 0} => 5, {1, 1} => 5},
        positions: MapSet.new([{0, 0}, {0, 1}, {1, 0}, {1, 1}])
      }
  """
  def from_str(text) do
    heights =
      text
      |> String.split("\n")
      |> Enum.with_index()
      |> Enum.reduce(%{}, fn {line, row}, acc ->
        line
        |> String.split("", trim: true)
        |> Enum.with_index()
        |> Enum.reduce(acc, fn {height, col}, acc ->
          Map.put(acc, {row, col}, height |> String.to_integer())
        end)
      end)

    struct(__MODULE__, %{:heights => heights, :positions => heights |> Map.keys() |> MapSet.new()})
  end

  @doc """
  Represent a HeightMap as a list of its positions

  ## Example:

      iex> from_str("09\\n55") |> to_list()
      [{0, 0}, {0, 1}, {1, 0}, {1, 1}]
  """
  def to_list(height_map), do: height_map.heights |> Map.keys()

  @doc """
  Find neighbors of a position

  ## Examples:

      iex> neighbors(from_str("123\\n456\\n789"), {1, 1})
      [{0, 1}, {1, 0}, {2, 1}, {1, 2}]

      iex> neighbors(from_str("123\\n456\\n789"), {0, 0})
      [{1, 0}, {0, 1}]
  """
  def neighbors(%{positions: positions}, {x, y}) do
    Enum.filter([{x - 1, y}, {x, y - 1}, {x + 1, y}, {x, y + 1}], &MapSet.member?(positions, &1))
  end

  @doc """
  Check if a position is lower than all its neighbors

  ## Examples:

      4 5 6
      7 4 5

      iex> low_point?(from_str("456\\n745"), {0, 1})
      false

      iex> low_point?(from_str("456\\n745"), {1, 1})
      true
  """
  def low_point?(height_map, pos) do
    neighbors(height_map, pos)
    |> Enum.map(fn neighbor -> height_map.heights[pos] < height_map.heights[neighbor] end)
    |> Enum.all?()
  end

  @doc """
  Find the basin connected to source

  ## Examples:

       7 6 9        . . .
       9 9 6   ->   . . #
      (5)3 2        # # #

      iex> fill_basin(from_str("769\\n996\\n532"), {2, 0})
      [{1, 2}, {2, 0}, {2, 1}, {2, 2}]
  """
  def fill_basin(height_map, source),
    do: fill_basin(height_map, [source], MapSet.new())

  def fill_basin(_height_map, [], filled), do: filled |> MapSet.to_list() |> Enum.sort()

  def fill_basin(height_map, [current | queue], filled) do
    if height_map.heights[current] == 9 or MapSet.member?(filled, current) do
      fill_basin(height_map, queue, filled)
    else
      fill_basin(
        height_map,
        queue ++ neighbors(height_map, current),
        MapSet.put(filled, current)
      )
    end
  end
end
