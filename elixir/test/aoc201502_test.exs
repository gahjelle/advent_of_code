defmodule AOC2015.Day02.Test do
  use ExUnit.Case, async: true
  require AOC

  alias AOC2015.Day02.Present
  import AOC2015.Day02, only: [parse: 1, part1: 1, part2: 1]
  @puzzle_dir "lib/2015/02_i_was_told_there_would_be_no_math/"

  setup _context do
    {:ok,
     [
       example1: @puzzle_dir |> Path.join("example1.txt") |> AOC.read_text() |> parse(),
       input: @puzzle_dir |> Path.join("input.txt") |> AOC.read_text() |> parse()
     ]}
  end

  @tag :parse
  test "parse example", context do
    assert context[:example1] === [
             %Present{length: 2, width: 3, height: 4},
             %Present{length: 1, width: 1, height: 10}
           ]
  end

  @tag :example
  test "part 1 example 1", context do
    assert part1(context[:example1]) == 101
  end

  @tag :example
  test "part 2 example", context do
    assert part2(context[:example1]) == 48
  end

  @tag :solution
  @tag :year2015
  @tag :day2
  test "part 1 solved", context do
    assert part1(context[:input]) == 1_598_415
  end

  @tag :solution
  @tag :year2015
  @tag :day2
  test "part 2 solved", context do
    assert part2(context[:input]) == 3_812_909
  end
end
