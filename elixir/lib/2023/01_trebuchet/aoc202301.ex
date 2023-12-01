defmodule AOC2023.Day01 do
  @moduledoc """
  Advent of Code 2023, day 1: Trebuchet?!.
  """
  require AOC

  @doc """
  Parse input.
  """
  def parse(puzzle_input), do: puzzle_input |> String.split("\n", trim: true)

  @doc """
  Solve part 1.
  """
  def part1(lines) do
    lines
    |> Enum.map(fn line ->
      line
      |> String.replace(~r/[^0-9]/, "")
      |> then(fn number -> String.at(number, 0) <> String.at(number, -1) end)
      |> String.to_integer()
    end)
    |> Enum.sum()
  end

  @doc """
  Solve part 2.
  """
  def part2(lines) do
    lines
    |> Enum.map(fn line ->
      find_first_digit(line) * 10 + find_last_digit(line)
    end)
    |> Enum.sum()
  end

  @doc """
  Find first digit in a text. Textual or numeric.

  ## Examples:

      iex> find_first_digit("one2three")
      1
      iex> find_first_digit("abcthree4")
      3
      iex> find_first_digit("eigh7")
      7
  """
  def find_first_digit(text) do
    case text do
      "one" <> _rest -> 1
      "two" <> _rest -> 2
      "three" <> _rest -> 3
      "four" <> _rest -> 4
      "five" <> _rest -> 5
      "six" <> _rest -> 6
      "seven" <> _rest -> 7
      "eight" <> _rest -> 8
      "nine" <> _rest -> 9
      <<char::utf8>> <> _rest when char >= ?1 and char <= ?9 -> char - ?0
      <<_char::utf8>> <> rest -> find_first_digit(rest)
    end
  end

  @doc """
  Find last digit in a text. Textual or numeric.

  ## Examples:

      iex> find_last_digit("one2three")
      3
      iex> find_last_digit("abcthree4")
      4
      iex> find_last_digit("eigh7")
      7
      iex> find_last_digit("eightwo")
      2
  """
  def find_last_digit(text) do
    case String.reverse(text) do
      "eno" <> _rest -> 1
      "owt" <> _rest -> 2
      "eerht" <> _rest -> 3
      "ruof" <> _rest -> 4
      "evif" <> _rest -> 5
      "xis" <> _rest -> 6
      "neves" <> _rest -> 7
      "thgie" <> _rest -> 8
      "enin" <> _rest -> 9
      <<char::utf8>> <> _rest when char >= ?1 and char <= ?9 -> char - ?0
      <<_char::utf8>> <> rest -> find_last_digit(String.reverse(rest))
    end
  end

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
