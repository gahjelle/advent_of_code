defmodule AOC2024.Day06 do
  @moduledoc """
  Advent of Code 2024, day 6: Guard Gallivant.
  """
  require AOC

  @doc """
  Parse input.
  """
  def parse(puzzle_input) do
    grid =
      for {line, row} <- puzzle_input |> String.split("\n", trim: true) |> Enum.with_index(),
          {char, col} <- line |> String.split("", trim: true) |> Enum.with_index(),
          into: %{},
          do: {{row, col}, char}

    start = grid |> Map.filter(fn {_, char} -> char == "^" end) |> Map.keys() |> hd()
    {grid |> Map.put(start, "."), start}
  end

  @doc """
  Solve part 1.

  Currently off by one ...
  """
  def part1({grid, start}) do
    grid |> walk(start) |> MapSet.size()
  end

  @doc """
  Solve part 2.
  """
  def part2({grid, start}) do
    grid
    |> walk(start)
    |> MapSet.filter(&(&1 != start))
    |> Task.async_stream(fn obstacle -> walk(Map.put(grid, obstacle, "#"), start) end)
    |> Enum.reject(fn {:ok, result} -> result end)
    |> Enum.count()
  end

  @doc """
  Walk the grid from start until you exit the grid or find a loop.
  """
  def walk(grid, start), do: walk(grid, start, {-1, 0}, MapSet.new(), MapSet.new())

  def walk(grid, pos, dir, path, seen) do
    if MapSet.member?(seen, {pos, dir}), do: nil, else: walk_step(grid, pos, dir, path, seen)
  end

  defp walk_step(grid, pos = {row, col}, dir = {drow, dcol}, path, seen) do
    new_pos = {row + drow, col + dcol}

    if Map.has_key?(grid, new_pos) do
      case Map.get(grid, new_pos) do
        char when char in [".", "^"] ->
          walk(grid, new_pos, dir, MapSet.put(path, pos), MapSet.put(seen, {pos, dir}))

        "#" ->
          walk(grid, pos, {dcol, -drow}, path, seen)
      end
    else
      MapSet.put(path, pos)
    end
  end

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
