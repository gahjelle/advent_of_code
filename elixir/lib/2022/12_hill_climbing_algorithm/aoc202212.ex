defmodule AOC2022.Day12 do
  @moduledoc """
  Advent of Code 2022, day 12: Hill Climbing Algorithm.
  """
  require AOC

  @doc """
  Parse input.
  """
  def parse(puzzle_input) do
    grid =
      for {line, row} <- puzzle_input |> String.split("\n", trim: true) |> Enum.with_index(),
          {char, col} <- line |> String.to_charlist() |> Enum.with_index(),
          do: {{row, col}, char - ?a},
          into: %{}

    start = grid |> Enum.find(fn {_, height} -> height == ?S - ?a end) |> elem(0)
    goal = grid |> Enum.find(fn {_, height} -> height == ?E - ?a end) |> elem(0)

    {grid |> Map.put(start, 0) |> Map.put(goal, ?z - ?a), start, goal}
  end

  @doc """
  Solve part 1.
  """
  def part1({heights, start, goal}), do: heights |> find_path(start, goal)

  @doc """
  Solve part 2.

  This is a suboptimal solution as it tries all possible startpoints. A better
  solution would be to begin exploring at the target square and move backwards.
  """
  def part2({heights, _, goal}) do
    heights
    |> Map.filter(fn {_, height} -> height == 0 end)
    |> Map.keys()
    |> Task.async_stream(&find_path(heights, &1, goal))
    |> Stream.map(fn {:ok, num_steps} -> num_steps end)
    |> Enum.min()
  end

  @doc """
  Find the shortest path from start to goal while never increasing more than 1 height step.

  ## Example:

      AMlkjnm       oO<<<<<
      brfgskl  -->  v.>v.>^
      cdehijx       >>^>>^.

      iex> heights = %{{0, 0} => 0, {0, 1} => 12, {0, 2} => 11, {0, 3} => 10, {0, 4} => 9,
      ...>     {0, 5} => 13, {0, 6} => 12, {1, 0} => 1, {1, 1} => 17, {1, 2} => 5,
      ...>     {1, 3} => 6, {1, 4} => 18, {1, 5} => 10, {1, 6} => 11, {2, 0} => 2,
      ...>     {2, 1} => 3, {2, 2} => 4, {2, 3} => 7, {2, 4} => 8, {2, 5} => 9, {2, 6} => 23}
      iex> find_path(heights, {0, 0}, {0, 1})
      17
  """
  def find_path(heights, start, goal),
    do: find_path(heights, [{0, start}], %{start => 0}, goal)

  def find_path(_, [{num_steps, goal} | _], _, goal), do: num_steps
  def find_path(_, [], _, _), do: nil

  def find_path(heights, [{num_steps, current} | queue], best, goal) do
    neighbors =
      next_steps(heights, current)
      |> Enum.reject(fn step -> Map.has_key?(best, step) && best[step] <= num_steps + 1 end)

    {queue, best} =
      for next <- neighbors,
          reduce: {queue, best} do
        {queue, best} ->
          {queue ++ [{num_steps + 1, next}], Map.put(best, next, num_steps + 1)}
      end

    find_path(heights, queue, best, goal)
  end

  @doc """
  Find possible next steps from the current position.

  ## Example:

      .6.
      354
      .7.

      iex> heights = %{{0, 1} => 6, {1, 0} => 3, {1, 1} => 5, {1, 2} => 4, {2, 1} => 7}
      iex> next_steps(heights, {1, 1})
      [{0, 1}, {1, 0}, {1, 2}]
      iex> next_steps(heights, {1, 2})
      [{1, 1}]
  """
  def next_steps(heights, {row, col} = current) do
    [{row, col - 1}, {row, col + 1}, {row - 1, col}, {row + 1, col}]
    |> Enum.filter(fn rc -> Map.has_key?(heights, rc) end)
    |> Enum.into(%{}, fn rc -> {rc, heights[rc]} end)
    |> Map.filter(fn {_, height} -> height - heights[current] <= 1 end)
    |> Map.keys()
  end

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
