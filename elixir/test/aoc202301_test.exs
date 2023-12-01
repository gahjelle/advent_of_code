defmodule AOC2023.Day01.Test do
  @moduledoc """
  Tests for Advent of Code 2023, day 1: Trebuchet?!.
  """
  use ExUnit.Case, async: true
  require AOC
  import AOC2023.Day01, only: [parse: 1, part1: 1, part2: 1]
  doctest(AOC2023.Day01, import: true)

  @puzzle_dir "lib/2023/01_trebuchet/"
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
    assert example1 === [
             "1abc2",
             "pqr3stu8vwx",
             "a1b2c3d4e5f",
             "treb7uchet"
           ]
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == 142
  end

  @tag :example
  test "part 2 example 1", %{example1: example1} do
    assert part2(example1) == 142
  end

  @tag :example
  test "part 2 example 2", %{example2: example2} do
    assert part2(example2) == 281
  end

  @tag :solution
  @tag :year2023
  @tag :day1
  test "part 1 solved", %{input: input} do
    assert part1(input) == 55_017
  end

  @tag :solution
  @tag :year2023
  @tag :day1
  test "part 2 solved", %{input: input} do
    assert part2(input) == 53_539
  end
end
