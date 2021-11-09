defmodule AOC2017.Day01 do
  @moduledoc """
  Advent of Code 2017, day 1: Inverse Captcha
  """
  require AOC

  def parse(puzzle_input) do
    puzzle_input
    |> String.to_integer()
    |> Integer.digits()
  end

  def part1(input) do
    input
    |> prepend_last()
    |> Enum.reduce({nil, 0}, &compare_consecutive/2)
    |> elem(1)
  end

  def part2(input) do
    half_length = input |> length() |> half() |> trunc()

    input
    |> Enum.chunk_every(half_length)
    |> Enum.zip()
    |> Enum.filter(fn {first, second} -> first == second end)
    |> Enum.map(fn {first, second} -> first + second end)
    |> Enum.sum()
  end

  defp prepend_last(digits), do: [digits |> Enum.reverse() |> hd | digits]
  defp compare_consecutive(current, {current, total}), do: {current, total + current}
  defp compare_consecutive(current, {_previous, total}), do: {current, total}
  defp half(number), do: number / 2

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
