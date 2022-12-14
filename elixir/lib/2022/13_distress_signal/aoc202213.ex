defmodule AOC2022.Day13 do
  @moduledoc """
  Advent of Code 2022, day 13: Distress Signal.
  """
  require AOC

  @doc """
  Parse input.
  """
  def parse(puzzle_input),
    do: puzzle_input |> String.split("\n\n", trim: true) |> Enum.map(&parse_pair/1)

  @doc """
  Parse a pair of packets.

  ## Example:

      iex> parse_pair("[1, [2, 34], [5], 6]\\n[[[1]]]")
      {[1, [2, 34], [5], 6], [[[1]]]}
  """
  def parse_pair(pair),
    do: pair |> String.split("\n") |> Enum.map(&Jason.decode!/1) |> List.to_tuple()

  @doc """
  Solve part 1.
  """
  def part1(packets) do
    packets
    |> Enum.with_index(1)
    |> Enum.filter(fn {{left, right}, _} -> compare(left, right) end)
    |> Enum.map(&elem(&1, 1))
    |> Enum.sum()
  end

  @doc """
  Solve part 2.
  """
  def part2(packets) do
    [{[[2]], [[6]]} | packets]
    |> Enum.flat_map(&Tuple.to_list/1)
    |> Enum.sort(&compare/2)
    |> Enum.with_index(1)
    |> Enum.filter(fn {elem, _} -> elem == [[2]] || elem == [[6]] end)
    |> Enum.map(&elem(&1, 1))
    |> Enum.product()
  end

  @doc """
  Compare two packets.

  ## Examples:

      iex> compare(3, 6)
      true
      iex> compare(11, 11)
      nil
      iex> compare(1, 0)
      false
      iex> compare([1, 2, 3], [1, 3, 2])
      true
      iex> compare([1, 3, 5, 7], [1, 3, 5])
      false
      iex> compare([[1], 2, [3, 4]], [1, [2], 3, [[4]]])
      true
  """
  def compare([head | left_tail], [head | right_tail]), do: compare(left_tail, right_tail)
  def compare([left | _], [right | _]), do: compare(left, right)
  def compare([], right) when is_list(right), do: true
  def compare(left, []) when is_list(left), do: false
  def compare(left, right) when is_list(right), do: compare([left], right)
  def compare(left, right) when is_list(left), do: compare(left, [right])

  def compare(left, right) when is_integer(left) and is_integer(right) do
    if left < right, do: true, else: if(left > right, do: false, else: nil)
  end

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
