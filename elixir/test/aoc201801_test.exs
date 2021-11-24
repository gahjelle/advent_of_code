defmodule AOC2018.Day01.Test do
  use ExUnit.Case, async: true
  require AOC

  import AOC2018.Day01, only: [parse: 1, part1: 1, part2: 1]
  @puzzle_dir "lib/2018/01_chronal_calibration/"

  setup _context do
    {:ok,
     [
       example1: @puzzle_dir |> Path.join("example1.txt") |> AOC.read_text() |> parse(),
       example2: @puzzle_dir |> Path.join("example2.txt") |> AOC.read_text() |> parse(),
       example3: @puzzle_dir |> Path.join("example3.txt") |> AOC.read_text() |> parse(),
       input: @puzzle_dir |> Path.join("input.txt") |> AOC.read_text() |> parse()
     ]}
  end

  @tag :parse
  test "parse example", context do
    assert context[:example1] === [1, -2, 3, 1]
  end

  @tag :example
  test "part 1 example", context do
    assert part1(context[:example1]) == 3
  end

  @tag :example
  test "part 2 example", context do
    assert part2(context[:example1]) == 2
  end

  @tag :example
  test "part 2 example 2", context do
    assert part2(context[:example2]) == 10
  end

  @tag :example
  test "part 2 example 3", context do
    assert part2(context[:example3]) == 0
  end

  @tag :solution
  @tag :year2018
  @tag :day1
  test "part 1 solved", context do
    assert part1(context[:input]) == 531
  end

  @tag :solution
  @tag :year2018
  @tag :day1
  test "part 2 solved", context do
    assert part2(context[:input]) == 76787
  end
end
