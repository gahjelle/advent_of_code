defmodule AOC2015.Day04 do
  @moduledoc """
  Advent of Code 2015, day 4: The Ideal Stocking Stuffer
  """
  require AOC

  def parse(puzzle_input) do
    puzzle_input |> String.split("\n") |> hd()
  end

  def part1(input) do
    input |> find_md5_with_prefix("00000")
  end

  def part2(input) do
    input |> find_md5_with_prefix("000000")
  end

  defp find_md5_with_prefix(secret, prefix) do
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
