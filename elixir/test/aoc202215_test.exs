defmodule AOC2022.Day15.Test do
  @moduledoc """
  Tests for Advent of Code 2022, day 15: Beacon Exclusion Zone.
  """
  use ExUnit.Case, async: true
  require AOC

  import AOC2022.Day15,
    only: [parse: 1, part1: 1, part1: 2, part2: 1, part2: 2, row_coverage: 2]

  doctest(AOC2022.Day15, import: true)

  @puzzle_dir "lib/2022/15_beacon_exclusion_zone/"
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
             {{2, 18}, {-2, 15}},
             {{9, 16}, {10, 16}},
             {{13, 2}, {15, 3}},
             {{12, 14}, {10, 16}},
             {{10, 20}, {10, 16}},
             {{14, 17}, {10, 16}},
             {{8, 7}, {2, 10}},
             {{2, 0}, {2, 10}},
             {{0, 11}, {2, 10}},
             {{20, 14}, {25, 17}},
             {{17, 20}, {21, 22}},
             {{16, 7}, {15, 3}},
             {{14, 3}, {15, 3}},
             {{20, 1}, {15, 3}}
           ]
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1, 10) == 26
  end

  @tag :example
  test "part 2 example 1", %{example1: example1} do
    assert part2(example1, 20) == 56_000_011
  end

  @tag :example
  test "coverage example 1", %{example1: example1} do
    assert row_coverage(example1, 11) == [-3..13, 15..25]
  end

  @tag :solution
  @tag :year2022
  @tag :day15
  test "part 1 solved", %{input: input} do
    assert part1(input) == 5_508_234
  end

  @tag :solution
  @tag :year2022
  @tag :day15
  test "part 2 solved", %{input: input} do
    assert part2(input) == 10_457_634_860_779
  end
end
