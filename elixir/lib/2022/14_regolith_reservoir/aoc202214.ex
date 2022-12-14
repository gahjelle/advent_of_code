defmodule AOC2022.Day14 do
  @moduledoc """
  Advent of Code 2022, day 14: Regolith Reservoir.
  """
  require AOC

  @doc """
  Parse input.
  """
  def parse(puzzle_input) do
    puzzle_input
    |> String.split("\n", trim: true)
    |> Enum.flat_map(&parse_structure/1)
    |> Map.from_keys(:rock)
  end

  @doc """
  Parse one rock structure.

  ## Example:

      iex> parse_structure("4,4 -> 6,4 -> 6,2")
      [{4, 4}, {5, 4}, {6, 4}, {6, 4}, {6, 3}, {6, 2}]
  """
  def parse_structure(line),
    do:
      line
      |> String.split(" -> ", trim: true)
      |> Enum.chunk_every(2, 1, :discard)
      |> Enum.flat_map(fn [first, last] -> parse_line(first, last) end)

  @doc """
  Parse one line of rocks.

  ## Examples:

      iex> parse_line("12,5", "9,5")
      [{12, 5}, {11, 5}, {10, 5}, {9, 5}]
      iex> parse_line("7,3", "7,5")
      [{7, 3}, {7, 4}, {7, 5}]
  """
  def parse_line(first, last) do
    [first_col, first_row] = first |> String.split(",") |> Enum.map(&String.to_integer/1)
    [last_col, last_row] = last |> String.split(",") |> Enum.map(&String.to_integer/1)

    case {last_col - first_col, last_row - first_row} do
      {dcol, drow} when dcol > 0 or drow > 0 ->
        line(first_col..last_col, first_row..last_row)

      {dcol, _} when dcol < 0 ->
        line(first_col..last_col//-1, first_row..last_row)

      {_, drow} when drow < 0 ->
        line(first_col..last_col, first_row..last_row//-1)
    end
  end

  @doc """
  Expand line ranges into points on the line.

  ## Examples:

      iex> line(1..3, 2..2)
      [{1, 2}, {2, 2}, {3, 2}]
      iex> line(4..4, 5..1//-1)
      [{4, 5}, {4, 4}, {4, 3}, {4, 2}, {4, 1}]
  """
  def line(cols, rows), do: for(col <- cols, row <- rows, do: {col, row})

  @doc """
  Solve part 1.
  """
  def part1(rocks) do
    abyss = rocks |> Map.keys() |> Enum.map(&elem(&1, 1)) |> Enum.max()

    simulate_sand(rocks, {500, 0}, abyss) |> Enum.count(fn {_, elem} -> elem == :sand end)
  end

  @doc """
  Solve part 2.
  """
  def part2(rocks) do
    floor = rocks |> Map.keys() |> Enum.map(&elem(&1, 1)) |> Enum.max() |> then(&(&1 + 2))

    0..1000
    |> Enum.reduce(rocks, fn col, cave -> Map.put(cave, {col, floor}, :floor) end)
    |> simulate_sand({500, 0}, floor)
    |> Enum.count(fn {_, elem} -> elem == :sand end)
  end

  @doc """
  Simulate sand

  ## Examples:

      iex> rocks = %{{9, 3} => :rock, {10, 3} => :rock, {11, 3} => :rock}
      iex> simulate_sand(rocks, {10, 0}, 3)
      %{{9, 3} => :rock, {10, 3} => :rock, {11, 3} => :rock, {10, 2} => :sand}
      iex> simulate_sand(rocks, {10, 2}, 3)
      %{{9, 3} => :rock, {10, 3} => :rock, {11, 3} => :rock, {10, 2} => :sand}
      iex> simulate_sand(rocks, {9, 0}, 3)
      %{{9, 3} => :rock, {10, 3} => :rock, {11, 3} => :rock}
  """
  def simulate_sand(rocks, source, abyss) do
    Stream.cycle([source])
    |> Enum.reduce_while(rocks, fn source, cave ->
      case pour_sand_unit(cave, source, abyss) do
        nil -> {:halt, cave}
        ^source -> {:halt, Map.put(cave, source, :sand)}
        sand -> {:cont, Map.put(cave, sand, :sand)}
      end
    end)
  end

  @doc """
  Pour one unit of sand from the source.

  Report nil if the sand falls into the abyss, otherwise the end position.

  ## Examples:

      iex> pour_sand_unit(%{{9, 3} => :rock}, {10, 0}, 3)
      nil
      iex> rocks = %{{9, 3} => :rock, {10, 3} => :rock, {11, 3} => :rock}
      iex> pour_sand_unit(rocks, {10, 0}, 3)
      {10, 2}
      iex> pour_sand_unit(rocks |> Map.put({10, 2}, :sand), {10, 0}, 3)
      nil
  """
  def pour_sand_unit(_, {_, row}, abyss) when row >= abyss, do: nil

  def pour_sand_unit(cave, {col, row}, abyss) do
    cond do
      not Map.has_key?(cave, {col, row + 1}) ->
        pour_sand_unit(cave, {col, row + 1}, abyss)

      not Map.has_key?(cave, {col - 1, row + 1}) ->
        pour_sand_unit(cave, {col - 1, row + 1}, abyss)

      not Map.has_key?(cave, {col + 1, row + 1}) ->
        pour_sand_unit(cave, {col + 1, row + 1}, abyss)

      true ->
        {col, row}
    end
  end

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
