defmodule AOC2022.Day04.Test do
  @moduledoc """
  Tests for Advent of Code 2022, day 4: Camp Cleanup.
  """
  use ExUnit.Case, async: true
  require AOC
  import AOC2022.Day04, only: [parse: 1, part1: 1, part2: 1]
  doctest(AOC2022.Day04, import: true)

  @puzzle_dir "lib/2022/04_camp_cleanup/"
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
             {2..4, 6..8},
             {2..3, 4..5},
             {5..7, 7..9},
             {2..8, 3..7},
             {6..6, 4..6},
             {2..6, 4..8}
           ]
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == 2
  end

  @tag :example
  test "part 2 example 1", %{example1: example1} do
    assert part2(example1) == 4
  end

  @tag :solution
  @tag :year2022
  @tag :day4
  test "part 1 solved", %{input: input} do
    assert part1(input) == 444
  end

  @tag :solution
  @tag :year2022
  @tag :day4
  test "part 2 solved", %{input: input} do
    assert part2(input) == 801
  end
end
