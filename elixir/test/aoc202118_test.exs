defmodule AOC2021.Day18.Test do
  @moduledoc """
  Tests for Advent of Code 2021, day 18: Snailfish
  """
  use ExUnit.Case, async: true
  require AOC
  import AOC2021.Day18, only: [parse: 1, part1: 1, part2: 1]
  doctest(AOC2021.Day18, import: true)

  @puzzle_dir "lib/2021/18_snailfish/"
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
             "[1,1]",
             "[2,2]",
             "[3,3]",
             "[4,4]",
             "[[1,2],[[3,4],5]]"
           ]
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == 1027
  end

  @tag :example
  test "part 1 example 2", %{example2: example2} do
    assert part1(example2) == 4140
  end

  @tag :skip
  @tag :example
  test "part 2 example 1", %{example1: example1} do
    assert part2(example1) == 469
  end

  @tag :skip
  @tag :example
  test "part 2 example 2", %{example2: example2} do
    assert part2(example2) == 3993
  end

  @tag :solution
  @tag :year2021
  @tag :day18
  test "part 1 solved", %{input: input} do
    assert part1(input) == 4365
  end

  @tag :solution
  @tag :year2021
  @tag :day18
  test "part 2 solved", %{input: input} do
    assert part2(input) == 4490
  end
end
