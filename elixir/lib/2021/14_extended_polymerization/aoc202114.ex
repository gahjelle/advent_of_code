defmodule AOC2021.Day14 do
  @moduledoc """
  Advent of Code 2021, day 14: Extended Polymerization
  """
  require AOC

  @doc """
  Parse input
  """
  def parse(puzzle_input) do
    [template, _ | rules] = puzzle_input |> String.split("\n")

    {
      template |> String.first() |> String.to_charlist(),
      template
      |> String.to_charlist()
      |> Enum.chunk_every(2, 1, :discard)
      |> Enum.frequencies(),
      rules |> Enum.map(&parse_rule/1) |> Enum.into(%{})
    }
  end

  @doc """
  Parse one rule

  ## Example:

      iex> parse_rule("CH -> B")
      {'CH', ['CB', 'BH']}

      iex> parse_rule("GG -> G")
      {'GG', ['GG', 'GG']}
  """
  def parse_rule(rule) do
    [[first, second], [insert]] = rule |> String.split(" -> ") |> Enum.map(&String.to_charlist/1)
    {[first, second], [[first, insert], [insert, second]]}
  end

  @doc """
  Solve part 1
  """
  def part1({first, template, rules}) do
    1..10
    |> Enum.reduce(template, fn _, acc -> acc |> step(rules) end)
    |> count_polymers(first)
    |> score_polymer()
  end

  @doc """
  Solve part 2
  """
  def part2({first, template, rules}) do
    1..40
    |> Enum.reduce(template, fn _, acc -> acc |> step(rules) end)
    |> count_polymers(first)
    |> score_polymer()
  end

  @doc """
  Perform one step of polymer insertion

  ## Example:

      iex> step(%{'GA' => 1, 'AH' => 1}, %{
      ...>   'AG' => ['AH', 'HG'],
      ...>   'AH' => ['AG', 'GH'],
      ...>   'GA' => ['GH', 'HA'],
      ...>   'GH' => ['GA', 'AH'],
      ...>   'HA' => ['HG', 'GA'],
      ...>   'HG' => ['HA', 'AG']
      ...> })
      %{'GH' => 2, 'HA' => 1, 'AG' => 1}
  """
  def step(elements, rules) do
    elements
    |> Map.to_list()
    |> Enum.map(fn {pair, count} ->
      [first, second] = rules[pair]
      [{first, count}, {second, count}]
    end)
    |> Enum.flat_map(& &1)
    |> Enum.group_by(fn {pair, _} -> pair end, fn {_, count} -> count end)
    |> Enum.map(fn {pair, counts} -> {pair, counts |> Enum.sum()} end)
    |> Enum.into(%{})
  end

  @doc """
  Count polymers, include first polymer which is not accounted for in the pairs

  ## Example:

      iex> count_polymers(%{'GH' => 2, 'HA' => 1, 'AG' => 1}, 'G')
      [{?A, 1}, {?G, 2}, {?H, 2}]
  """
  def count_polymers(elements, first) do
    elements
    |> Map.to_list()
    |> Enum.concat([{[?0 | first], 1}])
    |> Enum.group_by(fn {[_, second], _} -> second end, fn {_, count} -> count end)
    |> Enum.map(fn {pair, counts} -> {pair, counts |> Enum.sum()} end)
  end

  @doc """
  Score polymer by subtracting the counts of the least common polymer from the most common one

  ## Example:

      iex> score_polymer([{?A, 123}, {?G, 567}, {?H, 345}])
      444
  """
  def score_polymer(counts) do
    {{_, min_count}, {_, max_count}} = counts |> Enum.min_max_by(fn {_, count} -> count end)
    max_count - min_count
  end

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
