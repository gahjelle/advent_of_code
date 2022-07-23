defmodule AOC2018.Day05 do
  @moduledoc """
  Advent of Code 2018, day 5: Alchemical Reduction
  """
  require AOC

  @doc """
  Parse input
  """
  def parse(puzzle_input), do: puzzle_input |> String.to_charlist()

  @doc """
  Solve part 1
  """
  def part1(input), do: input |> react() |> length()

  @doc """
  Solve part 2, with concurrency
  """
  def part2(input) do
    ?a..?z
    |> Task.async_stream(fn type -> input |> remove(type) |> react() |> length() end)
    |> Stream.map(fn {:ok, result} -> result end)
    |> Enum.min()
  end

  @doc """
  React a polymer

  ## Examples:

      iex> react('aBbA')
      ''

      iex> react('aabBCC')
      'aaCC'

      iex> react('aAbbCCDd')
      'bbCC'
  """
  def react(polymer), do: react(polymer, [])
  def react([head | rest], []), do: react(rest, [head])
  def react([], acc), do: acc |> Enum.reverse()
  def react([head | rest], [prev | acc]) when abs(head - prev) == 32, do: react(rest, acc)
  def react([head | rest], acc), do: react(rest, [head | acc])

  @doc """
  Remove all units of the given type from a polymer

  ## Examples:

      iex> remove('abBA', ?a)
      'bB'

      iex> remove('abBA', ?B)
      'aA'

      iex> remove('abBA', ?c)
      'abBA'

      iex> remove('aaAa', ?a)
      ''
  """
  def remove(polymer, type), do: Enum.reject(polymer, fn char -> rem(char - type, 32) == 0 end)

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
