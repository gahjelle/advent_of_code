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
  Solve part 2
  """
  def part2(input) do
    ?a..?z
    |> Enum.map(fn type -> input |> remove(type) |> react() |> length() end)
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
  def react([first | polymer], []), do: react(polymer, [first])

  def react([], reacted), do: reacted |> Enum.reverse()

  def react([current | rest], [previous | reacted]) do
    case abs(current - previous) do
      32 -> react(rest, reacted)
      _ -> react(rest, [current, previous | reacted])
    end
  end

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
  def remove(polymer, type) do
    Enum.reject(polymer, fn char -> rem(char - type, 32) == 0 end)
  end

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
