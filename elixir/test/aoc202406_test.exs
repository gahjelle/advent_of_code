defmodule AOC2024.Day06.Test do
  @moduledoc """
  Tests for Advent of Code 2024, day 6: Guard Gallivant.
  """
  use ExUnit.Case, async: true
  require AOC
  import AOC2024.Day06, only: [parse: 1, part1: 1, part2: 1]
  doctest(AOC2024.Day06, import: true)

  @puzzle_dir "lib/2024/06_guard_gallivant/"
  setup_all do
    {:ok,
     [
       example1: @puzzle_dir |> Path.join("example1.txt") |> AOC.read_text() |> parse(),
       input: @puzzle_dir |> Path.join("input.txt") |> AOC.read_text() |> parse()
     ]}
  end

  @tag :parse
  test "parse example", %{example1: example1} do
    {grid, start} = example1

    assert Map.filter(grid, fn {_, char} -> char != "." end) === %{
             {0, 4} => "#",
             {1, 9} => "#",
             {3, 2} => "#",
             {4, 7} => "#",
             {6, 1} => "#",
             {7, 8} => "#",
             {8, 0} => "#",
             {9, 6} => "#"
           }

    assert start == {6, 4}
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == 41
  end

  @tag :example
  test "part 2 example 1", %{example1: example1} do
    assert part2(example1) == 6
  end

  @tag :solution
  @tag :year2024
  @tag :day6
  test "part 1 solved", %{input: input} do
    assert part1(input) == 4883
  end

  @tag :slow
  @tag :solution
  @tag :year2024
  @tag :day6
  test "part 2 solved", %{input: input} do
    assert part2(input) == 1655
  end
end
