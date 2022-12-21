defmodule AOC2022.Day21 do
  @moduledoc """
  Advent of Code 2022, day 21: Monkey Math.
  """
  require AOC

  @doc """
  Parse input.
  """
  def parse(puzzle_input) do
    puzzle_input
    |> String.split("\n", trim: true)
    |> Enum.map(&parse_monkey/1)
    |> Enum.split_with(fn
      {_, {:number, _}} -> true
      _ -> false
    end)
    |> then(fn {nums, ops} ->
      {nums |> Enum.into(%{}, fn {monkey, {:number, number}} -> {monkey, number} end),
       Enum.into(ops, %{})}
    end)
  end

  @doc """
  Parse one monkey.

  ## Examples:

      iex> parse_monkey("aooc: 77")
      {"aooc", {:number, 77}}
      iex> parse_monkey("root: sant * clas")
      {"root", {:mul, {"sant", "clas"}}}
  """
  def parse_monkey(line) do
    case line |> String.split() do
      [monkey, number] -> {String.trim(monkey, ":"), {:number, String.to_integer(number)}}
      [monkey, first, "+", second] -> {String.trim(monkey, ":"), {:add, {first, second}}}
      [monkey, first, "-", second] -> {String.trim(monkey, ":"), {:sub, {first, second}}}
      [monkey, first, "*", second] -> {String.trim(monkey, ":"), {:mul, {first, second}}}
      [monkey, first, "/", second] -> {String.trim(monkey, ":"), {:div, {first, second}}}
    end
  end

  @doc """
  Solve part 1.
  """
  def part1(monkeys), do: monkeys |> monkey_shout("root") |> trunc()

  @doc """
  Solve part 2.
  """
  def part2(monkeys), do: guess_humn_number(monkeys, 0)

  @doc """
  Let monkeys shout numbers until the target number is found.
  """
  def monkey_shout({numbers, monkeys}, target) do
    if Map.has_key?(numbers, target) do
      numbers[target]
    else
      monkeys |> Enum.reduce({numbers, monkeys}, &calculate_one_monkey/2) |> monkey_shout(target)
    end
  end

  @doc """
  Check if one monkey can calculate their number.
  """
  def calculate_one_monkey({monkey, {op, {first, second}}}, {numbers, monkeys}) do
    if Map.has_key?(numbers, first) and Map.has_key?(numbers, second) do
      {Map.put(numbers, monkey, calculate(op, numbers[first], numbers[second])),
       Map.delete(monkeys, monkey)}
    else
      {numbers, monkeys}
    end
  end

  @doc """
  Iteratively guess the human number in a Newton's method kind of fashion.
  """
  def guess_humn_number({numbers, monkeys}, guess) do
    rooted_monkeys = Map.update!(monkeys, "root", fn {_, nums} -> {:equal, nums} end)

    [first, second] =
      guess..(guess + 1)
      |> Enum.map(fn humn ->
        monkey_shout({numbers |> Map.put("humn", humn), rooted_monkeys}, "root")
      end)

    if abs(first) < 1,
      do: guess,
      else: guess_humn_number({numbers, rooted_monkeys}, guess + trunc(first / (first - second)))
  end

  @doc """
  Perform simple arithmetic.

  :equal returns how far the operands are from each other.

  ## Examples:

      iex> calculate(:add, 20, 22)
      42
      iex> calculate(:div, 13, 5)
      2.6
      iex> calculate(:equal, 19, 19)
      0
  """
  def calculate(:add, first, second), do: first + second
  def calculate(:sub, first, second), do: first - second
  def calculate(:mul, first, second), do: first * second
  def calculate(:div, first, second), do: first / second
  def calculate(:equal, first, second), do: second - first

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
