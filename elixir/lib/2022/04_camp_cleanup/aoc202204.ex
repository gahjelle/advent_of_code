defmodule AOC2022.Day04 do
  @moduledoc """
  Advent of Code 2022, day 4: Camp Cleanup.
  """
  require AOC

  @doc """
  Parse input.
  """
  def parse(puzzle_input),
    do: puzzle_input |> String.split("\n", trim: true) |> Enum.map(&parse_pair/1)

  @doc """
  Parse one pair of elf assignments.

  ## Example:

      iex> parse_pair("4-11,3-5")
      {4..11, 3..5}
  """
  def parse_pair(line) do
    line
    |> String.split(",")
    |> then(fn [first, second] -> {parse_elf(first), parse_elf(second)} end)
  end

  @doc """
  Parse one elf assignment.

  ## Example:

      iex> parse_elf("5-19")
      5..19
  """
  def parse_elf(pair) do
    pair
    |> String.split("-")
    |> then(fn [low, high] -> String.to_integer(low)..String.to_integer(high) end)
  end

  @doc """
  Solve part 1.
  """
  def part1(pairs), do: pairs |> Enum.count(&all_overlap?/1)

  @doc """
  Solve part 2.
  """
  def part2(pairs), do: pairs |> Enum.count(&any_overlap?/1)

  @doc """
  Check if a pair of assignments overlap in some way.

  ## Examples:

      iex> overlap?(5..19, 1..7, &Enum.all?/2)
      false
      iex> overlap?(5..19, 1..7, &Enum.any?/2)
      true
      iex> overlap?(7..7, 6..8, &Enum.all?/2)
      true
  """
  def overlap?(small, big, any_all), do: small |> any_all.(fn id -> id in big end)

  @doc """
  Check if one assignment in a pair completely overlaps the other.

  ## Examples:

      iex> all_overlap?({5..7, 5..7})
      true
      iex> all_overlap?({1..4, 5..9})
      false
      iex> all_overlap?({1..100, 42..42})
      true
  """
  def all_overlap?({first, second}),
    do: overlap?(first, second, &Enum.all?/2) || overlap?(second, first, &Enum.all?/2)

  @doc """
  Check if there are any overlaps in the assignments of a pair of elves.

  ## Examples:

      iex> any_overlap?({5..7, 5..7})
      true
      iex> any_overlap?({1..4, 5..9})
      false
      iex> any_overlap?({1..42, 42..100})
      true
  """
  def any_overlap?({first, second}),
    do: overlap?(first, second, &Enum.any?/2) || overlap?(second, first, &Enum.any?/2)

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
