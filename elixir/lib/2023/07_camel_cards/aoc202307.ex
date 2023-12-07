defmodule AOC2023.Day07 do
  @moduledoc """
  Advent of Code 2023, day 7: Camel Cards.
  """
  require AOC

  @doc """
  Parse input.
  """
  def parse(puzzle_input) do
    puzzle_input
    |> String.split("\n", trim: true)
    |> Enum.map(&String.split/1)
    |> Enum.map(fn [cards, bid] -> {String.to_charlist(cards), String.to_integer(bid)} end)
  end

  @doc """
  Solve part 1.
  """
  def part1(data) do
    data
    |> Enum.map(fn {cards, bid} ->
      {rank_hand(cards, &find_hand_type/1, ~c"23456789TJQKA"), bid}
    end)
    |> Enum.sort()
    |> Enum.with_index(1)
    |> Enum.map(fn {{_, bid}, rank} -> bid * rank end)
    |> Enum.sum()
  end

  @doc """
  Solve part 2.
  """
  def part2(data) do
    data
    |> Enum.map(fn {cards, bid} ->
      {rank_hand(cards, &find_hand_type_w_joker/1, ~c"J23456789TQKA"), bid}
    end)
    |> Enum.sort()
    |> Enum.with_index(1)
    |> Enum.map(fn {{_, bid}, rank} -> bid * rank end)
    |> Enum.sum()
  end

  @doc """
  Rank a poker hand.

  First, rank it based on hand type (five of a kind, four of a kind, etc.), then
  rank individual cards.

  ## Examples:

      iex> rank_hand(~c"32T3K")
      [2, 1, 0, 8, 1, 11]
      iex> rank_hand(~c"T55J5")
      [4, 8, 3, 3, 9, 3]
  """
  def rank_hand(cards, hand_type \\ &find_hand_type/1, order \\ ~c"23456789TJQKA") do
    [hand_type.(cards) | cards |> Enum.map(fn card -> Enum.find_index(order, &(&1 == card)) end)]
  end

  @doc """
  Find the hand type of the cards.

  Returns a number that can be used to rank based on hand type.

  ## Examples:

      iex> find_hand_type(~c"32T3K")
      2
      iex> find_hand_type(~c"T55J5")
      4
  """
  def find_hand_type(cards) do
    num_cards = cards |> Enum.frequencies() |> Map.values() |> Enum.sort()

    case num_cards do
      [1, 1, 1, 1, 1] -> 1
      [1, 1, 1, 2] -> 2
      [1, 2, 2] -> 3
      [1, 1, 3] -> 4
      [2, 3] -> 5
      [1, 4] -> 6
      [5] -> 7
    end
  end

  @doc """
  Find the hand type of the cards, taking jokers into account.

  Returns a number that can be used to rank based on hand type.

  ## Examples:

      iex> find_hand_type_w_joker(~c"32T3K")
      2
      iex> find_hand_type_w_joker(~c"T55J5")
      6
      iex> find_hand_type_w_joker(~c"JJJJJ")
      7
  """
  def find_hand_type_w_joker(cards) do
    {best_card, _} =
      cards |> Enum.frequencies() |> Map.put(?J, 0) |> Enum.max_by(fn {_key, value} -> value end)

    find_hand_type(
      Enum.map(cards, fn
        ?J -> best_card
        card -> card
      end)
    )
  end

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
