defmodule AOC2022.Day08.Test do
  @moduledoc """
  Tests for Advent of Code 2022, day 8: Treetop Tree House.
  """
  use ExUnit.Case, async: true
  require AOC
  import AOC2022.Day08, only: [parse: 1, part1: 1, part2: 1]
  doctest(AOC2022.Day08, import: true)

  @puzzle_dir "lib/2022/08_treetop_tree_house/"
  setup_all do
    {:ok,
     [
       example1: @puzzle_dir |> Path.join("example1.txt") |> AOC.read_text() |> parse(),
       input: @puzzle_dir |> Path.join("input.txt") |> AOC.read_text() |> parse()
     ]}
  end

  @tag :parse
  test "parse example", %{example1: example1} do
    assert example1 === %{
             {0, 0} => 3,
             {0, 1} => 0,
             {0, 2} => 3,
             {0, 3} => 7,
             {0, 4} => 3,
             {1, 0} => 2,
             {1, 1} => 5,
             {1, 2} => 5,
             {1, 3} => 1,
             {1, 4} => 2,
             {2, 0} => 6,
             {2, 1} => 5,
             {2, 2} => 3,
             {2, 3} => 3,
             {2, 4} => 2,
             {3, 0} => 3,
             {3, 1} => 3,
             {3, 2} => 5,
             {3, 3} => 4,
             {3, 4} => 9,
             {4, 0} => 3,
             {4, 1} => 5,
             {4, 2} => 3,
             {4, 3} => 9,
             {4, 4} => 0
           }
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == 21
  end

  @tag :example
  test "part 2 example 1", %{example1: example1} do
    assert part2(example1) == 8
  end

  @tag :solution
  @tag :year2022
  @tag :day8
  test "part 1 solved", %{input: input} do
    assert part1(input) == 1700
  end

  @tag :solution
  @tag :year2022
  @tag :day8
  test "part 2 solved", %{input: input} do
    assert part2(input) == 470_596
  end
end
