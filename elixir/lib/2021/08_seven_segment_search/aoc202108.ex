defmodule AOC2021.Day08 do
  @moduledoc """
  Advent of Code 2021, day 8: Seven Segment Search

  Credits to Steven Braun for the fingerprinting idea
  """
  require AOC

  @words [
    'abcefg',
    'cf',
    'acdeg',
    'acdfg',
    'bcdf',
    'abdfg',
    'abdefg',
    'acf',
    'abcdefg',
    'abcdfg'
  ]
  @counts @words |> Enum.concat() |> Enum.frequencies()
  @digits @words
          |> Enum.with_index()
          |> Enum.map(fn {word, digit} ->
            {word |> Enum.map(&Map.get(@counts, &1)) |> Enum.sum(), digit}
          end)
          |> Enum.into(%{})

  @doc """
  Parse input
  """
  def parse(puzzle_input) do
    lines = puzzle_input |> String.split("\n") |> Enum.map(&parse_line/1)
    {lines |> Enum.map(&elem(&1, 0)), lines |> Enum.map(&elem(&1, 1))}
  end

  @doc """
  Parse one line of input

  ## Example:

      iex> parse_line("acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf")
      {['abcdefg', 'bcdef', 'acdfg', 'abcdf', 'abd', 'abcdef', 'bcdefg', 'abef', 'abcdeg', 'ab'],
       ['bcdef', 'abcdf', 'bcdef', 'abcdf']}
  """
  def parse_line(line) do
    [wires, output] = line |> String.split(" | ")

    {wires
     |> String.split(" ")
     |> Enum.map(fn word -> word |> String.to_charlist() |> Enum.sort() end),
     output
     |> String.split(" ")
     |> Enum.map(fn word -> word |> String.to_charlist() |> Enum.sort() end)}
  end

  @doc """
  Solve part 1
  """
  def part1({_, output}), do: output |> Enum.map(&count_unique/1) |> Enum.sum()

  @doc """
  Solve part 2
  """
  def part2({wires, output}),
    do: Enum.zip(wires, output) |> Enum.map(&deduce_number/1) |> Enum.sum()

  @doc """
  Count number of wire words that can be uniquely determined

  I.e. those words with length 2 (one), 3 (seven), 4 (four), and 7 (eight).

  ## Example:

      iex> count_unique(['ab', 'acdef', 'defg', 'abdefg'])
      2
  """
  def count_unique(words) do
    numbers = MapSet.new([2, 3, 4, 7])

    words
    |> Enum.map(&length/1)
    |> Enum.count(&MapSet.member?(numbers, &1))
  end

  @doc """
  Deduce the output number for a given list of wires

  ## Example:

      iex> deduce_number({['be','abcdefg','bcdefg','acdefg','bceg','cdefg','abdefg','bcdef','abcdf','bde'],
      ...>                ['abcdefg', 'bcdef', 'bcdefg', 'bceg']})
      8394
  """
  def deduce_number({wires, output}) do
    count = wires |> Enum.concat() |> Enum.frequencies()
    output |> Enum.map(&fingerprint(&1, count)) |> Integer.undigits()
  end

  @doc """
  Use fingerprint to convert a word to a digit

  ## Example:

      iex> fingerprint('bceg', %{?a => 4, ?b => 8, ?c => 7, ?d => 8, ?e => 9, ?f => 7, ?g => 6})
      4
  """
  def fingerprint(word, counts) do
    Map.get(
      @digits,
      word |> Enum.map(&Map.get(counts, &1)) |> Enum.sum()
    )
  end

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
