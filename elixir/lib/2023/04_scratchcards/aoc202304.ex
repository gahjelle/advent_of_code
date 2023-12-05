defmodule AOC2023.Day04 do
  @moduledoc """
  Advent of Code 2023, day 4: Scratchcards.
  """
  require AOC

  @doc """
  Parse input.
  """
  def parse(puzzle_input) do
    puzzle_input
    |> String.split("\n")
    |> Enum.map(fn line ->
      line
      |> String.split(":")
      |> Enum.at(1)
      |> String.split("|")
      |> Enum.map(fn tickets -> tickets |> String.split() |> MapSet.new() end)
      |> then(fn [win, own] -> MapSet.intersection(win, own) end)
      |> MapSet.size()
    end)
  end

  @doc """
  Solve part 1.
  """
  def part1(data) do
    data
    |> Enum.filter(&(&1 > 0))
    |> Enum.map(&(2 ** (&1 - 1)))
    |> Enum.sum()
  end

  @doc """
  Solve part 2.
  """
  def part2(data) do
    data
    |> Enum.with_index(1)
    |> Enum.filter(fn {win, _} -> win > 0 end)
    |> Enum.reduce(
      1..length(data) |> Enum.map(fn idx -> {idx, 1} end) |> Enum.into(%{}),
      fn {win, id}, counts ->
        (id + 1)..(id + win)
        |> Enum.reduce(counts, &win_new_scratchcards(&1, &2, Map.get(counts, id)))
      end
    )
    |> Map.values()
    |> Enum.sum()
  end

  @doc """
  Update the list of scratchcards with new copies.

  ## Example:

      iex> win_new_scratchcards(3, %{1 => 1, 2 => 2, 3 => 4, 4 => 7, 5 => 1}, 5)
      %{1 => 1, 2 => 2, 3 => 9, 4 => 7, 5 => 1}
  """
  def win_new_scratchcards(id, counts, copies) do
    Map.update(counts, id, nil, fn count -> count + copies end)
  end

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
