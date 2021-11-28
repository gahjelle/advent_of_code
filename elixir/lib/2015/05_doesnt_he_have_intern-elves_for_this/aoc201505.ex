defmodule AOC2015.Day05 do
  @moduledoc """
  Advent of Code 2015, day 5: Doesn't He Have Intern-Elves For This?
  """
  require AOC

  @vowels "aeiou"
          |> String.to_charlist()
          |> MapSet.new()

  @doc """
  Parse input
  """
  def parse(puzzle_input) do
    puzzle_input |> String.split("\n") |> Enum.map(&String.to_charlist/1)
  end

  @doc """
  Solve part 1
  """
  def part1(input) do
    input
    |> Enum.filter(fn s -> count_vowels(s) >= 3 && repeated_char?(s) && not_naughty_pairs?(s) end)
    |> Enum.count()
  end

  @doc """
  Count the number of vowels in a char list

  ## Example:

      iex> count_vowels('adventofcode')
      5
  """
  def count_vowels(string), do: Enum.count(string, fn c -> c in @vowels end)

  @doc """
  Check if a char list contains repeated characters

  ## Examples:

      iex> repeated_char?('geirarne')
      false

      iex> repeated_char?('hjelle')
      true
  """
  def repeated_char?([char, char | _]), do: true
  def repeated_char?([_ | tail]), do: repeated_char?(tail)
  def repeated_char?(_), do: false

  @doc """
  Check if char list contains any of the naughty character pairs: ab, cd, pq, xy

  ## Examples:

      iex> not_naughty_pairs?('abba')
      false

      iex> not_naughty_pairs?('inxs')
      true
  """
  def not_naughty_pairs?([c1, c2 | _]) when [c1, c2] in ['ab', 'cd', 'pq', 'xy'], do: false
  def not_naughty_pairs?([_ | tail]), do: not_naughty_pairs?(tail)
  def not_naughty_pairs?(_), do: true

  @doc """
  Solve part 2
  """
  def part2(input) do
    input
    |> Enum.filter(fn s -> repeated_pair?(s) && split_pair?(s) end)
    |> Enum.count()
  end

  @doc """
  Check if char list contains a repeated, non-overlapping pair of characters

  ## Examples:

      iex> repeated_pair?('aaa')
      false

      iex> repeated_pair?('elinhjelle')
      true

      iex> repeated_pair?('geirarne')
      false
  """
  def repeated_pair?(string) do
    case string do
      [c1, c2 | tail] -> repeated_pair?(tail, [c1, c2]) || repeated_pair?([c2 | tail])
      _ -> false
    end
  end

  def repeated_pair?(string, [c1, c2]) do
    case string do
      [t1, t2 | tail] -> (t1 == c1 and t2 == c2) || repeated_pair?([t2 | tail], [c1, c2])
      _ -> false
    end
  end

  @doc """
  Check if char list has a pair of equal characters with exactly one character in between

  Examples:

      iex> split_pair?('aaa')
      true

      iex> split_pair?('geirarne')
      true

      iex> split_pair?('elinhjelle')
      false
  """
  def split_pair?([char, _, char | _]), do: true
  def split_pair?([_ | tail]), do: split_pair?(tail)
  def split_pair?(_), do: false

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
