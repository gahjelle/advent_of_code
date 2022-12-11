defmodule AOC2022.Day11 do
  @moduledoc """
  Advent of Code 2022, day 11: Monkey in the Middle.
  """
  alias AOC2022.Day11.Monkeys
  require AOC

  @doc """
  Parse input.
  """
  def parse(puzzle_input), do: Monkeys.from_string(puzzle_input)

  @doc """
  Solve part 1.
  """
  def part1(monkeys), do: chase_monkeys(monkeys, 20, 3)

  @doc """
  Solve part 2.
  """
  def part2(monkeys), do: chase_monkeys(monkeys, 10_000, 1)

  @doc """
  Chase the monkeys for a number of rounds controlling the worry level.

  Count the total number of times each monkey inspects items and find the two
  most active monkeys. The level of monkey business is the product of the number
  of inspections of the two most active monkeys.

  ## Example:

      iex> monkeys = %{
      ...>   0 => Monkey.new(items: [4, 1, 8], op: {:add, 4}, test: 11, to_true: 1, to_false: 2),
      ...>   1 => Monkey.new(items: [], op: {:mul, 3}, test: 7, to_true: 2, to_false: 0),
      ...>   2 => Monkey.new(items: [0, 6], op: {:pow2}, test: 13, to_true: 0, to_false: 1)
      ...> }
      iex> chase_monkeys(monkeys, 3, 2)
      8 * 10
  """
  def chase_monkeys(monkeys, rounds, control) do
    monkeys
    |> Monkeys.chase(rounds, control)
    |> Enum.map(fn {_, monkey} -> monkey.count end)
    |> Enum.sort(:desc)
    |> Enum.take(2)
    |> Enum.product()
  end

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end

defmodule AOC2022.Day11.Monkeys do
  @moduledoc """
  Several monkeys are represented as a Map with monkey_id => monkey items.
  """
  alias AOC2022.Day11.Monkey

  @doc """
  Construct Monkeys from string information.

  ## Example:

      iex> lines = ~s(
      ...>Monkey 0:
      ...>  Starting items: 56
      ...>  Operation: new = old + 1
      ...>  Test: divisible by 7
      ...>    If true: throw to monkey 4
      ...>    If false: throw to monkey 2
      ...>
      ...>Monkey 1:
      ...>  Starting items: 68, 72
      ...>  Operation: new = old * 8
      ...>  Test: divisible by 19
      ...>    If true: throw to monkey 3
      ...>    If false: throw to monkey 0
      ...>)
      iex> from_string(lines)
      %{
        0 => Monkey.new(items: [56], op: {:add, 1}, test: 7, to_true: 4, to_false: 2),
        1 => Monkey.new(items: [68, 72], op: {:mul, 8}, test: 19, to_true: 3, to_false: 0)
      }
  """
  def from_string(lines) do
    lines
    |> String.split("\n\n", trim: true)
    |> Enum.map(&Monkey.from_string/1)
    |> Enum.with_index()
    |> Enum.into(%{}, &{elem(&1, 1), elem(&1, 0)})
  end

  @doc """
  Chase the monkeys for a given number of rounds and with control on your worry
  level.

  We calculate levels modulo the product of the divisibility tests to keep
  levels manageable.

  ## Example:

      iex> monkeys = %{
      ...>   0 => Monkey.new(items: [4, 1, 8], op: {:add, 4}, test: 11, to_true: 1, to_false: 2),
      ...>   1 => Monkey.new(items: [], op: {:mul, 3}, test: 7, to_true: 2, to_false: 0),
      ...>   2 => Monkey.new(items: [0, 6], op: {:pow2}, test: 13, to_true: 0, to_false: 1)
      ...> }
      iex> chase(monkeys, 3, 2)
      %{
        0 => %AOC2022.Day11.Monkey{items: [3], op: {:add, 4}, test: 11, to_true: 1, to_false: 2, count: 8},
        1 => %AOC2022.Day11.Monkey{items: [112, 32, 4, 112], op: {:mul, 3}, test: 7, to_true: 2, to_false: 0, count: 5},
        2 => %AOC2022.Day11.Monkey{items: [], op: {:pow2}, test: 13, to_true: 0, to_false: 1, count: 10}
      }
  """
  def chase(monkeys, rounds, control) do
    num_monkeys = map_size(monkeys)
    mod = monkeys |> Map.values() |> Enum.map(& &1.test) |> Enum.product()

    for _ <- 1..rounds,
        monkey_id <- 0..(num_monkeys - 1),
        reduce: monkeys do
      monkeys -> inspect(monkeys, monkey_id, control, mod)
    end
  end

  @doc """
  One monkey inspects their items and passes them to someone else.

  ## Example:

      iex> monkeys = %{
      ...>   0 => Monkey.new(items: [4, 1, 8], op: {:add, 4}, test: 11, to_true: 1, to_false: 2),
      ...>   1 => Monkey.new(items: [], op: {:mul, 3}, test: 7, to_true: 2, to_false: 0),
      ...>   2 => Monkey.new(items: [0, 6], op: {:pow2}, test: 13, to_true: 0, to_false: 1)
      ...> }
      iex> inspect(monkeys, 2, 3, 11 * 7 * 13)
      %{
        0 => Monkey.new(items: [4, 1, 8, 0], op: {:add, 4}, test: 11, to_true: 1, to_false: 2, count: 0),
        1 => Monkey.new(items: [12], op: {:mul, 3}, test: 7, to_true: 2, to_false: 0, count: 0),
        2 => Monkey.new(items: [], op: {:pow2}, test: 13, to_true: 0, to_false: 1, count: 2)
      }
  """
  def inspect(monkeys, monkey_id, control, mod) do
    monkey = monkeys[monkey_id]

    monkey.items
    |> Enum.reduce(monkeys, fn item, monkeys ->
      new_item = item |> Monkey.operate(monkey.op) |> div(control) |> rem(mod)
      to_monkey = if rem(new_item, monkey.test) == 0, do: monkey.to_true, else: monkey.to_false

      monkeys
      |> Map.update!(monkey_id, fn monkey -> Map.update!(monkey, :count, &(&1 + 1)) end)
      |> Map.update!(to_monkey, fn monkey -> Map.update!(monkey, :items, &(&1 ++ [new_item])) end)
    end)
    |> Map.update!(monkey_id, fn monkey -> Map.put(monkey, :items, []) end)
  end
