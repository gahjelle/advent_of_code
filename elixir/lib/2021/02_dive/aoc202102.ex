defmodule AOC2021.Day02 do
  @moduledoc """
  Advent of Code 2021, day 2: Dive!
  """
  require AOC

  @doc """
  Parse input
  """
  def parse(puzzle_input) do
    puzzle_input |> String.split("\n") |> Enum.map(&parse_command/1)
  end

  @doc """
  Parse a single command into a tuple

  ## Example:

      iex> parse_command("up 12")
      {:up, 12}
  """
  def parse_command("forward " <> steps), do: {:forward, steps |> String.to_integer()}
  def parse_command("up " <> steps), do: {:up, steps |> String.to_integer()}
  def parse_command("down " <> steps), do: {:down, steps |> String.to_integer()}

  @doc """
  Solve part 1
  """
  def part1(input) do
    input |> Enum.reduce({0, 0}, &move/2) |> Tuple.to_list() |> Enum.product()
  end

  @doc """
  Carry out one (part 1) move command

  ## Examples:

      iex> move({:forward, 12}, {10, 20})
      {22, 20}

      iex> move({:up, 3}, {10, 20})
      {10, 17}

      iex> move({:down, 14}, {10, 20})
      {10, 34}
  """
  def move({:forward, steps}, {horizontal_pos, depth}), do: {horizontal_pos + steps, depth}
  def move({:up, steps}, {horizontal_pos, depth}), do: {horizontal_pos, depth - steps}
  def move({:down, steps}, {horizontal_pos, depth}), do: {horizontal_pos, depth + steps}

  @doc """
  Solve part 2
  """
  def part2(input) do
    input
    |> Enum.reduce({0, 0, 0}, &move_with_aim/2)
    |> Tuple.to_list()
    |> Enum.slice(0..1)
    |> Enum.product()
  end

  @doc """
  Carry out one (part 2) move with aim command

  ## Examples:

      iex> move_with_aim({:up, 3}, {10, 20, 3})
      {10, 20, 0}

      iex> move_with_aim({:down, 14}, {10, 20, 3})
      {10, 20, 17}

      iex> move_with_aim({:forward, 12}, {10, 20, 3})
      {22, 56, 3}
  """
  def move_with_aim({:forward, steps}, {horizontal_pos, depth, aim}),
    do: {horizontal_pos + steps, depth + steps * aim, aim}

  def move_with_aim({:up, steps}, {horizontal_pos, depth, aim}),
    do: {horizontal_pos, depth, aim - steps}

  def move_with_aim({:down, steps}, {horizontal_pos, depth, aim}),
    do: {horizontal_pos, depth, aim + steps}

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
