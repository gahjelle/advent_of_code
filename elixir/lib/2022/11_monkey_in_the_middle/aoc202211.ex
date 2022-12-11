defmodule AOC2022.Day11 do
  @moduledoc """
  Advent of Code 2022, day 11: Monkey in the Middle.
  """
  alias AOC2022.Day11.Monkey
  require AOC

  @doc """
  Parse input.
  """
  def parse(puzzle_input) do
    monkeys =
      puzzle_input
      |> String.split("\n\n", trim: true)
      |> Enum.with_index()
      |> Enum.map(fn {info, idx} -> {idx, Monkey.from_string(info)} end)
      |> Enum.into(%{})

    items =
      puzzle_input
      |> String.split("\n\n", trim: true)
      |> Enum.with_index()
      |> Enum.map(fn {info, idx} -> {idx, Monkey.items_from_string(info)} end)
      |> Enum.into(%{})

    {monkeys, items}
  end

  @doc """
  Solve part 1.
  """
  def part1(data), do: chase_monkeys(data, 20, 3)

  @doc """
  Solve part 2.
  """
  def part2(data), do: chase_monkeys(data, 10_000, 1)

  @doc """
  Chase the monkeys for a given number of rounds and with control on your worry
  level.

  We calculate levels modulo the product of the divisibility tests to keep
  levels manageable.

  ## Example:

      iex> monkeys = %{
      ...>   0 => Monkey.new(id: 0, operation: {:add, 4}, test: 11, to_true: 1, to_false: 2),
      ...>   1 => Monkey.new(id: 1, operation: {:mul, 3}, test: 7, to_true: 2, to_false: 0),
      ...>   2 => Monkey.new(id: 2, operation: {:pow, 2}, test: 13, to_true: 0, to_false: 1)
      ...> }
      iex> items = %{0 => [4, 1, 8], 1 => [], 2 => [0, 6]}
      iex> chase_monkeys({monkeys, items}, 3, 2)
      80
  """
  def chase_monkeys({monkeys, items}, rounds, control) do
    mod = monkeys |> Map.values() |> Enum.map(& &1.test) |> Enum.product()

    1..rounds
    |> Enum.reduce({monkeys, items}, fn _, {monkeys, items} ->
      Monkey.chase(monkeys, items, {control, mod})
    end)
    |> elem(0)
    |> Map.values()
    |> Enum.sort(fn monkey_1, monkey_2 -> monkey_1.count >= monkey_2.count end)
    |> then(fn [monkey_1, monkey_2 | _] -> monkey_1.count * monkey_2.count end)
  end

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end

