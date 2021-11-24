defmodule AOC2015.Day05.Test do
  use ExUnit.Case, async: true
  require AOC

  import AOC2015.Day05, only: [parse: 1, part1: 1, part2: 1]
  @puzzle_dir "lib/2015/05_doesnt_he_have_intern-elves_for_this/"

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
    assert context[:example1] === [
             'ugknbfddgicrmopn',
             'aaa',
             'jchzalrnumimnmhp',
             'haegwjzuvuyypxyu',
             'dvszwmarrgswjxmb'
           ]
  end

  @tag :example
  test "part 1 example 1", context do
    assert part1(context[:example1]) == 2
  end

  @tag :example
  test "part 2 example 2", context do
    assert part2(context[:example2]) == 2
  end

  @tag :solution
  @tag :year2015
  @tag :day5
  test "part 1 solved", context do
    assert part1(context[:input]) == 236
  end

  @tag :solution
  @tag :year2015
  @tag :day5
  test "part 2 solved", context do
    assert part2(context[:input]) == 51
  end
end