end

defmodule AOC2022.Day11.Monkey do
  @moduledoc """
  Structure for representing one monkey.
  """
  defstruct items: [], op: {:mul, 1}, test: 1, to_true: 0, to_false: 0, count: 0

  @doc """
  Create a Monkey from keyword arguments.

  ## Example:

      iex> new(op: {:mul, 3}, test: 7, to_true: 2, to_false: 19)
      Monkey.new(items: [], op: {:mul, 3}, test: 7, to_true: 2, to_false: 19, count: 0)
  """
  def new(args), do: struct(__MODULE__, Enum.into(args, %{}))

  @doc """
  Create a Monkey from a text description.

  ## Example:

      iex> info = ~s(
      ...>Monkey 3:
      ...>  Starting items: 84, 93, 70
      ...>  Operation: new = old + 2
      ...>  Test: divisible by 3
      ...>    If true: throw to monkey 6
      ...>    If false: throw to monkey 7
      ...>)
      iex> from_string(info)
      Monkey.new(items: [84, 93, 70], op: {:add, 2}, test: 3, to_true: 6, to_false: 7)
  """
  def from_string(info) do
    info
    |> String.split("\n", trim: true)
    |> Enum.flat_map(&parse_line/1)
    |> then(fn monkey -> new(monkey) end)
  end

  @doc """
  Perform monkey operations.

  ## Examples:

      iex> operate(4, {:add, 3})
      7
      iex> operate(19, {:mul, 5})
      95
      iex> operate(7, {:pow2})
      49
  """
  def operate(old, {:add, addend}), do: old + addend
  def operate(old, {:mul, factor}), do: old * factor
  def operate(old, {:pow2}), do: old * old

  @doc """
  Parse one line of monkey information.

  ## Examples:

      iex> parse_line("  Operation: new = old + 71")
      [op: {:add, 71}]
      iex> parse_line("  Starting items: 1, 3, 71, 98443")
      [items: [1, 3, 71, 98443]]
  """
  def parse_line(<<"  Starting items: " <> items::binary>>),
    do: [items: items |> String.split(", ", trim: true) |> Enum.map(&String.to_integer/1)]

  def parse_line(<<"  Operation: new = old * old">>), do: [op: {:pow2}]

  def parse_line(<<"  Operation: new = old + " <> number::binary>>),
    do: [op: {:add, number |> String.to_integer()}]

  def parse_line(<<"  Operation: new = old * " <> number::binary>>),
    do: [op: {:mul, number |> String.to_integer()}]

  def parse_line(<<"  Test: divisible by " <> number::binary>>),
    do: [test: String.to_integer(number)]

  def parse_line(<<"    If true: throw to monkey " <> number::binary>>),
    do: [to_true: String.to_integer(number)]

  def parse_line(<<"    If false: throw to monkey " <> number::binary>>),
    do: [to_false: String.to_integer(number)]

  def parse_line(_), do: []
end
