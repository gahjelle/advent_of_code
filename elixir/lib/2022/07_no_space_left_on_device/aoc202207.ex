defmodule AOC2022.Day07 do
  @moduledoc """
  Advent of Code 2022, day 7: No Space Left On Device.
  """
  require AOC

  @doc """
  Parse input.
  """
  def parse(puzzle_input),
    do: puzzle_input |> String.split("\n", trim: true) |> parse_files([""], %{"/" => 0})

  @doc """
  Parse shell commands to create a file tree.
  """
  def parse_files([], _, tree), do: tree

  def parse_files([<<"$ cd ", dir::binary>> | commands], cwd, tree),
    do: parse_files(commands, add_dir(cwd, dir), tree)

  def parse_files([<<"$ ls">> | commands], cwd, tree), do: parse_files(commands, cwd, tree)

  def parse_files([<<"dir ", dir::binary>> | commands], cwd, tree),
    do: parse_files(commands, cwd, Map.put(tree, repr_dir(cwd, dir), 0))

  def parse_files([file | commands], cwd, tree) do
    [size, name] = String.split(file)
    parse_files(commands, cwd, Map.put(tree, repr_dir(cwd, name), String.to_integer(size)))
  end

  defp add_dir([top | tree], dir) do
    case dir do
      "/" -> [""]
      ".." -> tree
      dir -> [dir, top | tree]
    end
  end

  defp repr_dir(dir, file) do
    [file | dir] |> Enum.reverse() |> Enum.join("/")
  end

  @doc """
  Solve part 1.
  """
  def part1(tree),
    do: tree |> dir_sizes() |> Enum.filter(fn size -> size <= 100_000 end) |> Enum.sum()

  @doc """
  Solve part 2.
  """
  def part2(tree) do
    target = (tree |> Map.values() |> Enum.sum()) - 40_000_000
    tree |> dir_sizes() |> Enum.sort() |> Enum.find(fn size -> size > target end)
  end

  @doc """
  Calculate the total size of each directory, including subdirectories.
  """
  def dir_sizes(tree) do
    Map.filter(tree, fn {_, size} -> size == 0 end)
    |> Map.keys()
    |> Enum.map(fn dir ->
      tree
      |> Map.filter(fn {name, _} -> String.starts_with?(name, dir <> "/") end)
      |> Enum.reduce(0, fn {_, size}, total -> total + size end)
    end)
  end

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
