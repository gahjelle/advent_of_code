defmodule AOC2020.Day03 do
  @moduledoc """
  Advent of Code 2020, day 3: Toboggan Trajectory
  """
  require AOC
  alias AOC2020.Day03.Forest

  @doc """
  Parse input
  """
  def parse(puzzle_input), do: puzzle_input |> Forest.from_str()

  @doc """
  Solve part 1
  """
  def part1(input), do: input |> count_trees({3, 1})

  @doc """
  Solve part 2
  """
  def part2(input) do
    [{1, 1}, {3, 1}, {5, 1}, {7, 1}, {1, 2}]
    |> Enum.map(&count_trees(input, &1))
    |> Enum.product()
  end

  @doc """
  Find the path of the toboggan.

  ## Example:

      iex> path(Forest.new(MapSet.new(), 1, 5), {3, 1})
      [{0, 0}, {3, 1}, {6, 2}, {9, 3}, {12, 4}]
  """
  def path(%{height: height}, {dx, dy}) do
    0..(height - 1)//dy
    |> Enum.reduce({[], 0}, fn y, {steps, x} -> {[{x, y} | steps], x + dx} end)
    |> elem(0)
    |> Enum.reverse()
  end

  @doc """
  Count the number of trees that the toboggan crashes with.

  ## Examples:

      #.. | #..#..#..#..#.. ...
      .#. | .#..#..#..#..#. ...
      ..# | ..#..#..#..#..# ...
      ##. | ##.##.##.##.##. ...

      iex> forest = Forest.new(MapSet.new([{0, 0}, {1, 1}, {2, 2}, {0, 3}, {1, 3}]), 3, 4)
      iex> count_trees(forest, {1, 1})
      4
      iex> count_trees(forest, {3, 1})
      2
      iex> count_trees(forest, {1, 2})
      1
  """
  def count_trees(forest, step), do: path(forest, step) |> Enum.count(&Forest.tree?(forest, &1))

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end

defmodule AOC2020.Day03.Forest do
  @moduledoc """
  Struct representing trees
  """
  defstruct trees: MapSet.new(), width: 1, height: 1

  @doc """
  Create a new forest.

  ## Example:

      .# | .#.#.#.#.# ...
      #. | #.#.#.#.#. ...

      iex> new(MapSet.new([{1, 0}, {0, 1}]), 2, 2)
      %AOC2020.Day03.Forest{height: 2, trees: MapSet.new([{0, 1}, {1, 0}]), width: 2}
  """
  def new(trees, width, height),
    do: struct!(__MODULE__, %{trees: trees, width: width, height: height})

  @doc """
  Create a new forest from a string representation.

  ## Example:

      .# | .#.#.#.#.# ...
      #. | #.#.#.#.#. ...

      iex> from_str(".#\\n#.")
      %AOC2020.Day03.Forest{height: 2, trees: MapSet.new([{0, 1}, {1, 0}]), width: 2}
  """
  def from_str(text) do
    {trees, width, height} =
      text
      |> String.split("\n")
      |> Enum.with_index()
      |> Enum.reduce({MapSet.new(), 0, 0}, fn {line, row}, acc ->
        line
        |> String.split("", trim: true)
        |> Enum.with_index()
        |> Enum.reduce(acc, fn {feature, col}, acc ->
          add_feature(acc, feature, col, row)
        end)
      end)

    new(trees, width, height)
  end

  defp add_feature({trees, width, height}, "#", col, row),
    do:
      {MapSet.put(trees, {col, row}), if(col >= width, do: col + 1, else: width),
       if(row >= height, do: row + 1, else: height)}

  defp add_feature({trees, width, height}, _, col, row),
    do:
      {trees, if(col >= width, do: col + 1, else: width),
       if(row >= height, do: row + 1, else: height)}

  @doc """
  Check if there's a tree at the given position.

  ## Examples:

      #.. | #..#..#..#..#.. ...
      .#. | .#..#..#..#..#. ...
      ..# | ..#..#..#..#..# ...
      ##. | ##.##.##.##.##. ...

      iex> forest = new(MapSet.new([{0, 0}, {1, 1}, {2, 2}, {0, 3}, {1, 3}]), 3, 4)
      iex> tree?(forest, {0, 0})
      true
      iex> tree?(forest, {1, 0})
      false
      iex> tree?(forest, {8, 2})
      true
      iex> tree?(forest, {8, 3})
      false
      iex> tree?(forest, {0, 9})
      false
  """
  def tree?(forest, {x, y}), do: MapSet.member?(forest.trees, {rem(x, forest.width), y})
end
