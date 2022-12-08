defmodule AOC2022.Day08 do
  @moduledoc """
  Advent of Code 2022, day 8: Treetop Tree House.
  """
  require AOC

  @directions [:up, :down, :left, :right]

  @doc """
  Parse input.
  """
  def parse(puzzle_input) do
    for {line, row} <- puzzle_input |> String.split("\n", trim: true) |> Enum.with_index(),
        {height, col} <- line |> String.split("", trim: true) |> Enum.with_index(),
        into: %{},
        do: {{row, col}, height |> String.to_integer()}
  end

  @doc """
  Solve part 1.
  """
  def part1(heights) do
    heights
    |> Map.keys()
    |> Task.async_stream(&visible?(&1, heights), ordered: false)
    |> Stream.map(fn {:ok, visible} -> visible end)
    |> Enum.count(& &1)
  end

  @doc """
  Solve part 2.
  """
  def part2(heights) do
    heights
    |> Map.keys()
    |> Task.async_stream(&scenic_score(&1, heights))
    |> Stream.map(fn {:ok, score} -> score end)
    |> Enum.max()
  end

  @doc """
  Check if a tree is visible from any direction.

  ## Example:

      429
      523
      189

      iex> heights = parse("429\\n523\\n189")
      iex> visible?({1, 1}, heights)
      false
      iex> visible?({0, 2}, heights)
      true
  """
  def visible?(tree, heights),
    do: @directions |> Enum.any?(&is_seen?({tree, heights[tree]}, heights, &1))

  @doc """
  Calculate the scenic score of one tree.

  ## Example:

      iex> heights = parse("30373\\n25512\\n65332\\n33549\\n35390")
      iex> scenic_score({1, 2}, heights)
      4
      iex> scenic_score({3, 2}, heights)
      8
  """
  def scenic_score(tree, heights) do
    @directions |> Enum.map(&sees_trees({tree, heights[tree]}, heights, &1)) |> Enum.product()
  end

  @doc """
  Check if one tree is seen in the given direction.

  ## Example:

      469
      563
      189

      iex> heights = parse("469\\n563\\n189")
      iex> is_seen?({{1, 1}, 6}, heights, :right)
      true
      iex> is_seen?({{1, 1}, 6}, heights, :down)
      false
  """
  def is_seen?({{row, col}, height}, heights, :up),
    do: (row + 1)..max_row(heights)//1 |> Enum.all?(&(heights[{&1, col}] < height))

  def is_seen?({{row, col}, height}, heights, :down),
    do: 0..(row - 1)//1 |> Enum.all?(&(heights[{&1, col}] < height))

  def is_seen?({{row, col}, height}, heights, :left),
    do: (col + 1)..max_col(heights)//1 |> Enum.all?(&(heights[{row, &1}] < height))

  def is_seen?({{row, col}, height}, heights, :right),
    do: 0..(col - 1)//1 |> Enum.all?(&(heights[{row, &1}] < height))

  @doc """
  Count how many trees is seen from one tree in the given direction.

  ## Example:

      469
      563
      189

      iex> heights = parse("469\\n563\\n189")
      iex> sees_trees({{0, 2}, 9}, heights, :down)
      2
      iex> sees_trees({{2, 1}, 8}, heights, :up)
      2
      iex> sees_trees({{0, 0}, 4}, heights, :left)
      0
  """
  def sees_trees({{row, col}, height}, heights, :up),
    do:
      (row - 1)..0//-1
      |> Enum.find_index(&(heights[{&1, col}] >= height))
      |> then(&if is_nil(&1), do: row, else: &1 + 1)

  def sees_trees({{row, col}, height}, heights, :down),
    do:
      (row + 1)..max_row(heights)//1
      |> Enum.find_index(&(heights[{&1, col}] >= height))
      |> then(&if is_nil(&1), do: max_row(heights) - row, else: &1 + 1)

  def sees_trees({{row, col}, height}, heights, :left),
    do:
      (col - 1)..0//-1
      |> Enum.find_index(&(heights[{row, &1}] >= height))
      |> then(&if is_nil(&1), do: col, else: &1 + 1)

  def sees_trees({{row, col}, height}, heights, :right),
    do:
      (col + 1)..max_col(heights)//1
      |> Enum.find_index(&(heights[{row, &1}] >= height))
      |> then(&if is_nil(&1), do: max_col(heights) - col, else: &1 + 1)

  defp max_row(heights), do: heights |> Map.keys() |> Enum.map(&elem(&1, 0)) |> Enum.max()
  defp max_col(heights), do: heights |> Map.keys() |> Enum.map(&elem(&1, 1)) |> Enum.max()

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
