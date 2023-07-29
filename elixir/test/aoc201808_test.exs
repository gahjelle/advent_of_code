defmodule AOC2018.Day08.Test do
  @moduledoc """
  Tests for Advent of Code 2018, day 8: Memory Maneuver.
  """
  use ExUnit.Case, async: true
  require AOC
  import AOC2018.Day08, only: [parse: 1, part1: 1, part2: 1]
  doctest(AOC2018.Day08, import: true)

  @puzzle_dir "lib/2018/08_memory_maneuver/"
  setup_all do
    {:ok,
     [
       example1: @puzzle_dir |> Path.join("example1.txt") |> AOC.read_text() |> parse(),
       input: @puzzle_dir |> Path.join("input.txt") |> AOC.read_text() |> parse()
     ]}
  end

  @tag :parse
  test "parse example", %{example1: example1} do
    assert example1 === [2, 3, 0, 3, 10, 11, 12, 1, 1, 0, 1, 99, 2, 1, 1, 2]
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == 138
  end

  @tag :example
  test "part 2 example 1", %{example1: example1} do
    assert part2(example1) == 66
  end

  @tag :solution
  @tag :year2018
  @tag :day8
  test "part 1 solved", %{input: input} do
    assert part1(input) == 46_829
  end

  @tag :solution
  @tag :year2018
  @tag :day8
  test "part 2 solved", %{input: input} do
    assert part2(input) == 37_450
  end
end
