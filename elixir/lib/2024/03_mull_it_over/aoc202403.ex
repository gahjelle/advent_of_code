defmodule AOC2024.Day03 do
  @moduledoc """
  Advent of Code 2024, day 3: Mull it Over.
  """
  require AOC

  @doc """
  Parse input.
  """
  def parse(puzzle_input) do
    puzzle_input |> String.split("\n", trim: true) |> Enum.join(" ") |> do_or_dont()
  end

  @doc """
  Split a text on "don't()" and "do()"

  ## Example

      iex> do_or_dont("First don't() do what you want then do() it anyway")
      ["First ", " do what you want then ", " it anyway"]
  """
  def do_or_dont(text), do: do_or_dont(text, [], true)
  def do_or_dont("", parts, _), do: parts |> Enum.reverse()

  def do_or_dont(text, parts, true) do
    case String.split(text, "don't()", parts: 2) do
      [left, right] -> do_or_dont(right, [left | parts], false)
      [rest] -> do_or_dont("", [rest | parts], false)
    end
  end

  def do_or_dont(text, parts, false) do
    case String.split(text, "do()", parts: 2) do
      [left, right] -> do_or_dont(right, [left | parts], true)
      [rest] -> do_or_dont("", [rest | parts], true)
    end
  end

  @doc """
  Solve part 1.
  """
  def part1(data) do
    data |> Enum.join("") |> find_multiplies() |> Enum.sum()
  end

  @doc """
  Solve part 2.
  """
  def part2(data) do
    data |> Enum.take_every(2) |> Enum.join("") |> find_multiplies() |> Enum.sum()
  end

  @doc """
  Find occurences of "mul(num1,num2)" in text and carry out the multiplications.

  ## Example

      iex> find_multiplies("First mul(4,2) then mul(44,46) and end with mul")
      [8, 2024]
  """
  def find_multiplies(text) do
    Regex.scan(~r/mul\((\d{1,3}),(\d{1,3})\)/, text, capture: :all_but_first)
    |> Enum.map(fn [first, second] -> String.to_integer(first) * String.to_integer(second) end)
  end

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
