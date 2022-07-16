defmodule AOC2018.Day02 do
  @moduledoc """
  Advent of Code 2018, day 2: Inventory Management System
  """
  require AOC

  @doc """
  Parse input
  """
  def parse(puzzle_input) do
    puzzle_input |> String.split("\n") |> Enum.map(&String.to_charlist/1)
  end

  @doc """
  Solve part 1
  """
  def part1(input), do: input |> count_words_with_repeats([2, 3]) |> Enum.product()

  @doc """
  Count the number of words with the given number of repeated characters

  ## Examples:

      iex> count_words_with_repeats(['abcaba', 'de', 'ffg'], [2, 3])
      [2, 1]

      iex> count_words_with_repeats(['abbcccdddd', 'eefff'], [1, 4, 2])
      [1, 1, 2]
  """
  def count_words_with_repeats(words, repeats) do
    words
    |> Enum.map(&check_repeats_in_word(repeats, &1))
    |> Enum.zip()
    |> Enum.map(&Tuple.sum/1)
  end

  @doc """
  Check if any characters are repeated the given number of times

  ## Examples:

      iex> check_repeats_in_word([2, 3], 'abcaba')
      [1, 1]

      iex> check_repeats_in_word([1, 4, 2], 'accceeeee')
      [1, 0, 0]
  """
  def check_repeats_in_word(repeats, word) do
    counts = word |> Enum.frequencies() |> Map.values() |> MapSet.new()
    Enum.map(repeats, fn repeat -> if MapSet.member?(counts, repeat), do: 1, else: 0 end)
  end

  @doc """
  Solve part 2
  """
  def part2(input), do: input |> find_similar() |> List.to_string()

  @doc """
  Find which box IDs that differ by only one character

  ## Example:

      iex> find_similar(['abcde', 'fghij', 'gfhij', 'fguij'])
      'fgij'
  """
  def find_similar([box_id | box_ids]) do
    box_ids |> Enum.find_value(&find_similar(&1, box_id, [], 0)) || find_similar(box_ids)
  end

  def find_similar([head | tail_1], [head | tail_2], same, num_diffs) do
    find_similar(tail_1, tail_2, [head | same], num_diffs)
  end

  def find_similar([_ | tail_1], [_ | tail_2], same, num_diffs) do
    find_similar(tail_1, tail_2, same, num_diffs + 1)
  end

  def find_similar([], [], same, 1), do: same |> Enum.reverse()
  def find_similar([], [], _same, _), do: nil

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
