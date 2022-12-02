defmodule AOC2022.Day02 do
  @moduledoc """
  Advent of Code 2022, day 2: Rock Paper Scissors.
  """
  require AOC

  @doc """
  Parse input.
  """
  def parse(puzzle_input),
    do: puzzle_input |> String.split("\n", trim: true) |> Enum.map(&parse_strategy/1)

  @doc """
  Parse one strategy.

  ## Examples:

      iex> parse_strategy("A Z")
      {:rock, :scissors, ?Z}
      iex> parse_strategy("B Y")
      {:paper, :paper, ?Y}
  """
  def parse_strategy(<<first, " ", second>>),
    do: {letter_to_rps(first, 'ABC'), letter_to_rps(second, 'XYZ'), second}

  @doc """
  Convert a letter to a rock, paper, scissors move.

  ## Examples:

      iex> letter_to_rps(?B, 'ABC')
      :paper
      iex> letter_to_rps(?Z, 'ZXY')
      :rock
  """
  def letter_to_rps(letter, letters) do
    letters
    |> Enum.zip([:rock, :paper, :scissors])
    |> Enum.find(fn {lt, _} -> lt == letter end)
    |> elem(1)
  end

  @doc """
  Solve part 1.
  """
  def part1(rounds) do
    rounds
    |> Enum.map(fn {other, self, _} -> score({self, other}) end)
    |> Enum.sum()
  end

  @doc """
  Solve part 2.
  """
  def part2(rounds) do
    rounds
    |> Enum.map(fn {other, _, choice} -> choose(choice, other) end)
    |> Enum.map(&score/1)
    |> Enum.sum()
  end

  @doc """
  Score one round.

  The score for a single round is the score for the shape you selected (1 for
  Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the
  round (0 if you lost, 3 if the round was a draw, and 6 if you won).

  ## Example:

      iex> score({:paper, :scissors})
      2
  """
  def score({:rock, :rock}), do: 1 + 3
  def score({:rock, :paper}), do: 1 + 0
  def score({:rock, :scissors}), do: 1 + 6
  def score({:paper, :rock}), do: 2 + 6
  def score({:paper, :paper}), do: 2 + 3
  def score({:paper, :scissors}), do: 2 + 0
  def score({:scissors, :rock}), do: 3 + 0
  def score({:scissors, :paper}), do: 3 + 6
  def score({:scissors, :scissors}), do: 3 + 3

  @doc """
  Choose strategy.

  X means you need to lose, Y means you need to end the round in a draw, and Z
  means you need to win.

  ## Examples:

      iex> choose(?X, :paper)
      {:rock, :paper}
      iex> choose(?Y, :scissors)
      {:scissors, :scissors}
  """
  def choose(?X, :rock), do: {:scissors, :rock}
  def choose(?Y, :rock), do: {:rock, :rock}
  def choose(?Z, :rock), do: {:paper, :rock}
  def choose(?X, :paper), do: {:rock, :paper}
  def choose(?Y, :paper), do: {:paper, :paper}
  def choose(?Z, :paper), do: {:scissors, :paper}
  def choose(?X, :scissors), do: {:paper, :scissors}
  def choose(?Y, :scissors), do: {:scissors, :scissors}
  def choose(?Z, :scissors), do: {:rock, :scissors}

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
