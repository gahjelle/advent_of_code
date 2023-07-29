defmodule AOC2018.Day08 do
  @moduledoc """
  Advent of Code 2018, day 8: Memory Maneuver.
  """
  require AOC

  @doc """
  Parse input.
  """
  def parse(puzzle_input), do: puzzle_input |> String.split() |> Enum.map(&String.to_integer/1)

  @doc """
  Solve part 1.
  """
  def part1(numbers), do: numbers |> get_metadata() |> Enum.sum()

  @doc """
  Solve part 2.
  """
  def part2(numbers), do: numbers |> get_value()

  @doc """
  Parse the metadata from a data stream of numbers.

  ## Examples:

      iex> get_metadata([0, 2, 3, 4])
      [3, 4]

      iex> get_metadata([1, 1, 0, 2, 10, 11, 99])
      [10, 11, 99]

      iex> get_metadata([1, 0, 0, 1, 201808])
      [201808]

      iex> get_metadata([2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2])
      [99, 2, 10, 11, 12, 1, 1, 2]
  """
  def get_metadata(numbers) do
    {_numbers = [], metadata} = get_metadata(numbers, [])
    metadata |> Enum.reverse()
  end

  def get_metadata([], metadata), do: {[], metadata}

  def get_metadata([0, 0 | numbers], metadata), do: {numbers, metadata}

  def get_metadata([0, num_meta, metahead | numbers], metadata) do
    get_metadata([0, num_meta - 1 | numbers], [metahead | metadata])
  end

  def get_metadata([num_children, num_meta | numbers], metadata) do
    {rest, child_meta} = get_metadata(numbers, [])
    get_metadata([num_children - 1, num_meta | rest], metadata ++ child_meta)
  end

  @doc """
  Parse the node value from a data stream of numbers.

  ## Examples:

      iex> get_value([0, 2, 3, 4])
      3 + 4

      iex> get_value([1, 1, 0, 2, 10, 11, 1])
      10 + 11

      iex> get_value([1, 0, 0, 1, 201808])
      0

      iex> get_value([2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2])
      (10 + 11 + 12) + (10 + 11 + 12) + 0
  """
  def get_value(numbers) do
    {_numbers = [], value} = get_value(numbers, 0)
    value
  end

  def get_value([], acc), do: {[], acc}
  def get_value([0, 0 | numbers], acc), do: {numbers, acc}
  def get_value([0, num, meta | numbers], acc), do: get_value([0, num - 1 | numbers], acc + meta)

  def get_value([num_children, num_meta | numbers], acc) do
    {numbers, children} =
      1..num_children
      |> Enum.reduce({numbers, []}, fn _, {numbers, children} ->
        {numbers, value} = get_value(numbers, 0)
        {numbers, [value | children]}
      end)

    {metadata, numbers} = Enum.split(numbers, num_meta)

    value =
      metadata
      |> Enum.filter(fn index -> index >= 1 and index <= num_children end)
      |> Enum.map(&Enum.at(children, num_children - &1, 0))
      |> Enum.sum()

    {numbers, value + acc}
  end

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
