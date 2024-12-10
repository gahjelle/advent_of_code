defmodule AOC2024.Day10 do
  @moduledoc """
  Advent of Code 2024, day 10: Hoof It.
  """
  require AOC

  @doc """
  Parse input.
  """
  def parse(puzzle_input) do
    for {line, row} <- puzzle_input |> String.split("\n", trim: true) |> Enum.with_index(),
        {char, col} <- line |> String.split("", trim: true) |> Enum.with_index(),
        into: %{},
        do: {{row, col}, char |> String.to_integer()}
  end

  @doc """
  Solve part 1.
  """
  def part1(grid) do
    Map.filter(grid, fn {_, height} -> height == 0 end)
    |> Map.keys()
    |> Enum.map(fn trailhead -> find_targets(grid, trailhead, 0) |> MapSet.size() end)
    |> Enum.sum()
  end

  @doc """
  Solve part 2.
  """
  def part2(grid) do
    Map.filter(grid, fn {_, height} -> height == 0 end)
    |> Map.keys()
    |> Enum.map(&count_paths(grid, &1, 0))
    |> Enum.sum()
  end

  def find_targets(_, pos, 9), do: MapSet.new([pos])

  def find_targets(grid, {row, col}, height) do
    [{0, 1}, {1, 0}, {0, -1}, {-1, 0}]
    |> Enum.map(fn {drow, dcol} ->
      new_pos = {row + drow, col + dcol}

      if Map.get(grid, new_pos) == height + 1,
        do: find_targets(grid, new_pos, height + 1),
        else: MapSet.new()
    end)
    |> Enum.reduce(&MapSet.union/2)
  end

  def count_paths(_, _, 9), do: 1

  def count_paths(grid, {row, col}, height) do
    [{0, 1}, {1, 0}, {0, -1}, {-1, 0}]
    |> Enum.map(fn {drow, dcol} ->
      new_pos = {row + drow, col + dcol}
      if Map.get(grid, new_pos) == height + 1, do: count_paths(grid, new_pos, height + 1), else: 0
    end)
    |> Enum.sum()
  end

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
