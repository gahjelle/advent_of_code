defmodule AOC2021.Day03 do
  @moduledoc """
  Advent of Code 2021, day 3: Binary Diagnostic
  """
  require AOC

  @doc """
  Parse input
  """
  def parse(puzzle_input) do
    puzzle_input
    |> String.split("\n")
    |> Enum.map(fn bn -> bn |> String.split("", trim: true) |> Enum.map(&String.to_integer/1) end)
  end

  @doc """
  Solve part 1
  """
  def part1(input) do
    num_columns = input |> Enum.at(0) |> length
    gamma = input |> gamma_rate() |> Integer.undigits(2)
    epsilon = Bitwise.bnot(gamma) + Integer.pow(2, num_columns)
    gamma * epsilon
  end

  @doc """
  Solve part 2
  """
  def part2(input) do
    oxygen_generator = input |> oxygen_generator_rating() |> Integer.undigits(2)
    co2_scrubber = input |> co2_scrubber_rating() |> Integer.undigits(2)
    oxygen_generator * co2_scrubber
  end

  @doc """
  Sum each column

  ## Example:

      iex> sum_columns([[1, 0, 1], [0, 1, 1]])
      [1, 1, 2]
  """
  def sum_columns(report) do
    num_columns = report |> Enum.at(0) |> length

    report
    |> Enum.reduce(List.duplicate(0, num_columns), fn row, sum ->
      Enum.zip(row, sum) |> Enum.map(fn {acc, new} -> acc + new end)
    end)
  end

  @doc """
  Calculate gamma rate, the most common binary digit in each position

  ## Example:

      iex> gamma_rate([[1, 0, 1], [0, 1, 1], [0, 1, 0]])
      [0, 1, 1]
  """
  def gamma_rate(report) do
    num_rows = report |> length

    report
    |> sum_columns()
    |> Enum.map(fn sum -> if sum >= num_rows / 2, do: 1, else: 0 end)
  end

  @doc """
  Calculate oxygen generator rating, the element with the most common bits

  ## Example:

      iex> oxygen_generator_rating([[1, 0, 1], [0, 1, 1], [0, 1, 0]])
      [0, 1, 1]
  """
  def oxygen_generator_rating(report) do
    report |> filter_rows(fn row, col_num -> row |> gamma_rate() |> Enum.at(col_num) end)
  end

  @doc """
  Calculate CO2 scrubber rating, the element with the most common bits

  ## Example:

      iex> co2_scrubber_rating([[1, 0, 1], [0, 1, 1], [0, 1, 0]])
      [1, 0, 1]
  """
  def co2_scrubber_rating(report) do
    report
    |> filter_rows(fn row, col_num ->
      row |> gamma_rate() |> Enum.map(&(1 - &1)) |> Enum.at(col_num)
    end)
  end

  defp filter_rows(report, chooser), do: filter_rows(report, 0, chooser)
  defp filter_rows([row], _, _), do: row

  defp filter_rows(report, column, chooser) do
    filter_rows(
      report |> Enum.filter(fn row -> row |> Enum.at(column) == chooser.(report, column) end),
      column + 1,
      chooser
    )
  end

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
