defmodule AOC2024.Day10.Test do
  @moduledoc """
  Tests for Advent of Code 2024, day 10: Hoof It.
  """
  use ExUnit.Case, async: true
  require AOC
  import AOC2024.Day10, only: [parse: 1, part1: 1, part2: 1]
  doctest(AOC2024.Day10, import: true)

  @puzzle_dir "lib/2024/10_hoof_it/"
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
    assert example1 === %{
             {0, 0} => 0,
             {0, 1} => 1,
             {0, 2} => 2,
             {0, 3} => 3,
             {1, 0} => 1,
             {1, 1} => 2,
             {1, 2} => 3,
             {1, 3} => 4,
             {2, 0} => 8,
             {2, 1} => 7,
             {2, 2} => 6,
             {2, 3} => 5,
             {3, 0} => 9,
             {3, 1} => 8,
             {3, 2} => 7,
             {3, 3} => 6
           }
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == 1
  end

  @tag :example
  test "part 2 example 1", %{example1: example1} do
    assert part2(example1) == 16
  end

  @tag :example
  test "part 1 example 2", %{example2: example2} do
    assert part1(example2) == 36
  end

  @tag :example
  test "part 2 example 2", %{example2: example2} do
    assert part2(example2) == 81
  end

  @tag :solution
  @tag :year2024
  @tag :day10
  test "part 1 solved", %{input: input} do
    assert part1(input) == 811
  end

  @tag :solution
  @tag :year2024
  @tag :day10
  test "part 2 solved", %{input: input} do
    assert part2(input) == 1794
  end
end
