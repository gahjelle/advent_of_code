defmodule AOC2021.Day05 do
  @moduledoc """
  Advent of Code 2021, day 5: Hydrothermal Venture
  """
  require AOC

  @doc """
  Parse input
  """
  def parse(puzzle_input) do
    puzzle_input |> String.split("\n") |> Enum.map(&parse_line/1)
  end

  @doc """
  Parse one line of input

  ## Examples:

      iex> parse_line("8,0 -> 0,8")
      {:diagonal, {8, 0}, {0, 8}}

      iex> parse_line("9,4 -> 3,4")
      {:horisontal, {9, 4}, {3, 4}}

      iex> parse_line("2,2 -> 2,1")
      {:vertical, {2, 2}, {2, 1}}
  """
  def parse_line(line) do
    [[x1, y1], [x2, y2]] =
      line
      |> String.split(" -> ")
      |> Enum.map(fn pt -> pt |> String.split(",") |> Enum.map(&String.to_integer/1) end)

    cond do
      x1 == x2 -> {:vertical, {x1, y1}, {x2, y2}}
      y1 == y2 -> {:horisontal, {x1, y1}, {x2, y2}}
      true -> {:diagonal, {x1, y1}, {x2, y2}}
    end
  end

  @doc """
  Solve part 1
  """
  def part1(input), do: input |> Enum.reject(&(&1 |> elem(0) == :diagonal)) |> count_overlaps()

  @doc """
  Solve part 2
  """
  def part2(input), do: input |> count_overlaps()

  @doc """
  Count the number of points with two or more lines overlapping

  ## Examples:

  iex> count_overlaps([{:horisontal, {4, 2}, {2, 2}},{:vertical, {3, 1}, {3, 3}},{:horisontal, {2, 2}, {0, 2}}])
  2

  iex> count_overlaps([{:diagonal, {2, 0}, {0, 2}},{:horisontal, {0, 2}, {2, 2}},{:vertical, {0, 0}, {0, 2}}])
  1
  """
  def count_overlaps(lines) do
    lines |> overlaps() |> Map.values() |> Enum.count(&(&1 >= 2))
  end

  @doc """
  Find number of time each point is overlapped by lines

  ## Examples:

      iex> overlaps([{:horisontal, {4, 2}, {2, 2}},{:vertical, {3, 1}, {3, 3}},{:horisontal, {2, 2}, {0, 2}}])
      %{{4, 2} => 1, {3, 2} => 2, {2, 2} => 2, {3, 1} => 1, {3, 3} => 1, {1, 2} => 1, {0, 2} => 1}

      iex> overlaps([{:diagonal, {2, 0}, {0, 2}},{:horisontal, {0, 2}, {2, 2}},{:vertical, {0, 0}, {0, 2}}])
      %{{2, 0} => 1, {1, 1} => 1, {0, 2} => 3, {1, 2} => 1, {2, 2} => 1, {0, 0} => 1, {0, 1} => 1}
  """
  def overlaps(lines), do: overlaps(lines, %{})
  def overlaps([], acc), do: acc

  def overlaps([{:vertical, {x, y1}, {x, y2}} | lines], acc),
    do: lines |> overlaps(y1..y2 |> Enum.reduce(acc, fn y, acc -> update(acc, x, y) end))

  def overlaps([{:horisontal, {x1, y}, {x2, y}} | lines], acc),
    do: lines |> overlaps(x1..x2 |> Enum.reduce(acc, fn x, acc -> update(acc, x, y) end))

  def overlaps([{:diagonal, {x1, y1}, {x2, y2}} | lines], acc),
    do:
      lines
      |> overlaps(
        Enum.zip(x1..x2, y1..y2)
        |> Enum.reduce(acc, fn {x, y}, acc -> update(acc, x, y) end)
      )

  defp update(acc, x, y), do: Map.update(acc, {x, y}, 1, &(&1 + 1))

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
