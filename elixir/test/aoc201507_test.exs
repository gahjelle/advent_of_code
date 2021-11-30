defmodule AOC2015.Day07.Test do
  @moduledoc """
  Tests for Advent of Code 2015, day 7: Some Assembly Required
  """
  use ExUnit.Case, async: true
  require AOC
  import AOC2015.Day07, only: [parse: 1, part1: 1, part2: 1]
  doctest(AOC2015.Day07, import: true)
  use Bitwise

  @puzzle_dir "lib/2015/07_some_assembly_required/"
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
             {:set, "x", {123}},
             {:set, "b", {456}},
             {:and, "d", {1, "b"}},
             {:or, "aoc", {"x", "b"}},
             {:lshift, "f", {"x", 2}},
             {:rshift, "g", {"b", 2}},
             {:not, "h", {"x"}},
             {:not, "i", {"b"}},
             {:setfrom, "z", {"g"}},
             {:or, "a", {"b", "z"}}
           ]
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == (456 ||| 456 >>> 2)
  end

  @tag :example
  test "part 2 example 1", %{example1: example1} do
    assert part2(example1) == (506 ||| 506 >>> 2)
  end

  @tag :solution
  @tag :year2015
  @tag :day7
  test "part 1 solved", %{input: input} do
    assert part1(input) == 3176
  end

  @tag :solution
  @tag :year2015
  @tag :day7
  test "part 2 solved", %{input: input} do
    assert part2(input) == 14_710
  end
end
