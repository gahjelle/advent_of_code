defmodule AOC2015.Day03.Test do
  use ExUnit.Case, async: true
  require AOC

  import AOC2015.Day03, only: [parse: 1, part1: 1, part2: 1]
  @puzzle_dir "lib/2015/03_perfectly_spherical_houses_in_a_vacuum/"

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
    assert context[:example1] === [{0, 1}, {1, 0}, {0, -1}, {-1, 0}]
  end

  @tag :example
  test "part 1 example 1", context do
    assert part1(context[:example1]) == 4
  end

  @tag :example
  test "part 1 example 2", context do
    assert part1(context[:example2]) == 2
  end

  @tag :example
  test "part 2 example 1", context do
    assert part2(context[:example1]) == 3
  end

  @tag :example
  test "part 2 example 2", context do
    assert part2(context[:example2]) == 11
  end

  @tag :solution
  @tag :year2015
  @tag :day3
  test "part 1 solved", context do
    assert part1(context[:input]) == 2565
  end

  @tag :solution
  @tag :year2015
  @tag :day3
  test "part 2 solved", context do
    assert part2(context[:input]) == 2639
  end
end
