defmodule AOC2016.Day01 do
  @moduledoc """
  Advent of Code 2016, day 1: No Time for a Taxicab
  """
  require AOC

  @doc """
  Parse input
  """
  def parse(puzzle_input) do
    puzzle_input
    |> String.split(", ")
    |> Enum.map(&string_to_instruction/1)
  end

  @doc """
  Parse one instruction

  ## Example:

      iex> string_to_instruction("R123")
      {:right, 123}
  """
  def string_to_instruction("L" <> num_steps), do: {:left, num_steps |> String.to_integer()}
  def string_to_instruction("R" <> num_steps), do: {:right, num_steps |> String.to_integer()}

  @doc """
  Solve part 1
  """
  def part1(input) do
    input
    |> Enum.reduce({:north, 0, 0}, fn {hand, num_steps}, {dir, x, y} ->
      step(turn(dir, hand), x, y, num_steps)
    end)
    |> distance()
  end

  @doc """
  Solve part 2
  """
  def part2(input) do
    input
    |> Enum.reduce_while({:north, 0, 0, MapSet.new()}, fn {hand, num_steps}, {dir, x, y, seen} ->
      trace_steps(turn(dir, hand), x, y, num_steps, seen)
    end)
    |> distance()
  end

  @doc """
  Step through a command, stop if passing through a seen location

  ## Examples:

      iex> trace_steps({:east, 2, 2}, 2, MapSet.new())
      {:cont, {:east, 4, 2, MapSet.new([{2, 2}, {3, 2}])}}

      iex> trace_steps({:east, 2, 2}, 2, MapSet.new([{3, 2}]))
      {:halt, {:east, 3, 2}}
  """
  def trace_steps({dir, x, y}, num_steps, seen), do: trace_steps(dir, x, y, num_steps, seen)
  def trace_steps(dir, x, y, 0, seen), do: {:cont, {dir, x, y, seen}}

  def trace_steps(dir, x, y, num_steps, seen) do
    case {x, y} in seen do
      true ->
        {:halt, {dir, x, y}}

      false ->
        trace_steps(step(dir, x, y), num_steps - 1, MapSet.put(seen, {x, y}))
    end
  end

  @doc """
  Turn to change direction

  ## Example:

      iex> turn(:north, :left)
      :west
  """
  def turn(:east, :right), do: :south
  def turn(:east, :left), do: :north
  def turn(:north, :right), do: :east
  def turn(:north, :left), do: :west
  def turn(:south, :right), do: :west
  def turn(:south, :left), do: :east
  def turn(:west, :right), do: :north
  def turn(:west, :left), do: :south

  @doc """
  Take a number of steps in the given direction

  ## Examples:

      iex> step(:north, 1, 1, 5)
      {:north, 1, 6}

      iex> step(:west, 1, 1, 5)
      {:west, -4, 1}
  """
  def step(dir, x, y, num_steps \\ 1)
  def step(:east, x, y, num_steps), do: {:east, x + num_steps, y}
  def step(:north, x, y, num_steps), do: {:north, x, y + num_steps}
  def step(:south, x, y, num_steps), do: {:south, x, y - num_steps}
  def step(:west, x, y, num_steps), do: {:west, x - num_steps, y}

  @doc """
  Calculate the (Manhattan) distance to a position

  ## Examples:

      iex> distance({:north, 1, 6})
      7

      iex> distance({:west, -4, 1})
      5
  """
  def distance({_direction, x, y}), do: abs(x) + abs(y)

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
