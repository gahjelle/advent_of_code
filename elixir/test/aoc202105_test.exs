defmodule AOC2021.Day05.Test do
  @moduledoc """
  Tests for Advent of Code 2021, day 5: Hydrothermal Venture
  """
  use ExUnit.Case, async: true
  require AOC
  import AOC2021.Day05, only: [parse: 1, part1: 1, part2: 1]
  doctest(AOC2021.Day05, import: true)

  @puzzle_dir "lib/2021/05_hydrothermal_venture/"
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
             {:horisontal, {0, 9}, {5, 9}},
             {:diagonal, {8, 0}, {0, 8}},
             {:horisontal, {9, 4}, {3, 4}},
             {:vertical, {2, 2}, {2, 1}},
             {:vertical, {7, 0}, {7, 4}},
             {:diagonal, {6, 4}, {2, 0}},
             {:horisontal, {0, 9}, {2, 9}},
             {:horisontal, {3, 4}, {1, 4}},
             {:diagonal, {0, 0}, {8, 8}},
             {:diagonal, {5, 5}, {8, 2}}
           ]
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == 5
  end

  @tag :example
  test "part 2 example 1", %{example1: example1} do
    assert part2(example1) == 12
  end

  @tag :solution
  @tag :year2021
  @tag :day5
  test "part 1 solved", %{input: input} do
    assert part1(input) == 6856
  end

  @tag :solution
  @tag :year2021
  @tag :day5
  test "part 2 solved", %{input: input} do
    assert part2(input) == 20_666
  end
end
