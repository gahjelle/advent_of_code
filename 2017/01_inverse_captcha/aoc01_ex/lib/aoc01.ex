defmodule AOC2017.Day01 do
  @moduledoc """
  Inverse Captcha

  Advent of Code 2017, day 1
  Solution by Geir Arne Hjelle, 2021-11-05
  """

  def main(args) do
    Enum.map(args, &solve/1)
  end

  def solve(path) do
    IO.puts("\nPart 1 (#{path}):")
    path |> parse() |> Enum.map(&part1/1) |> Enum.join("\n") |> IO.puts()

    IO.puts("\nPart 2: (#{path})")
    path |> parse() |> Enum.map(&part2/1) |> Enum.join("\n") |> IO.puts()
  end

  def parse(path) do
    with {:ok, file} <- File.read(path) do
      file
      |> String.trim()
      |> String.split("\n")
      |> Enum.map(&String.to_integer/1)
      |> Enum.map(&Integer.digits/1)
    end
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
end
