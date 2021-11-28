defmodule AOC2016.Day01.Test do
  @moduledoc """
  Tests for Advent of Code 2016, day 1: No Time for a Taxicab
  """
  use ExUnit.Case, async: true
  require AOC

  import AOC2016.Day01, only: [parse: 1, part1: 1, part2: 1]
  @puzzle_dir "lib/2016/01_no_time_for_a_taxicab/"

  setup_all do
    {:ok,
     [
       example1: @puzzle_dir |> Path.join("example1.txt") |> AOC.read_text() |> parse(),
       example2: @puzzle_dir |> Path.join("example2.txt") |> AOC.read_text() |> parse(),
       input: @puzzle_dir |> Path.join("input.txt") |> AOC.read_text() |> parse()
     ]}
  end

  @tag :parse
  test "parse example", %{example1: example1} do
    assert example1 === [{:right, 5}, {:left, 5}, {:right, 5}, {:right, 3}]
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == 12
  end

  @tag :example
  test "part 2 example 2", %{example2: example2} do
    assert part2(example2) == 4
  end

  @tag :solution
  @tag :year2016
  @tag :day1
  test "part 1 solved", %{input: input} do
    assert part1(input) == 246
  end

  @tag :solution
  @tag :year2016
  @tag :day1
  test "part 2 solved", %{input: input} do
    assert part2(input) == 124
  end
end
