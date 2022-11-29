defmodule AOC2021.Day15 do
  @moduledoc """
  Advent of Code 2021, day 15: Chiton

  Appreciation and apologies to: https://github.com/josevalim/aoc/blob/main/2021/day-15.livemd
  """
  require AOC

  @doc """
  Parse input
  """
  def parse(puzzle_input) do
    for {line, row} <- Enum.with_index(String.split(puzzle_input, "\n", trim: true)),
        {char, col} <- Enum.with_index(String.split(line, "", trim: true)),
        risk = String.to_integer(char),
        into: %{},
        do: {{row, col}, risk}
  end

  @doc """
  Solve part 1
  """
  def part1(risks), do: risks |> find_safest()

  @doc """
  Solve part 2
  """
  def part2(risks), do: risks |> expand({5, 5}) |> find_safest()

  @doc """
  Use Dijkstra to find the total risk of the safest path through the grid.

  ## Example:

      321      321
      456  ->  ..6
      987      ..7

      iex> risks = parse("321\\n456\\n987")
      iex> find_safest(risks)
      16
  """
  def find_safest(risks) do
    total_risks = %{{0, 0} => 0}
    queue = Heap.min() |> Heap.push({0, {0, 0}})
    target = risks |> Map.keys() |> Enum.max()

    dijkstra(risks, total_risks, queue, target)
  end

  defp dijkstra(risks, total_risks, queue, target) do
    {{risk, {row, col} = node}, queue} = Heap.split(queue)

    if node == target do
      risk
    else
      neighbors = [{row - 1, col}, {row + 1, col}, {row, col - 1}, {row, col + 1}]

      {queue, total_risks} =
        for next <- neighbors,
            Map.has_key?(risks, next),
            next_risk = risk + risks[next],
            next_risk < Map.get(total_risks, next, :infinity),
            reduce: {queue, total_risks} do
          {queue, total_risks} ->
            queue = Heap.push(queue, {next_risk, next})
            total_risks = Map.put(total_risks, next, next_risk)
            {queue, total_risks}
        end

      dijkstra(risks, total_risks, queue, target)
    end
  end

  @doc """
  Expand a grid while increasing the risk level.

  ## Example:
                12|23|34
      12        89|91|12
      89   ->   --+--+--
                23|34|45
                91|12|23

      iex> expand(%{{0, 0} => 1, {0, 1} => 2, {1, 0} => 8, {1, 1} => 9}, {2, 3})
      %{{0, 0} => 1, {0, 1} => 2, {1, 0} => 8, {1, 1} => 9,
        {2, 0} => 2, {2, 1} => 3, {3, 0} => 9, {3, 1} => 1,
        {0, 2} => 2, {0, 3} => 3, {1, 2} => 9, {1, 3} => 1,
        {2, 2} => 3, {2, 3} => 4, {3, 2} => 1, {3, 3} => 2,
        {0, 4} => 3, {0, 5} => 4, {1, 4} => 1, {1, 5} => 2,
        {2, 4} => 4, {2, 5} => 5, {3, 4} => 2, {3, 5} => 3}
  """
  def expand(risks, {height, width}) do
    {max_row, max_col} = risks |> Map.keys() |> Enum.max()
    {rows, cols} = {max_row + 1, max_col + 1}

    for x <- 0..(width - 1), y <- 0..(height - 1), reduce: risks do
      acc ->
        for row <- 0..max_row, col <- 0..max_col, reduce: acc do
          acc ->
            Map.put(acc, {row + rows * y, col + cols * x}, bump(risks[{row, col}], x + y))
        end
    end
  end

  @doc """
  Bump the risk level.

  ## Example:

      iex> bump(3, 4)
      7
      iex> bump(5, 4)
      9
      iex> bump(7, 3)
      1
  """
  def bump(value, add), do: rem(value + add - 1, 9) + 1

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
