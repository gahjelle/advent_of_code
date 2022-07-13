defmodule AOC2016.Day02.Test do
  @moduledoc """
  Tests for Advent of Code 2016, day 2: Bathroom Security
  """
  use ExUnit.Case, async: true
  require AOC
  import AOC2016.Day02, only: [parse: 1, part1: 1, part2: 1]
  doctest(AOC2016.Day02, import: true)

  @puzzle_dir "lib/2016/02_bathroom_security/"
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
             "ULL",
             "RRDDD",
             "LURDL",
             "UUUUD"
           ]
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == "1985"
  end

  @tag :example
  test "part 2 example 1", %{example1: example1} do
    assert part2(example1) == "5DB3"
  end

  @tag :solution
  @tag :year2016
  @tag :day2
  test "part 1 solved", %{input: input} do
    assert part1(input) == "92435"
  end

  @tag :solution
  @tag :year2016
  @tag :day2
  test "part 2 solved", %{input: input} do
    assert part2(input) == "C1A88"
  end
end
