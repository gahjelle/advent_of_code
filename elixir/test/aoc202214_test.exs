defmodule AOC2022.Day14.Test do
  @moduledoc """
  Tests for Advent of Code 2022, day 14: Regolith Reservoir.
  """
  use ExUnit.Case, async: true
  require AOC
  import AOC2022.Day14, only: [parse: 1, part1: 1, part2: 1]
  doctest(AOC2022.Day14, import: true)

  @puzzle_dir "lib/2022/14_regolith_reservoir/"
  setup_all do
    {:ok,
     [
       example1: @puzzle_dir |> Path.join("example1.txt") |> AOC.read_text() |> parse(),
       input: @puzzle_dir |> Path.join("input.txt") |> AOC.read_text() |> parse()
     ]}
  end

  @tag :parse
  test "parse example", %{example1: example1} do
    assert example1 === %{
             {498, 4} => :rock,
             {498, 5} => :rock,
             {498, 6} => :rock,
             {497, 6} => :rock,
             {496, 6} => :rock,
             {503, 4} => :rock,
             {502, 4} => :rock,
             {502, 5} => :rock,
             {502, 6} => :rock,
             {502, 7} => :rock,
             {502, 8} => :rock,
             {502, 9} => :rock,
             {501, 9} => :rock,
             {500, 9} => :rock,
             {499, 9} => :rock,
             {498, 9} => :rock,
             {497, 9} => :rock,
             {496, 9} => :rock,
             {495, 9} => :rock,
             {494, 9} => :rock
           }
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == 24
  end

  @tag :example
  test "part 2 example 1", %{example1: example1} do
    assert part2(example1) == 93
  end

  @tag :solution
  @tag :year2022
  @tag :day14
  test "part 1 solved", %{input: input} do
    assert part1(input) == 1_016
  end

  @tag :solution
  @tag :year2022
  @tag :day14
  test "part 2 solved", %{input: input} do
    assert part2(input) == 25_402
  end
end
