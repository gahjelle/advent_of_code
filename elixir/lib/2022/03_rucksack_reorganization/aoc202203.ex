defmodule AOC2022.Day03 do
  @moduledoc """
  Advent of Code 2022, day 3: Rucksack Reorganization.
  """
  require AOC

  @doc """
  Parse input.
  """
  def parse(puzzle_input),
    do: puzzle_input |> String.split("\n", trim: true) |> Enum.map(&String.to_charlist/1)

  @doc """
  Solve part 1.
  """
  def part1(rucksack), do: rucksack |> Enum.map(&find_item/1) |> Enum.sum()

  @doc """
  Solve part 2.
  """
  def part2(rucksack),
    do: rucksack |> Enum.chunk_every(3) |> Enum.map(&find_common/1) |> Enum.sum()

  @doc """
  Find the item in common in both rucksack compartments. Return the priority of the item.

  ## Example:

      iex> find_item('geiRarne')
      5
  """
  def find_item(rucksack) do
    per_compartment = div(length(rucksack), 2)

    rucksack |> Enum.chunk_every(per_compartment) |> find_common()
  end

  @doc """
  Find the common item in the given rucksacks or compartments. Return the priority of the item.

  ## Examples:

      iex> find_common(['abc', 'ABc'])
      3
      iex> find_common(['geiRarnE', 'advent', 'wastl'])
      1
  """
  def find_common(rucksacks) do
    rucksacks
    |> Enum.map(&MapSet.new/1)
    |> Enum.reduce(&MapSet.intersection/2)
    |> MapSet.to_list()
    |> hd
    |> to_priority()
  end

  @doc """
  Convert rucksack item to priority.

  - Lowercase item types a through z have priorities 1 through 26.
  - Uppercase item types A through Z have priorities 27 through 52.

  ## Examples:

      iex> to_priority(?G)
      33
      iex> to_priority(?h)
      8
  """
  def to_priority(char) when char <= ?Z, do: char - ?A + 27
  def to_priority(char) when char >= ?a, do: char - ?a + 1

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
