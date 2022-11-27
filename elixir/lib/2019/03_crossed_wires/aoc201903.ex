defmodule AOC2019.Day03 do
  @moduledoc """
  Advent of Code 2019, day 3: Crossed Wires
  """
  require AOC

  @doc """
  Parse input.
  """
  def parse(puzzle_input) do
    [first, second] = puzzle_input |> String.split("\n")
    {parse_wire(first), parse_wire(second)}
  end

  @doc """
  Parse one wire input into coordinates.

  ## Example:

      iex> parse_wire("U2,R1,D3,L2")
      [{0, 1}, {0, 2}, {1, 2}, {1, 1}, {1, 0}, {1, -1}, {0, -1}, {-1, -1}]
  """
  def parse_wire(wire) do
    parse_wire(
      wire
      |> String.split(",")
      |> Enum.map(fn <<dir, steps::binary>> -> {dir, String.to_integer(steps)} end),
      {0, 0},
      []
    )
  end

  def parse_wire([{_, 0} | tail], current, coords), do: parse_wire(tail, current, coords)

  def parse_wire([{dir, steps} | tail], current, coords) do
    next = step(current, dir)
    parse_wire([{dir, steps - 1} | tail], next, [next | coords])
  end

  def parse_wire([], _, coords), do: coords |> Enum.reverse()

  @doc """
  Solve part 1.
  """
  def part1({first, second}) do
    MapSet.intersection(MapSet.new(first), MapSet.new(second))
    |> Enum.map(&manhattan/1)
    |> Enum.min()
  end

  @doc """
  Solve part 2.
  """
  def part2({first, second}) do
    {first_map, second_map} = {enumerate_steps(first), enumerate_steps(second)}

    MapSet.intersection(
      first_map |> Map.keys() |> MapSet.new(),
      second_map |> Map.keys() |> MapSet.new()
    )
    |> Enum.map(fn coords -> first_map[coords] + second_map[coords] end)
    |> Enum.min()
  end

  @doc """
  Take one step in the given direction.

  ## Examples:

      iex> step({0, 0}, ?R)
      {1, 0}
      iex> step({-2, 4}, ?D)
      {-2, 3}
  """
  def step({x, y}, ?U), do: {x, y + 1}
  def step({x, y}, ?R), do: {x + 1, y}
  def step({x, y}, ?D), do: {x, y - 1}
  def step({x, y}, ?L), do: {x - 1, y}

  @doc """
  Manhattan metric.

  ## Examples:

      iex> manhattan({3, 5})
      8
      iex> manhattan({-7, 2})
      9
  """
  def manhattan({first, second}), do: abs(first) + abs(second)

  @doc """
  Enumerate the steps for each coordinate

  ## Example:

      iex> enumerate_steps([{0, 1}, {0, 2}, {1, 2}, {1, 1}, {0, 1}, {-1, 1}])
      %{{0, 1} => 1, {0, 2} => 2, {1, 2} => 3, {1, 1} => 4, {-1, 1} => 6}
  """
  def enumerate_steps(steps), do: enumerate_steps(steps, 1, %{})
  def enumerate_steps([], _, done), do: done

  def enumerate_steps([step | steps], num, done),
    do: enumerate_steps(steps, num + 1, Map.put_new(done, step, num))

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
