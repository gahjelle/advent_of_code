defmodule AOC2023.Day09.Test do
  @moduledoc """
  Tests for Advent of Code 2023, day 9: Mirage Maintenance.
  """
  use ExUnit.Case, async: true
  require AOC
  import AOC2023.Day09, only: [parse: 1, part1: 1, part2: 1]
  doctest(AOC2023.Day09, import: true)

  @puzzle_dir "lib/2023/09_mirage_maintenance/"
  setup_all do
    {:ok,
     [
       example1: @puzzle_dir |> Path.join("example1.txt") |> AOC.read_text() |> parse(),
       input: @puzzle_dir |> Path.join("input.txt") |> AOC.read_text() |> parse()
     ]}
  end

  @tag :parse
  test "parse example", %{example1: example1} do
    assert example1 === [
             [0, 3, 6, 9, 12, 15],
             [1, 3, 6, 10, 15, 21],
             [10, 13, 16, 21, 30, 45]
           ]
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == 114
  end

  @tag :example
  test "part 2 example 1", %{example1: example1} do
    assert part2(example1) == 2
  end

  @tag :solution
  @tag :year2023
  @tag :day9
  test "part 1 solved", %{input: input} do
    assert part1(input) == 1_974_913_025
  end

  @tag :solution
  @tag :year2023
  @tag :day9
  test "part 2 solved", %{input: input} do
    assert part2(input) == 884
  end
end
