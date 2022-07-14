defmodule AOC2019.Day02 do
  @moduledoc """
  Advent of Code 2019, day 2: 1202 Program Alarm
  """
  require AOC

  @doc """
  Parse input
  """
  def parse(puzzle_input) do
    puzzle_input
    |> String.split(",")
    |> Enum.map(&String.to_integer/1)
    |> Enum.with_index()
    |> Enum.into(%{}, fn {value, idx} -> {idx, value} end)
  end

  @doc """
  Solve part 1
  """
  def part1(input) do
    input |> initialize_intcode_and_run(1202)
  end

  @doc """
  Solve part 2
  """
  def part2(input) do
    {moon_landing, ""} = "1969_07_20" |> String.replace("_", "") |> Integer.parse()
    input |> test_program(0, moon_landing)
  end

  @doc """
  Run the intcode computer on different inputs until target output is found

    ## Examples:

        iex> test_program(%{0 => 1, 1 => 0, 2 => 0, 3 => 0, 4 => 99}, 0, 4)
        202
  """
  def test_program(program, noun_and_verb, target) do
    output = initialize_intcode_and_run(program, noun_and_verb)
    if output == target, do: noun_and_verb, else: test_program(program, noun_and_verb + 1, target)
  end

  @doc """
  Initialize the intcode computer with the given noun and verb and run it

    ## Examples:

        iex> initialize_intcode_and_run(%{0 => 1, 1 => 0, 2 => 0, 3 => 0, 4 => 99}, 202)
        4
        iex> initialize_intcode_and_run(%{0 => 1, 1 => 0, 2 => 0, 3 => 0, 4 => 99}, 2, 2)
        4
  """
  def initialize_intcode_and_run(program, noun_and_verb) do
    initialize_intcode_and_run(program, div(noun_and_verb, 100), rem(noun_and_verb, 100))
  end

  def initialize_intcode_and_run(program, noun, verb) do
    program |> Map.merge(%{1 => noun, 2 => verb}) |> run_intcode(0)
  end

  @doc """
  Run the intcode computer

  ## Examples:

      iex> run_intcode(%{0 => 1, 1 => 0, 2 => 0, 3 => 0, 4 => 99})
      2
      iex> run_intcode(%{0 => 2, 1 => 0, 2 => 0, 3 => 0, 4 => 99})
      4
  """
  def run_intcode(program), do: run_intcode(program, 0)

  def run_intcode(program, pointer) do
    opcode = program[pointer]

    if opcode == 99,
      do: program |> Map.get(0),
      else: execute_opcode(program, opcode, pointer) |> run_intcode(pointer + 4)
  end

  @doc """
  Execute one opcode

  ## Examples:

      iex> execute_opcode(%{0 => 1, 1 => 0, 2 => 0, 3 => 0, 4 => 99}, 1, 0)
      %{0 => 2, 1 => 0, 2 => 0, 3 => 0, 4 => 99}
      iex> execute_opcode(%{0 => 2, 1 => 0, 2 => 0, 3 => 0, 4 => 99}, 2, 0)
      %{0 => 4, 1 => 0, 2 => 0, 3 => 0, 4 => 99}
  """
  def execute_opcode(program, 1, pointer) do
    {pos_1, pos_2, new_pos} = {program[pointer + 1], program[pointer + 2], program[pointer + 3]}
    Map.put(program, new_pos, Map.get(program, pos_1, 0) + Map.get(program, pos_2, 0))
  end

  def execute_opcode(program, 2, pointer) do
    {pos_1, pos_2, new_pos} = {program[pointer + 1], program[pointer + 2], program[pointer + 3]}
    Map.put(program, new_pos, Map.get(program, pos_1, 0) * Map.get(program, pos_2, 0))
  end

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
