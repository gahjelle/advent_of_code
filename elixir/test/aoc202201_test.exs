defmodule AOC2022.Day01.Test do
  @moduledoc """
  Tests for Advent of Code 2022, day 1: Calorie Counting
  """
  use ExUnit.Case, async: true
  require AOC
  import AOC2022.Day01, only: [parse: 1, part1: 1, part2: 1]
  doctest(AOC2022.Day01, import: true)

  @puzzle_dir "lib/2022/01_calorie_counting/"
  setup_all do
    {:ok,
     [
       example1: @puzzle_dir |> Path.join("example1.txt") |> AOC.read_text() |> parse(),
       input: @puzzle_dir |> Path.join("input.txt") |> AOC.read_text() |> parse()
     ]}
  end

  @tag :parse
  test "parse example", %{example1: example1} do
    assert example1 === [[1000, 2000, 3000], [4000], [5000, 6000], [7000, 8000, 9000], [10_000]]
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == 24_000
  end

  @tag :example
  test "part 2 example 1", %{example1: example1} do
    assert part2(example1) == 45_000
  end

  @tag :solution
  @tag :year2022
  @tag :day1
  test "part 1 solved", %{input: input} do
    assert part1(input) == 70_698
  end

  @tag :solution
  @tag :year2022
  @tag :day1
  test "part 2 solved", %{input: input} do
    assert part2(input) == 206_643
  end
end
