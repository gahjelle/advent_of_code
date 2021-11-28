defmodule AOC2015.Day01.Test do
  @moduledoc """
  Tests for Advent of Code 2015, day 1: Not Quite Lisp
  """
  use ExUnit.Case, async: true
  require AOC
  import AOC2015.Day01, only: [parse: 1, part1: 1, part2: 1]

  @puzzle_dir "lib/2015/01_not_quite_lisp/"
  setup_all do
    {:ok,
     [
       example1: @puzzle_dir |> Path.join("example1.txt") |> AOC.read_text() |> parse(),
       example2: @puzzle_dir |> Path.join("example2.txt") |> AOC.read_text() |> parse(),
       example3: @puzzle_dir |> Path.join("example3.txt") |> AOC.read_text() |> parse(),
       example4: @puzzle_dir |> Path.join("example4.txt") |> AOC.read_text() |> parse(),
       input: @puzzle_dir |> Path.join("input.txt") |> AOC.read_text() |> parse()
     ]}
  end

  @tag :parse
  test "parse example", %{example1: example1} do
    assert example1 === [1, 1, -1, -1]
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == 0
  end

  @tag :example
  test "part 1 example 2", %{example2: example2} do
    assert part1(example2) == 3
  end

  @tag :example
  test "part 1 example 3", %{example3: example3} do
    assert part1(example3) == -3
  end

  @tag :example
  test "part 2 example 4", %{example4: example4} do
    assert part2(example4) == 5
  end

  @tag :solution
  @tag :year2015
  @tag :day1
  test "part 1 solved", %{input: input} do
    assert part1(input) == 232
  end

  @tag :solution
  @tag :year2015
  @tag :day1
  test "part 2 solved", %{input: input} do
    assert part2(input) == 1783
  end
end
