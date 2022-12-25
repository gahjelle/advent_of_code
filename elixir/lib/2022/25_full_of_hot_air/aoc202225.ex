defmodule AOC2022.Day25 do
  @moduledoc """
  Advent of Code 2022, day 25: Full of Hot Air.
  """
  require AOC

  @doc """
  Parse input.
  """
  def parse(puzzle_input), do: puzzle_input |> String.split("\n", trim: true)

  @doc """
  Solve part 1.
  """
  def part1(fuel), do: fuel |> Enum.map(&from_snafu/1) |> Enum.sum() |> then(&to_snafu/1)

  @doc """
  There is no part 2.
  """
  def part2(_), do: nil

  @doc """
  Convert from SANFU to decimal.

  ## Examples:

      iex> from_snafu("1=")
      3
      iex> from_snafu("111")
      31
      iex> from_snafu("1121-1110-1=0")
      314159265
  """
  def from_snafu(snafu) do
    snafu
    |> String.to_charlist()
    |> Enum.map(&digit_from_snafu/1)
    |> Enum.reverse()
    |> Enum.with_index()
    |> Enum.map(fn {snafu, power} -> snafu * 5 ** power end)
    |> Enum.sum()
  end

  @doc """
  Convert one SNAFU digit to decimal.

  ## Examples:

      iex> digit_from_snafu(?2)
      2
      iex> digit_from_snafu(?-)
      -1
  """
  def digit_from_snafu(?2), do: 2
  def digit_from_snafu(?1), do: 1
  def digit_from_snafu(?0), do: 0
  def digit_from_snafu(?-), do: -1
  def digit_from_snafu(?=), do: -2

  @doc """
  Convert from decimal to SNAFU.

  ## Examples:

      iex> to_snafu(12)
      "22"
      iex> to_snafu(13)
      "1=="
      iex> to_snafu(123)
      "100="
      iex> to_snafu(12345)
      "1-0---0"
  """
  def to_snafu(number), do: to_snafu(number, [])
  def to_snafu(0, snafu), do: List.to_string(snafu)

  def to_snafu(number, suffix),
    do: to_snafu(div(number + 2, 5), [digit_to_snafu(rem(number + 2, 5) - 2) | suffix])

  @doc """
  Convert one digit to SNAFU.

  ## Examples:

      iex> digit_to_snafu(1)
      ?1
      iex> digit_to_snafu(-2)
      ?=
  """
  def digit_to_snafu(2), do: ?2
  def digit_to_snafu(1), do: ?1
  def digit_to_snafu(0), do: ?0
  def digit_to_snafu(-1), do: ?-
  def digit_to_snafu(-2), do: ?=

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
