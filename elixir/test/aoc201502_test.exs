defmodule AOC2015.Day02.Test do
  @moduledoc """
  Tests for Advent of Code 2015, day 2: I Was Told There Would Be No Math
  """
  use ExUnit.Case, async: true
  require AOC

  alias AOC2015.Day02.Present
  import AOC2015.Day02, only: [parse: 1, part1: 1, part2: 1]
  doctest(AOC2015.Day02, import: true)
  doctest(AOC2015.Day02.Present, import: true)

  @puzzle_dir "lib/2015/02_i_was_told_there_would_be_no_math/"
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
             %Present{length: 2, width: 3, height: 4},
             %Present{length: 1, width: 1, height: 10}
           ]
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == 101
  end

  @tag :example
  test "part 2 example 1", %{example1: example1} do
    assert part2(example1) == 48
  end

  @tag :solution
  @tag :year2015
  @tag :day2
  test "part 1 solved", %{input: input} do
    assert part1(input) == 1_598_415
  end

  @tag :solution
  @tag :year2015
  @tag :day2
  test "part 2 solved", %{input: input} do
    assert part2(input) == 3_812_909
  end
end
