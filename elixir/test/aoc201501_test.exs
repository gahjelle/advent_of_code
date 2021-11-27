defmodule AOC2015.Day01.Test do
  @moduledoc """
  Tests for Advent of Code 2015, day 1: Not Quite Lisp
  """
  use ExUnit.Case, async: true
  require AOC

  import AOC2015.Day01, only: [parse: 1, part1: 1, part2: 1]
  @puzzle_dir "lib/2015/01_not_quite_lisp/"

  setup _context do
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
  test "parse example", context do
    assert context[:example1] === [1, 1, -1, -1]
  end

  @tag :example
  test "part 1 example 1", context do
    assert part1(context[:example1]) == 0
  end

  @tag :example
  test "part 1 example 2", context do
    assert part1(context[:example2]) == 3
  end

  @tag :example
  test "part 1 example 3", context do
    assert part1(context[:example3]) == -3
  end

  @tag :example
  test "part 2 example", context do
    assert part2(context[:example4]) == 5
  end

  @tag :solution
  @tag :year2015
  @tag :day1
  test "part 1 solved", context do
    assert part1(context[:input]) == 232
  end

  @tag :solution
  @tag :year2015
  @tag :day1
  test "part 2 solved", context do
    assert part2(context[:input]) == 1783
  end
end
