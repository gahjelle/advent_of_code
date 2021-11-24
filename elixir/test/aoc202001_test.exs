defmodule AOC2020.Day01.Test do
  use ExUnit.Case, async: true
  require AOC

  import AOC2020.Day01, only: [parse: 1, part1: 1, part2: 1]
  @puzzle_dir "lib/2020/01_report_repair/"

  setup _context do
    {:ok,
     [
       example1: @puzzle_dir |> Path.join("example1.txt") |> AOC.read_text() |> parse(),
       input: @puzzle_dir |> Path.join("input.txt") |> AOC.read_text() |> parse()
     ]}
  end

  @tag :parse
  test "parse example", context do
    assert context[:example1] === MapSet.new([1721, 979, 366, 299, 675, 1456])
  end

  @tag :example
  test "part 1 example 1", context do
    assert part1(context[:example1]) == 514_579
  end

  @tag :example
  test "part 2 example 1", context do
    assert part2(context[:example1]) == 241_861_950
  end

  @tag :solution
  @tag :year2020
  @tag :day1
  test "part 1 solved", context do
    assert part1(context[:input]) == 744_475
  end

  @tag :solution
  @tag :year2020
  @tag :day1
  test "part 2 solved", context do
    assert part2(context[:input]) == 70_276_940
  end
end
