defmodule AOC2020.Day05.Test do
  @moduledoc """
  Tests for Advent of Code 2020, day 5: Binary Boarding.
  """
  use ExUnit.Case, async: true
  require AOC
  import AOC2020.Day05, only: [parse: 1, part1: 1, part2: 1]
  doctest(AOC2020.Day05, import: true)

  @puzzle_dir "lib/2020/05_binary_boarding/"
  setup_all do
    {:ok,
     [
       example1: @puzzle_dir |> Path.join("example1.txt") |> AOC.read_text() |> parse(),
       example2: @puzzle_dir |> Path.join("example2.txt") |> AOC.read_text() |> parse(),
       input: @puzzle_dir |> Path.join("input.txt") |> AOC.read_text() |> parse()
     ]}
  end

  @tag :parse
  test "parse example", %{example1: example1} do
    assert example1 === [357, 567, 119, 820] |> MapSet.new()
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == 820
  end

  @tag :example
  test "part 2 example 2", %{example2: example2} do
    assert part2(example2) == 433
  end

  @tag :solution
  @tag :year2020
  @tag :day5
  test "part 1 solved", %{input: input} do
    assert part1(input) == 928
  end

  @tag :solution
  @tag :year2020
  @tag :day5
  test "part 2 solved", %{input: input} do
    assert part2(input) == 610
  end
end
