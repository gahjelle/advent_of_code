defmodule AOC2021.Day06 do
  @moduledoc """
  Advent of Code 2021, day 6: Lanternfish
  """
  require AOC

  @doc """
  Parse input
  """
  def parse(puzzle_input) do
    puzzle_input |> String.split(",") |> Enum.map(&String.to_integer/1)
  end

  @doc """
  Solve part 1
  """
  def part1(input), do: input |> count_lanternfish(80)

  @doc """
  Solve part 2
  """
  def part2(input), do: input |> count_lanternfish(256)

  @doc """
  Count all lanternfish at the end of the given day based on the starting timers

  ## Example:

      iex> count_lanternfish([3, 4, 3, 1, 2], 18)
      26
  """
  def count_lanternfish(starting_timers, days) do
    counts = 0..days |> Enum.reduce(%{}, fn day, acc -> lanternfish(day, acc) end)
    starting_timers |> Enum.map(&counts[days - &1]) |> Enum.sum()
  end

  @doc """
  Count the number of lanternfish created by one lanternfish in the given number of days

  ## Examples:

      iex> lanternfish(0)[0]
      1

      iex> lanternfish(1)[1]
      2

      iex> lanternfish(16)[16]
      5

      iex> lanternfish(17)[17]
      7
  """
  def lanternfish(num_days), do: lanternfish(num_days, %{})

  def lanternfish(num_days, counts) do
    cond do
      Map.has_key?(counts, num_days) ->
        counts

      num_days < 1 ->
        Map.put(counts, num_days, 1)

      true ->
        until_now =
          Map.merge(lanternfish(num_days - 7, counts), lanternfish(num_days - 9, counts))

        Map.put(until_now, num_days, until_now[num_days - 7] + until_now[num_days - 9])
    end
  end

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
