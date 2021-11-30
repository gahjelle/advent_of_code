defmodule AOC2017.Day02.Test do
  @moduledoc """
  Tests for Advent of Code 2017, day 2: Corruption Checksum
  """
  use ExUnit.Case, async: true
  require AOC
  import AOC2017.Day02, only: [parse: 1, part1: 1, part2: 1]
  doctest(AOC2017.Day02, import: true)

  @puzzle_dir "lib/2017/02_corruption_checksum/"
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
    assert example1 === [[5, 1, 9, 5], [7, 5, 3], [2, 4, 6, 8]]
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == 18
  end

  @tag :example
  test "part 2 example 2", %{example2: example2} do
    assert part2(example2) == 9
  end

  @tag :solution
  @tag :year2017
  @tag :day2
  test "part 1 solved", %{input: input} do
    assert part1(input) == 39_126
  end

  @tag :solution
  @tag :year2017
  @tag :day2
  test "part 2 solved", %{input: input} do
    assert part2(input) == 258
  end
end
