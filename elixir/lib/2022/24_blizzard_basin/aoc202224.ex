defmodule AOC2022.Day24 do
  @moduledoc """
  Advent of Code 2022, day 24: Blizzard Basin.
  """
  require AOC

  @doc """
  Parse input.
  """
  def parse(puzzle_input) do
    map =
      puzzle_input
      |> String.split("\n", trim: true)
      |> Enum.with_index()
      |> Enum.map(fn {line, row} ->
        line
        |> String.split("", trim: true)
        |> Enum.with_index()
        |> Enum.map(fn {char, col} ->
          {
            case char do
              "^" -> :up
              "v" -> :down
              "<" -> :left
              ">" -> :right
              _ -> :none
            end,
            {row, col}
          }
        end)
      end)
      |> Enum.flat_map(& &1)
      |> Enum.reject(fn {dir, _} -> dir == :none end)
      |> Enum.group_by(&elem(&1, 0), &elem(&1, 1))

    size = map |> Map.values() |> Enum.concat() |> Enum.max()
    {size, run_blizzards(map, size)}
  end

  @doc """
  Solve part 1.
  """
  def part1({{rows, cols} = size, blizzards}),
    do: find_path(blizzards, {0, {0, 1}}, {rows + 1, cols}, size)

  @doc """
  Solve part 2.
  """
  def part2({{rows, cols} = size, blizzards}) do
    find_path(blizzards, {0, {0, 1}}, {rows + 1, cols}, size)
    |> then(&find_path(blizzards, {&1, {rows + 1, cols}}, {0, 1}, size))
    |> then(&find_path(blizzards, {&1, {0, 1}}, {rows + 1, cols}, size))
  end

  @doc """
  Run blizzard simulation and record all cycles.

  ## Example:

      iex> map = %{up: [{1, 2}], down: [{2, 2}], left: [{1, 1}, {2, 3}], right: [{1, 3}]}
      iex> run_blizzards(map, {2, 3})
      %{
        0 => MapSet.new([{1, 1}, {1, 2}, {1, 3}, {2, 2}, {2, 3}]),
        1 => MapSet.new([{1, 1}, {1, 2}, {1, 3}, {2, 2}]),
        2 => MapSet.new([{1, 2}, {2, 1}, {2, 2}]),
        3 => MapSet.new([{1, 1}, {1, 2}, {1, 3}, {2, 2}, {2, 3}]),
        4 => MapSet.new([{1, 1}, {1, 2}, {1, 3}, {2, 2}]),
        5 => MapSet.new([{1, 2}, {2, 1}, {2, 2}])
      }
  """
  def run_blizzards(map, {rows, cols} = size) do
    cycle = div(rows * cols, Integer.gcd(rows, cols))

    1..(cycle - 1)
    |> Enum.reduce({map, %{0 => represent(map)}}, fn step, {map, steps} ->
      new_map = step_blizzards(map, size)
      {new_map, Map.put(steps, step, represent(new_map))}
    end)
    |> elem(1)
  end

  @doc """
  Convert a map of blizzards to a set of points.

  ## Example:

      iex> map = %{up: [{1, 2}], down: [{2, 2}], left: [{1, 1}, {2, 3}], right: [{1, 3}]}
      iex> represent(map)
      MapSet.new([{1, 1}, {1, 2}, {1, 3}, {2, 2}, {2, 3}])
  """
  def represent(map), do: map |> Map.values() |> Enum.concat() |> Enum.into(%MapSet{})

  @doc """
  Move all blizzards one step.

  ## Example:

      iex> map = %{up: [{1, 2}], down: [{2, 2}], left: [{1, 1}, {2, 3}], right: [{1, 3}]}
      iex> step_blizzards(map, {2, 3})
      %{up: [{2, 2}], down: [{1, 2}], left: [{1, 3}, {2, 2}], right: [{1, 1}]}
  """
  def step_blizzards(map, size) do
    Enum.into(map, %{}, fn {dir, blizzards} ->
      {dir, blizzards |> Enum.map(&step_blizzard(dir, &1, size))}
    end)
  end

  defp step_blizzard(:up, {r, c}, {rows, _}), do: {if(r > 1, do: r - 1, else: rows), c}
  defp step_blizzard(:down, {r, c}, {rows, _}), do: {if(r < rows, do: r + 1, else: 1), c}
  defp step_blizzard(:left, {r, c}, {_, cols}), do: {r, if(c > 1, do: c - 1, else: cols)}
  defp step_blizzard(:right, {r, c}, {_, cols}), do: {r, if(c < cols, do: c + 1, else: 1)}

  @doc """
  Find a path from start to goal through the blizzards.
  """
  def find_path(blizzards, start, goal, size) do
    find_path(
      blizzards,
      [start],
      goal,
      size,
      Map.from_keys(blizzards |> Map.keys(), MapSet.new())
    )
  end

  def find_path(_, [{step, goal} | _], goal, _, _), do: step

  def find_path(blizzards, [{step, current} | queue], goal, size, seen) do
    cycles = map_size(blizzards)
    cycle = rem(step, cycles)
    next_cycle = rem(step + 1, cycles)

    if MapSet.member?(seen[cycle], current) or MapSet.member?(blizzards[cycle], current) do
      find_path(blizzards, queue, goal, size, seen)
    else
      new_queue =
        [:down, :right, :wait, :up, :left]
        |> Enum.map(&step(&1, current, size))
        |> Enum.filter(& &1)
        |> Enum.reject(fn pos ->
          MapSet.member?(seen[next_cycle], pos) or MapSet.member?(blizzards[next_cycle], pos)
        end)
        |> Enum.map(&{step + 1, &1})
        |> then(fn steps -> queue ++ steps end)

      find_path(
        blizzards,
        new_queue,
        goal,
        size,
        Map.update!(seen, cycle, &MapSet.put(&1, current))
      )
    end
  end

  @doc """
  Take one step inside the canyon.

  ## Examples:

      iex> step(:down, {2, 2}, {5, 5})
      {3, 2}
      iex> step(:left, {3, 1}, {5, 5})
      nil
      iex> step(:wait, {5, 5}, {5, 5})
      {5, 5}
      iex> step(:up, {1, 1}, {5, 5})
      {0, 1}
      iex> step(:up, {1, 2}, {5, 5})
      nil
  """
  def step(:down, {row, col}, {rows, cols}),
    do: if(row < rows or (col == cols and row == rows), do: {row + 1, col})

  def step(:up, {row, col}, _), do: if(row > 1 or (col == 1 and row == 1), do: {row - 1, col})
  def step(:left, {row, col}, {rows, _}), do: if(col > 1 and row <= rows, do: {row, col - 1})
  def step(:right, {row, col}, {_, cols}), do: if(col < cols and row > 0, do: {row, col + 1})
  def step(:wait, current, _), do: current

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
