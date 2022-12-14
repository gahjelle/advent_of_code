defmodule AOC2022.Day12.Test do
  @moduledoc """
  Tests for Advent of Code 2022, day 12: Hill Climbing Algorithm.
  """
  use ExUnit.Case, async: true
  require AOC
  import AOC2022.Day12, only: [parse: 1, part1: 1, part2: 1]
  doctest(AOC2022.Day12, import: true)

  @puzzle_dir "lib/2022/12_hill_climbing_algorithm/"
  setup_all do
    {:ok,
     [
       example1: @puzzle_dir |> Path.join("example1.txt") |> AOC.read_text() |> parse(),
       input: @puzzle_dir |> Path.join("input.txt") |> AOC.read_text() |> parse()
     ]}
  end

  @tag :parse
  test "parse example", %{example1: example1} do
    assert example1 ===
             {%{
                {0, 0} => 0,
                {1, 0} => 0,
                {2, 0} => 0,
                {0, 1} => 0,
                {0, 2} => 1,
                {0, 3} => 16,
                {0, 4} => 15,
                {0, 5} => 14,
                {0, 6} => 13,
                {0, 7} => 12,
                {1, 1} => 1,
                {1, 2} => 2,
                {1, 3} => 17,
                {1, 4} => 24,
                {1, 5} => 23,
                {1, 6} => 23,
                {1, 7} => 11,
                {2, 1} => 2,
                {2, 2} => 2,
                {2, 3} => 18,
                {2, 4} => 25,
                {2, 5} => 25,
                {2, 6} => 23,
                {2, 7} => 10,
                {3, 0} => 0,
                {3, 1} => 2,
                {3, 2} => 2,
                {3, 3} => 19,
                {3, 4} => 20,
                {3, 5} => 21,
                {3, 6} => 22,
                {3, 7} => 9,
                {4, 0} => 0,
                {4, 1} => 1,
                {4, 2} => 3,
                {4, 3} => 4,
                {4, 4} => 5,
                {4, 5} => 6,
                {4, 6} => 7,
                {4, 7} => 8
              }, {0, 0}, {2, 5}}
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == 31
  end

  @tag :example
  test "part 2 example 1", %{example1: example1} do
    assert part2(example1) == 29
  end

  @tag :solution
  @tag :year2022
  @tag :day12
  test "part 1 solved", %{input: input} do
    assert part1(input) == 490
  end

  @tag :solution
  @tag :year2022
  @tag :day12
  test "part 2 solved", %{input: input} do
    assert part2(input) == 488
  end
end
