defmodule AOC2015.Day07 do
  @moduledoc """
  Advent of Code 2015, day 7: Some Assembly Required
  """
  require AOC
  import Bitwise

  @doc """
  Parse input
  """
  def parse(puzzle_input) do
    puzzle_input |> String.split("\n") |> Enum.map(&parse_instruction/1)
  end

  @doc """
  Parse one instruction and return a tuple of command, wire, and arguments

  ## Example:

      iex> parse_instruction("p LSHIFT 2 -> q")
      {:lshift, "q", {"p", 2}}
  """
  def parse_instruction(instruction) do
    [command, to_wire] = instruction |> String.split(" -> ")
    parse_command(command |> String.split(), to_wire)
  end

  @doc """
  Parse as number if possible, otherwise return string

  ## Examples:

      iex> value("42")
      42

      iex> value("aoc")
      "aoc"
  """
  def value(value) do
    case Integer.parse(value) do
      {number, ""} -> number
      :error -> value
    end
  end

  defp parse_command([value], to_wire) do
    case Integer.parse(value) do
      {number, ""} -> {:set, to_wire, {number}}
      :error -> {:setfrom, to_wire, {value}}
    end
  end

  defp parse_command([wire_1, "AND", wire_2], to_wire),
    do: {:and, to_wire, {value(wire_1), wire_2}}

  defp parse_command([wire_1, "OR", wire_2], to_wire), do: {:or, to_wire, {value(wire_1), wire_2}}
  defp parse_command(["NOT", wire], to_wire), do: {:not, to_wire, {wire}}

  defp parse_command([wire, "LSHIFT", shift], to_wire),
    do: {:lshift, to_wire, {wire, shift |> String.to_integer()}}

  defp parse_command([wire, "RSHIFT", shift], to_wire),
    do: {:rshift, to_wire, {wire, shift |> String.to_integer()}}

  @doc """
  Solve part 1
  """
  def part1(input) do
    input |> execute_commands() |> Map.get("a")
  end

  @doc """
  Check if all dependencies of a calculation are met

  ## Examples:

      iex> ready?(%{}, "a")
      false

      iex> ready?(%{"a" => 1}, "a")
      true

      iex> ready?(%{"a" => 1}, "a", "b")
      false
  """
  def ready?(state, wire), do: Map.has_key?(state, wire)

  def ready?(state, wire_1, wire_2),
    do: Map.has_key?(state, wire_1) and Map.has_key?(state, wire_2)

  @doc """
  Execute a series of commands and update state. Handle dependencies between commands.

  ## Example:

      x RSHIFT 12 -> y                44 -> ga                     44 -> ga
      NOT ga -> x           --->      NOT ga -> x           --->   NOT 44 = 65491 -> x
      44 -> ga                        x RSHIFT 12 -> y             65491 RSHIFT 12 = 15 -> y
      y AND ga -> a                   y AND ga -> a                15 AND 44 = 12 -> a

      iex> execute_commands([
      ...>   {:rshift, "y", {"x", 12}},
      ...>   {:not, "x", {"ga"}},
      ...>   {:set, "ga", {44}},
      ...>   {:and, "a", {"y", "ga"}}
      ...> ])
      %{"a" => 12, "ga" => 44, "x" => 65491, "y" => 15}
  """
  def execute_commands(commands), do: execute_commands(commands, [], %{})
  def execute_commands([], [], state), do: state
  def execute_commands([], not_ready, state), do: execute_commands(not_ready, [], state)

  def execute_commands([{command, to_wire, args} | commands], not_ready, state) do
    case execute_command({command, args}, state) do
      :notready -> execute_commands(commands, [{command, to_wire, args} | not_ready], state)
      value -> execute_commands(commands, not_ready, Map.put(state, to_wire, value))
    end
  end

  @doc """
  Execute one command, return value or :notready

  ## Examples:

      iex> execute_command({:set, {42}}, %{})
      42

      iex> execute_command({:setfrom, {"a"}}, %{})
      :notready

      iex> execute_command({:setfrom, {"a"}}, %{"a" => 1})
      1

      iex> execute_command({:and, {1, "a"}}, %{"a" => 7})
      1

      iex> execute_command({:and, {"ga", "aoc"}}, %{"ga" => 44, "aoc" => 2015})
      12

      iex> execute_command({:or, {"ga", "aoc"}}, %{"ga" => 44, "aoc" => 2015})
      2047

      iex> execute_command({:not, {"x"}}, %{"x" => 123, "y" => 456})
      65412

      iex> execute_command({:lshift, {"ga", 3}}, %{"ga" => 44})
      352

      iex> execute_command({:rshift, {"ga", 3}}, %{"ga" => 44})
      5
  """
  def execute_command({:set, {number}}, _state), do: number

  def execute_command({:setfrom, {wire}}, state),
    do: if(ready?(state, wire), do: state[wire], else: :notready)

  def execute_command({:and, {wire_1, wire_2}}, state) when is_integer(wire_1),
    do: if(ready?(state, wire_2), do: wire_1 &&& state[wire_2], else: :notready)

  def execute_command({:and, {wire_1, wire_2}}, state) when is_binary(wire_1),
    do: if(ready?(state, wire_1, wire_2), do: state[wire_1] &&& state[wire_2], else: :notready)

  def execute_command({:or, {wire_1, wire_2}}, state),
    do: if(ready?(state, wire_1, wire_2), do: state[wire_1] ||| state[wire_2], else: :notready)

  def execute_command({:not, {wire}}, state),
    # 16 bits, 2¹⁶ = 65,536
    do: if(ready?(state, wire), do: bnot(state[wire]) + 65_536, else: :notready)

  def execute_command({:lshift, {wire, shift}}, state),
    do: if(ready?(state, wire), do: state[wire] <<< shift, else: :notready)

  def execute_command({:rshift, {wire, shift}}, state),
    do: if(ready?(state, wire), do: state[wire] >>> shift, else: :notready)

  @doc """
  Solve part 2
  """
  def part2(input) do
    input |> rewire("b", part1(input)) |> execute_commands() |> Map.get("a")
  end

  @doc """
  Rewire by replacing command with a :set command

  ## Example:

      iex> rewire([{:set, "c", {7}}, {:not, "b", {"c"}}, {:and, "a", {"b", "c"}}], "b", 2015)
      [{:set, "c", {7}}, {:set, "b", {2015}}, {:and, "a", {"b", "c"}}]
  """
  def rewire(commands, wire, value) do
    commands
    |> Enum.map(fn
      {command, to_wire, args} ->
        case to_wire do
          ^wire -> {:set, wire, {value}}
          _ -> {command, to_wire, args}
        end
    end)
  end

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
