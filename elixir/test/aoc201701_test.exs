defmodule AOC2017.Day01.Test do
  use ExUnit.Case, async: true
  require AOC

  import AOC2017.Day01, only: [parse: 1, part1: 1, part2: 1]
  @puzzle_dir "lib/2017/01_inverse_captcha/"

  setup _context do
    {:ok,
     [
       example4: @puzzle_dir |> Path.join("example4.txt") |> AOC.read_text() |> parse(),
       example7: @puzzle_dir |> Path.join("example7.txt") |> AOC.read_text() |> parse(),
       example9: @puzzle_dir |> Path.join("example9.txt") |> AOC.read_text() |> parse(),
       input: @puzzle_dir |> Path.join("input.txt") |> AOC.read_text() |> parse()
     ]}
  end

  @tag :parse
  test "parse example", context do
    assert context[:example7] === [1, 2, 3, 4, 2, 5]
  end

  @tag :example
  test "part 1 example", context do
    assert part1(context[:example4]) == 9
  end

  @tag :example
  test "part 2 example", context do
    assert part2(context[:example9]) == 4
  end

  @tag :solution
  @tag :year2017
  @tag :day1
  test "part 1 solved", context do
    assert part1(context[:input]) == 1141
  end

  @tag :solution
  @tag :year2017
  @tag :day1
  test "part 2 solved", context do
    assert part2(context[:input]) == 950
  end
end
