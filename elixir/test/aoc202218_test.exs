defmodule AOC2022.Day18.Test do
  @moduledoc """
  Tests for Advent of Code 2022, day 18: Boiling Boulders.
  """
  use ExUnit.Case, async: true
  require AOC
  import AOC2022.Day18, only: [parse: 1, part1: 1, part2: 1]
  doctest(AOC2022.Day18, import: true)

  @puzzle_dir "lib/2022/18_boiling_boulders/"
  setup_all do
    {:ok,
     [
       example1: @puzzle_dir |> Path.join("example1.txt") |> AOC.read_text() |> parse(),
       input: @puzzle_dir |> Path.join("input.txt") |> AOC.read_text() |> parse()
     ]}
  end

  @tag :parse
  test "parse example", %{example1: example1} do
    assert example1 ===
             MapSet.new([
               {2, 2, 2},
               {1, 2, 2},
               {3, 2, 2},
               {2, 1, 2},
               {2, 3, 2},
               {2, 2, 1},
               {2, 2, 3},
               {2, 2, 4},
               {2, 2, 6},
               {1, 2, 5},
               {3, 2, 5},
               {2, 1, 5},
               {2, 3, 5}
             ])
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == 64
  end

  @tag :example
  test "part 2 example 1", %{example1: example1} do
    assert part2(example1) == 58
  end

  @tag :solution
  @tag :year2022
  @tag :day18
  test "part 1 solved", %{input: input} do
    assert part1(input) == 3390
  end

  @tag :solution
  @tag :year2022
  @tag :day18
  test "part 2 solved", %{input: input} do
    assert part2(input) == 2058
  end
end
