defmodule AOC2022.Day10 do
  @moduledoc """
  Advent of Code 2022, day 10: Cathode-Ray Tube.
  """
  require AOC

  @doc """
  Parse input.
  """
  def parse(puzzle_input) do
    puzzle_input
    |> String.split("\n", trim: true)
    |> Enum.flat_map(&parse_line/1)
    # Adjust for everything happening at the end of cycles
    |> then(fn nums -> [0 | nums] |> Enum.reverse() |> tl() |> Enum.reverse() end)
    |> Enum.scan(1, &(&1 + &2))
  end

  @doc """
  Parse one line of input.

  ## Examples:

      iex> parse_line("noop")
      [0]
      iex> parse_line("addx 4")
      [0, 4]
      iex> parse_line("addx -11")
      [0, -11]
  """
  def parse_line("noop"), do: [0]
  def parse_line(<<"addx ", number::binary>>), do: [0, String.to_integer(number)]

  @doc """
  Solve part 1.
  """
  def part1(registers) do
    registers
    |> Enum.with_index(1)
    |> Enum.slice(19..-1//40)
    |> Enum.map(fn {reg, idx} -> reg * idx end)
    |> Enum.sum()
  end

  @doc """
  Solve part 2.
  """
  def part2(registers) do
    registers
    |> Enum.with_index()
    |> Enum.map(fn {reg, idx} -> abs(reg - rem(idx, 40)) <= 1 end)
    |> Enum.map(fn lit -> if lit, do: '█', else: ' ' end)
    |> Enum.chunk_every(40)
    |> Enum.map_join("\n", &List.to_string/1)
  end

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
