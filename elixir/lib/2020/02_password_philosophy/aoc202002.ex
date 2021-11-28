defmodule AOC2020.Day02 do
  @moduledoc """
  Advent of Code 2020, day 2: Password Philosophy
  """
  require AOC
  import NimbleParsec

  @doc """
  Parse input
  """
  def parse(puzzle_input) do
    puzzle_input
    |> String.split("\n")
    |> Enum.map(fn s ->
      {:ok, [one, two, char, password], "", %{}, _, _} = policy(s)
      {one, two, char, password |> String.to_charlist()}
    end)
  end

  @doc """
  Parse one policy

  ## Examples:

      iex> policy("2-11 g: adventofcode")
      {:ok, [2, 11, ?g, "adventofcode"], "", %{}, {1, 0}, 20}

      iex> policy("not a policy")
      {:error, "expected ASCII character in the range '0' to '9'", "not a policy", %{}, {1, 0}, 0}
  """
  defparsec(
    :policy,
    integer(min: 1)
    |> ignore(string("-"))
    |> integer(min: 1)
    |> ignore(string(" "))
    |> ascii_char([?a..?z])
    |> ignore(string(": "))
    |> ascii_string([?a..?z], min: 1)
  )

  @doc """
  Solve part 1
  """
  def part1(input) do
    input |> Enum.filter(&valid_count?/1) |> Enum.count()
  end

  @doc """
  Check if a policy specifies the correct count for a character

  ## Examples:

      iex> valid_count?({1, 2, ?a, 'abba'})
      true

      iex> valid_count?({3, 4, ?b, 'abba'})
      false
  """
  def valid_count?({min, max, char, password}) do
    (password |> Enum.count(fn c -> c == char end)) in min..max
  end

  @doc """
  Solve part 2
  """
  def part2(input) do
    input |> Enum.filter(&valid_position?/1) |> Enum.count()
  end

  @doc """
  Check if a policy specifies exactly one valid position for a character

  ## Examples:

      iex> valid_position?({1, 2, ?a, 'abba'})
      true

      iex> valid_position?({2, 3, ?b, 'abba'})
      false
  """
  def valid_position?({pos_1, pos_2, char, password}) do
    [first, second | _] = password |> Enum.drop(pos_1 - 1) |> Enum.take_every(pos_2 - pos_1)
    first != second && (first == char || second == char)
  end

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
