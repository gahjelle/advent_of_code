defmodule AOC2018.Day02 do
  @moduledoc """
  Advent of Code 2018, day 2: Inventory Management System

  With apologies and thanks: https://www.twitch.tv/videos/346878818
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
  def part1(input) do
    input
    |> count_twos_and_threes()
    |> then(fn {twos, threes} -> twos * threes end)
  end

  @doc """
  Count the number of each character in a char list

  ## Example:

      iex> count_characters('abcaba')
      %{?a => 3, ?b => 2, ?c => 1}
  """
  def count_characters(box_id), do: count_characters(box_id, %{})
  def count_characters([], count_acc), do: count_acc

  def count_characters([char | rest], count_acc) do
    count_characters(rest, Map.update(count_acc, char, 1, &(&1 + 1)))
  end

  @doc """
  Separately check if there are any characters occuring twice or three times

  ## Example:

      iex> any_twos_and_threes(%{?a => 4, ?b => 2, ?c => 1})
      {1, 0}
  """
  def any_twos_and_threes(counts) do
    counts
    |> Enum.reduce({0, 0}, fn
      {_char, 2}, {_twos, threes} -> {1, threes}
      {_char, 3}, {twos, _threes} -> {twos, 1}
      _, acc -> acc
    end)
  end

  @doc """
  Count how many box ids has characters repeated twice and three times

  ## Examples:

      iex> count_twos_and_threes(['ab', 'aabb', 'aabbb'])
      {2, 1}
  """
  def count_twos_and_threes(box_ids) do
    box_ids
    |> Enum.reduce({0, 0}, fn box_id, {twos_acc, threes_acc} ->
      {twos, threes} =
        box_id
        |> count_characters()
        |> any_twos_and_threes()

      {twos_acc + twos, threes_acc + threes}
    end)
  end

  @doc """
  Solve part 2
  """
  def part2(input) do
    input |> find_similar() |> List.to_string()
  end

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
