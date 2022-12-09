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
    shape = {max_row(heights), max_col(heights)}

    heights
    |> Map.keys()
    |> Enum.map(&visible?(&1, heights, shape))
    |> Enum.count(& &1)
  end

  @doc """
  Solve part 2.
  """
  def part2(heights) do
    shape = {max_row(heights), max_col(heights)}

    heights
    |> Map.keys()
    |> Enum.map(&scenic_score(&1, heights, shape))
    |> Enum.max()
  end

  @doc """
  Check if a tree is visible from any direction.

  ## Example:

      429
      523
      189

      iex> heights = parse("429\\n523\\n189")
      iex> visible?({1, 1}, heights, {2, 2})
      false
      iex> visible?({0, 2}, heights, {2, 2})
      true
  """
  def visible?(tree, heights, shape),
    do: @directions |> Enum.any?(&is_seen?({tree, heights[tree]}, heights, shape, &1))

  @doc """
  Calculate the scenic score of one tree.

  ## Example:

      iex> heights = parse("30373\\n25512\\n65332\\n33549\\n35390")
      iex> scenic_score({1, 2}, heights, {4, 4})
      4
      iex> scenic_score({3, 2}, heights, {4, 4})
      8
  """
  def scenic_score(tree, heights, shape) do
    @directions
    |> Enum.map(&sees_trees({tree, heights[tree]}, heights, shape, &1))
    |> Enum.product()
  end

  @doc """
  Check if one tree is seen in the given direction.

  ## Example:

      469
      563
      189

      iex> heights = parse("469\\n563\\n189")
      iex> is_seen?({{1, 1}, 6}, heights, {2, 2}, :right)
      true
      iex> is_seen?({{1, 1}, 6}, heights, {2, 2}, :down)
      false
  """
  def is_seen?({{row, col}, height}, heights, {rows, _}, :up),
    do: (row + 1)..rows//1 |> Enum.all?(&(heights[{&1, col}] < height))

  def is_seen?({{row, col}, height}, heights, _, :down),
    do: 0..(row - 1)//1 |> Enum.all?(&(heights[{&1, col}] < height))

  def is_seen?({{row, col}, height}, heights, {_, cols}, :left),
    do: (col + 1)..cols//1 |> Enum.all?(&(heights[{row, &1}] < height))

  def is_seen?({{row, col}, height}, heights, _, :right),
    do: 0..(col - 1)//1 |> Enum.all?(&(heights[{row, &1}] < height))

  @doc """
  Count how many trees is seen from one tree in the given direction.

  ## Example:

      469
      563
      189

      iex> heights = parse("469\\n563\\n189")
      iex> sees_trees({{0, 2}, 9}, heights, {3, 3}, :down)
      2
      iex> sees_trees({{2, 1}, 8}, heights, {3, 3}, :up)
      2
      iex> sees_trees({{0, 0}, 4}, heights, {3, 3}, :left)
      0
  """
  def sees_trees({{row, col}, height}, heights, _, :up),
    do:
      (row - 1)..0//-1
      |> Enum.find_index(&(heights[{&1, col}] >= height))
      |> then(&if is_nil(&1), do: row, else: &1 + 1)

  def sees_trees({{row, col}, height}, heights, {rows, _}, :down),
    do:
      (row + 1)..rows//1
      |> Enum.find_index(&(heights[{&1, col}] >= height))
      |> then(&if is_nil(&1), do: rows - row, else: &1 + 1)

  def sees_trees({{row, col}, height}, heights, _, :left),
    do:
      (col - 1)..0//-1
      |> Enum.find_index(&(heights[{row, &1}] >= height))
      |> then(&if is_nil(&1), do: col, else: &1 + 1)

  def sees_trees({{row, col}, height}, heights, {_, cols}, :right),
    do:
      (col + 1)..cols//1
      |> Enum.find_index(&(heights[{row, &1}] >= height))
      |> then(&if is_nil(&1), do: cols - col, else: &1 + 1)

  defp max_row(heights), do: heights |> Map.keys() |> Enum.map(&elem(&1, 0)) |> Enum.max()
  defp max_col(heights), do: heights |> Map.keys() |> Enum.map(&elem(&1, 1)) |> Enum.max()

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