defmodule AOC2022.Day11.Monkey do
  @moduledoc """
  Structure for representing monkeys.
  """
  defstruct operation: {:mul, 1}, test: 1, to_true: 0, to_false: 0, count: 0

  @doc """
  Create a Monkey from keyword arguments.

  ## Example:

      iex> new(operation: {:mul, 3}, test: 7, to_true: 2, to_false: 19)
      %Monkey{operation: {:mul, 3}, test: 7, to_true: 2, to_false: 19, count: 0}
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
      %Monkey{operation: {:add, 2}, test: 3, to_true: 6, to_false: 7}
  """
  def from_string(info) do
    info
    |> String.split("\n", trim: true)
    |> Enum.flat_map(&parse_line/1)
    |> then(fn monkey -> new(monkey) end)
  end

  @doc """
  List starting items from a text description.

  ## Example:

      iex> info = ~s(
      ...>Monkey 3:
      ...>  Starting items: 84, 93, 70
      ...>  Operation: new = old + 2
      ...>  Test: divisible by 3
      ...>    If true: throw to monkey 6
      ...>    If false: throw to monkey 7
      ...>)
      iex> items_from_string(info)
      [84, 93, 70]
  """
  def items_from_string(info) do
    info |> String.split("\n", trim: true) |> Enum.flat_map(&parse_item/1)
  end

  @doc """
  Chase all monkeys.

  ## Example:

      iex> monkeys = %{
      ...>   0 => Monkey.new(operation: {:add, 4}, test: 11, to_true: 1, to_false: 2),
      ...>   1 => Monkey.new(operation: {:mul, 3}, test: 7, to_true: 2, to_false: 0),
      ...>   2 => Monkey.new(operation: {:pow, 2}, test: 13, to_true: 0, to_false: 1)
      ...> }
      iex> items = %{0 => [4, 1], 1 => [8], 2 => [0, 6]}
      iex> chase(monkeys, items, {2, 11 * 7 * 13})
      {
        %{
          0 => Monkey.new(operation: {:add, 4}, test: 11, to_true: 1, to_false: 2, count: 2),
          1 => Monkey.new(operation: {:mul, 3}, test: 7, to_true: 2, to_false: 0, count: 1),
          2 => Monkey.new(operation: {:pow, 2}, test: 13, to_true: 0, to_false: 1, count: 4)
        },
        %{0 => [12, 0], 1 => [18, 8, 2], 2 => []}
      }
  """
  def chase(monkeys, items, {control, mod}) do
    monkeys
    |> Map.keys()
    |> Enum.reduce({monkeys, items}, fn monkey_id, {monkeys, items} ->
      for item <- items[monkey_id], reduce: {monkeys, items} do
        {monkeys, items} ->
          monkeys = Map.update!(monkeys, monkey_id, &count/1)
          items = items |> inspect(monkeys, monkey_id, item, control, mod)
          {monkeys, items}
      end
    end)
  end

  @doc """
  Count one comparison for one monkey.

  ## Example:

      iex> count(Monkey.new(count: 4)).count
      5
  """
  def count(monkey), do: Map.update!(monkey, :count, &(&1 + 1))

  @doc """
  Have a monkey inspect one item.

  ## Example:

      iex> monkeys = %{1 => Monkey.new(operation: {:mul, 3}, test: 7, to_true: 2, to_false: 0)}
      iex> items = %{0 => [4, 1], 1 => [8], 2 => [0, 6]}
      iex> inspect(items, monkeys, 1, 8, 2, 1001)
      %{0 => [4, 1, 12], 1 => [], 2 => [0, 6]}
  """
  def inspect(items, monkeys, monkey_id, item, control, mod) do
    monkey = monkeys[monkey_id]
    new_item = item |> operate(monkey.operation) |> div(control) |> rem(mod)
    new_monkey = if rem(new_item, monkey.test) == 0, do: monkey.to_true, else: monkey.to_false

    items
    |> Map.update!(monkey_id, &Enum.reject(&1, fn i -> i == item end))
    |> Map.update!(new_monkey, fn levels -> levels ++ [new_item] end)
  end

  @doc """
  Perform monkey operations.

  ## Examples:

      iex> operate(4, {:add, 3})
      7
      iex> operate(19, {:mul, 5})
      95
      iex> operate(7, {:pow, 2})
      49
  """
  def operate(number, {:add, addend}), do: number + addend
  def operate(number, {:mul, factor}), do: number * factor
  def operate(number, {:pow, exponent}), do: number ** exponent

  defp parse_line(<<"  Operation: new = old * old">>),
    do: [operation: {:pow, 2}]

  defp parse_line(<<"  Operation: new = old + " <> number::binary>>),
    do: [operation: {:add, number |> String.to_integer()}]

  defp parse_line(<<"  Operation: new = old * " <> number::binary>>),
    do: [operation: {:mul, number |> String.to_integer()}]

  defp parse_line(<<"  Test: divisible by " <> number::binary>>),
    do: [test: String.to_integer(number)]

  defp parse_line(<<"    If true: throw to monkey " <> number::binary>>),
    do: [to_true: String.to_integer(number)]

  defp parse_line(<<"    If false: throw to monkey " <> number::binary>>),
    do: [to_false: String.to_integer(number)]

  defp parse_line(_), do: []

  defp parse_item(<<"  Starting items: " <> items::binary>>) do
    items |> String.split(", ", trim: true) |> Enum.map(&String.to_integer/1)
  end

  defp parse_item(_), do: []
end
