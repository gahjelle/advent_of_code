defmodule AOC2016.Day01.Test do
  use ExUnit.Case, async: true
  require AOC

  import AOC2016.Day01, only: [parse: 1, part1: 1, part2: 1]
  @puzzle_dir "lib/2016/01_no_time_for_a_taxicab/"

  setup _context do
    {:ok,
     [
       example1: @puzzle_dir |> Path.join("example1.txt") |> AOC.read_text() |> parse(),
       example2: @puzzle_dir |> Path.join("example2.txt") |> AOC.read_text() |> parse(),
       input: @puzzle_dir |> Path.join("input.txt") |> AOC.read_text() |> parse()
     ]}
  end

  @tag :parse
  test "parse example", context do
    assert context[:example1] === [{:right, 5}, {:left, 5}, {:right, 5}, {:right, 3}]
  end

  @tag :example
  test "part 1 example 1", context do
    assert part1(context[:example1]) == 12
  end

  @tag :example
  test "part 2 example 2", context do
    assert part2(context[:example2]) == 4
  end

  @tag :solution
  @tag :year2016
  @tag :day1
  test "part 1 solved", context do
    assert part1(context[:input]) == 246
  end

  @tag :solution
  @tag :year2016
  @tag :day1
  test "part 2 solved", context do
    assert part2(context[:input]) == 124
  end
end
