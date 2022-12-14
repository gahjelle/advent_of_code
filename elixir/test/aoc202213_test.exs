defmodule AOC2022.Day13.Test do
  @moduledoc """
  Tests for Advent of Code 2022, day 13: Distress Signal.
  """
  use ExUnit.Case, async: true
  require AOC
  import AOC2022.Day13, only: [parse: 1, part1: 1, part2: 1]
  doctest(AOC2022.Day13, import: true)

  @puzzle_dir "lib/2022/13_distress_signal/"
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
             {[1, 1, 3, 1, 1], [1, 1, 5, 1, 1]},
             {[[1], [2, 3, 4]], [[1], 4]},
             {[9], [[8, 7, 6]]},
             {[[4, 4], 4, 4], [[4, 4], 4, 4, 4]},
             {[7, 7, 7, 7], [7, 7, 7]},
             {[], [3]},
             {[[[]]], [[]]},
             {[1, [2, [3, [4, [5, 6, 7]]]], 8, 9], [1, [2, [3, [4, [5, 6, 0]]]], 8, 9]}
           ]
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == 13
  end

  @tag :example
  test "part 2 example 1", %{example1: example1} do
    assert part2(example1) == 140
  end

  @tag :solution
  @tag :year2022
  @tag :day13
  test "part 1 solved", %{input: input} do
    assert part1(input) == 6_428
  end

  @tag :solution
  @tag :year2022
  @tag :day13
  test "part 2 solved", %{input: input} do
    assert part2(input) == 22_464
  end
end
