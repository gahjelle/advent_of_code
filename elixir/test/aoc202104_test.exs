defmodule AOC2021.Day04.Test do
  @moduledoc """
  Tests for Advent of Code 2021, day 4: Giant Squid
  """
  use ExUnit.Case, async: true
  require AOC
  import AOC2021.Day04, only: [parse: 1, part1: 1, part2: 1]
  doctest(AOC2021.Day04, import: true)

  @puzzle_dir "lib/2021/04_giant_squid/"
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
    assert example1 ===
             {[0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
              [
                %{
                  0 => {0, 0},
                  1 => {0, 1},
                  2 => {1, 0},
                  3 => {1, 1},
                  5 => {2, 1},
                  6 => {2, 2},
                  7 => {1, 2},
                  8 => {0, 2},
                  9 => {2, 0}
                }
              ]}
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == (6 + 7 + 8 + 9) * 5
  end

  @tag :example
  test "part 1 example 2", %{example2: example2} do
    assert part1(example2) == 4512
  end

  @tag :example
  test "part 2 example 1", %{example1: example1} do
    assert part2(example1) == (6 + 7 + 8 + 9) * 5
  end

  @tag :example
  test "part 2 example 2", %{example2: example2} do
    assert part2(example2) == 1924
  end

  @tag :solution
  @tag :year2021
  @tag :day4
  test "part 1 solved", %{input: input} do
    assert part1(input) == 10_374
  end

  @tag :solution
  @tag :year2021
  @tag :day4
  test "part 2 solved", %{input: input} do
    assert part2(input) == 24_742
  end
end
