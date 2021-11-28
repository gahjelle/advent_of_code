defmodule AOC2015.Day04 do
  @moduledoc """
  Advent of Code 2015, day 4: The Ideal Stocking Stuffer
  """
  require AOC

  @doc """
  Parse input
  """
  def parse(puzzle_input) do
    puzzle_input |> String.split("\n") |> hd()
  end

  def part1(input, prefix \\ "00000") do
    input |> find_md5_with_prefix(prefix)
  end

  def part2(input, prefix \\ "000000") do
    input |> find_md5_with_prefix(prefix)
  end

  @doc """
  Find the first MD5 hash of the form <secret><number> whose hex representation starts with prefix

  ## Examples:

      iex> find_md5_with_prefix("elixir", "A0C")
      2947

      iex> :crypto.hash(:md5, "elixir2947") |> Base.encode16() |> String.slice(0..2)
      "A0C"
  """
  def find_md5_with_prefix(secret, prefix) do
    Stream.cycle([1])
    |> Enum.reduce_while(0, fn step, number ->
      case :crypto.hash(:md5, "#{secret}#{number + step}")
           |> Base.encode16()
           |> String.starts_with?(prefix) do
        true -> {:halt, number + step}
        false -> {:cont, number + step}
      end
    end)
  end

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
