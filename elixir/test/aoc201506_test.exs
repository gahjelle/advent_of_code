defmodule AOC2015.Day06.Test do
  @moduledoc """
  Tests for Advent of Code 2015, day 6: Probably a Fire Hazard
  """
  use ExUnit.Case, async: true
  require AOC
  import AOC2015.Day06, only: [parse: 1, part1: 1, part2: 1]
  doctest(AOC2015.Day06, import: true)

  @puzzle_dir "lib/2015/06_probably_a_fire_hazard/"
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
    assert example1 === [
             {:on, {0, 0}, {999, 999}},
             {:toggle, {0, 0}, {999, 0}},
             {:off, {499, 499}, {500, 500}}
           ]
  end

  @tag :slow
  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == 1_000_000 + (0 - 1000) - 4
  end

  @tag :example
  test "part 1 example 2", %{example2: example2} do
    #    0123        0123        0123        0123        0123
    #  0 ....      0 ###.      0 ###.      0 ###.      0 ##..
    #  1 ....  ->  1 ###.  ->  1 ...#  ->  1 ...#  ->  1 ..##
    #  2 ....      2 ###.      2 ###.      2 #...      2 #.#.
    #  3 ....      3 ....      3 ....      3 ....      3 ..#.
    assert part1(example2) == 9 + (1 - 3) - 2 + (3 - 1)
  end

  @tag :example
  test "part 2 example 2", %{example2: example2} do
    #    0123        0123        0123        0123        0123
    #  0 0000      0 1110      0 1110      0 1110      0 1130
    #  1 0000  ->  1 1110  ->  1 3332  ->  1 3222  ->  1 3242
    #  2 0000      2 1110      2 1110      2 1000      2 1020
    #  3 0000      3 0000      3 0000      3 0000      3 0020
    assert part2(example2) == 21
  end

  @tag :slow
  @tag :solution
  @tag :year2015
  @tag :day6
  test "part 1 solved", %{input: input} do
    assert part1(input) == 569_999
  end

  @tag :slow
  @tag :solution
  @tag :year2015
  @tag :day6
  test "part 2 solved", %{input: input} do
    assert part2(input) == 17_836_115
  end
end
