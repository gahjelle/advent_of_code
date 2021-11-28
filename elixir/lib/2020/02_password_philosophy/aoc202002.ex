defmodule AOC2020.Day02 do
  @moduledoc """
  Advent of Code 2020, day 2: Password Philosophy
  """
  require AOC
  import NimbleParsec

  def parse(puzzle_input) do
    puzzle_input
    |> String.split("\n")
    |> Enum.map(fn s ->
      {:ok, [one, two, char, password], "", %{}, _, _} = policy(s)
      {one, two, char, password |> String.to_charlist()}
    end)
  end

  defparsecp(
    :policy,
    integer(min: 1)
    |> ignore(string("-"))
    |> integer(min: 1)
    |> ignore(string(" "))
    |> ascii_char([?a..?z])
    |> ignore(string(": "))
    |> ascii_string([?a..?z], min: 1)
  )

  def part1(input) do
    input |> Enum.filter(&valid_count?/1) |> Enum.count()
  end

  def valid_count?({min, max, char, password}) do
    (password |> Enum.count(fn c -> c == char end)) in min..max
  end

  def part2(input) do
    input |> Enum.filter(&valid_position?/1) |> Enum.count()
  end

  def valid_position?({pos_1, pos_2, char, password}) do
    [first, second | _] = password |> Enum.drop(pos_1 - 1) |> Enum.take_every(pos_2 - pos_1)
    first != second && (first == char || second == char)
  end

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
