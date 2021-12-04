defmodule AOC2021.Day03 do
  @moduledoc """
  Advent of Code 2021, day 3: Binary Diagnostic
  """
  require AOC

  @doc """
  Parse input
  """
  def parse(puzzle_input) do
    puzzle_input
    |> String.split("\n")
    |> Enum.map(fn bn -> bn |> String.split("", trim: true) |> Enum.map(&String.to_integer/1) end)
  end

  @doc """
  Solve part 1
  """
  def part1(input) do
    counts = input |> Enum.zip() |> count_bits()
    gamma_rate = counts |> rate(&>/2) |> Integer.undigits(2)
    epsilon_rate = counts |> rate(&</2) |> Integer.undigits(2)
    gamma_rate * epsilon_rate
  end

  @doc """
  Solve part 2
  """
  def part2(input) do
    o2_generator = input |> filter_rows(&>=/2) |> Integer.undigits(2)
    co2_scrubber = input |> filter_rows(&</2) |> Integer.undigits(2)
    o2_generator * co2_scrubber
  end

  @doc """
  Count the number of bits in columns

  ## Example:

      iex> count_bits([{1, 0, 1, 0}, {0, 1, 1, 1}, {0, 1, 0, 0}])
      {[2, 1, 3], [2, 3, 1]}

      iex> count_bits({1, 0, 1, 1, 0})
      {2, 3}
  """
  def count_bits(rows) when is_list(rows) do
    for bit <- 0..1 do
      rows |> Enum.map(fn bits -> bits |> Tuple.to_list() |> Enum.count(&(&1 == bit)) end)
    end
    |> List.to_tuple()
  end

  def count_bits(column) when is_tuple(column) do
    freqs = column |> Tuple.to_list() |> Enum.frequencies()
    {Map.get(freqs, 0, 0), Map.get(freqs, 1, 0)}
  end

  @doc """
  Calculate gamma and epsilon rates

  ## Examples:

      iex> rate({[2, 1, 1], [1, 2, 2]}, &>/2)
      [0, 1, 1]

      iex> rate({[2, 1, 1], [1, 2, 2]}, &</2)
      [1, 0, 0]
  """
  def rate({num_zeros, num_ones}, compare) do
    Enum.zip(num_zeros, num_ones)
    |> Enum.map(fn {zeros, ones} -> if compare.(ones, zeros), do: 1, else: 0 end)
  end

  @doc """
  Filter out the best matching row based on a comparison function

  ## Examples:

    iex> filter_rows([[1, 0, 1], [0, 1, 1], [0, 1, 0]], &>=/2)
    [0, 1, 1]

    iex> filter_rows([[1, 0, 1], [0, 1, 1], [0, 1, 0]], &<=/2)
    [1, 0, 1]
  """
  def filter_rows(rows, compare), do: filter_rows(rows, compare, [])
  def filter_rows([row], _compare, acc), do: (acc |> Enum.reverse()) ++ row

  def filter_rows(rows, compare, acc) do
    column = rows |> Enum.zip() |> hd
    {zeros, ones} = column |> count_bits()
    bit_to_keep = if compare.(ones, zeros), do: 1, else: 0

    filter_rows(
      Enum.zip(rows, column |> Tuple.to_list())
      |> Enum.flat_map(fn {row, bit} -> if bit == bit_to_keep, do: [row |> tl()], else: [] end),
      compare,
      [bit_to_keep | acc]
    )
  end

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
