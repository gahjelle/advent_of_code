defmodule AOC2018.Day03.Test do
  @moduledoc """
  Tests for Advent of Code 2018, day 3: No Matter How You Slice It
  """
  use ExUnit.Case, async: true
  require AOC
  import AOC2018.Day03, only: [parse: 1, part1: 1, part2: 1]
  doctest(AOC2018.Day03, import: true)

  @puzzle_dir "lib/2018/03_no_matter_how_you_slice_it/"
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
    assert example1 === %{
             {3, 2} => [3],
             {3, 3} => [2],
             {4, 2} => [3, 1],
             {4, 3} => [1]
           }
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == 1
  end

  @tag :example
  test "part 2 example 1", %{example1: example1} do
    assert part2(example1) == 2
  end

  @tag :example
  test "part 1 example 2", %{example2: example2} do
    assert part1(example2) == 4
  end

  @tag :example
  test "part 2 example 2", %{example2: example2} do
    assert part2(example2) == 3
  end

  @tag :solution
  @tag :year2018
  @tag :day3
  test "part 1 solved", %{input: input} do
    assert part1(input) == 111_485
  end

  @tag :solution
  @tag :year2018
  @tag :day3
  test "part 2 solved", %{input: input} do
    assert part2(input) == 113
  end
end
