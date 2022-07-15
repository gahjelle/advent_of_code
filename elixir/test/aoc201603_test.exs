defmodule AOC2016.Day03.Test do
  @moduledoc """
  Tests for Advent of Code 2016, day 3: Squares With Three Sides
  """
  use ExUnit.Case, async: true
  require AOC
  import AOC2016.Day03, only: [parse: 1, part1: 1, part2: 1]
  doctest(AOC2016.Day03, import: true)

  @puzzle_dir "lib/2016/03_squares_with_three_sides/"
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
             [5, 10, 25],
             [5, 12, 13],
             [12, 13, 8]
           ]
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == 2
  end

  @tag :example
  test "part 2 example 1", %{example1: example1} do
    assert part2(example1) == 1
  end

  @tag :solution
  @tag :year2016
  @tag :day3
  test "part 1 solved", %{input: input} do
    assert part1(input) == 1050
  end

  @tag :solution
  @tag :year2016
  @tag :day3
  test "part 2 solved", %{input: input} do
    assert part2(input) == 1921
  end
end
