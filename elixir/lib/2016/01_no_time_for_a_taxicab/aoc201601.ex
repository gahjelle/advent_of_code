defmodule AOC2016.Day01 do
  @moduledoc """
  Advent of Code 2016, day 1: No Time for a Taxicab
  """
  require AOC

  def parse(puzzle_input) do
    puzzle_input
    |> String.split(", ")
    |> Enum.map(&string_to_instruction/1)
  end

  defp string_to_instruction("L" <> num_steps), do: {:left, num_steps |> String.to_integer()}
  defp string_to_instruction("R" <> num_steps), do: {:right, num_steps |> String.to_integer()}

  def part1(input) do
    input
    |> Enum.reduce({:north, 0, 0}, fn {hand, num_steps}, {dir, x, y} ->
      step(turn(dir, hand), x, y, num_steps)
    end)
    |> distance()
  end

  def part2(input) do
    input
    |> Enum.reduce_while({:north, 0, 0, MapSet.new()}, fn {hand, num_steps}, {dir, x, y, seen} ->
      trace_steps(turn(dir, hand), x, y, num_steps, seen)
    end)
    |> distance()
  end

  defp trace_steps({dir, x, y}, num_steps, seen), do: trace_steps(dir, x, y, num_steps, seen)
  defp trace_steps(dir, x, y, 0, seen), do: {:cont, {dir, x, y, seen}}

  defp trace_steps(dir, x, y, num_steps, seen) do
    case {x, y} in seen do
      true ->
        {:halt, {dir, x, y}}

      false ->
        trace_steps(step(dir, x, y), num_steps - 1, MapSet.put(seen, {x, y}))
    end
  end

  defp turn(:east, :right), do: :south
  defp turn(:east, :left), do: :north
  defp turn(:north, :right), do: :east
  defp turn(:north, :left), do: :west
  defp turn(:south, :right), do: :west
  defp turn(:south, :left), do: :east
  defp turn(:west, :right), do: :north
  defp turn(:west, :left), do: :south

  defp step(dir, x, y, num_steps \\ 1)
  defp step(:east, x, y, num_steps), do: {:east, x + num_steps, y}
  defp step(:north, x, y, num_steps), do: {:north, x, y + num_steps}
  defp step(:south, x, y, num_steps), do: {:south, x, y - num_steps}
  defp step(:west, x, y, num_steps), do: {:west, x - num_steps, y}

  defp distance({_direction, x, y}), do: abs(x) + abs(y)

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
