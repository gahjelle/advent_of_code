defmodule AOC2024.Day01.Test do
  @moduledoc """
  Tests for Advent of Code 2024, day 1: Historian Hysteria.
  """
  use ExUnit.Case, async: true
  require AOC
  import AOC2024.Day01, only: [parse: 1, part1: 1, part2: 1]
  doctest(AOC2024.Day01, import: true)

  @puzzle_dir "lib/2024/01_historian_hysteria/"
  setup_all do
    {:ok,
     [
       example1: @puzzle_dir |> Path.join("example1.txt") |> AOC.read_text() |> parse(),
       input: @puzzle_dir |> Path.join("input.txt") |> AOC.read_text() |> parse()
     ]}
  end

  @tag :parse
  test "parse example", %{example1: example1} do
    assert example1 === {[3, 4, 2, 1, 3, 3], [4, 3, 5, 3, 9, 3]}
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == 11
  end

  @tag :example
  test "part 2 example 1", %{example1: example1} do
    assert part2(example1) == 31
  end

  @tag :solution
  @tag :year2024
  @tag :day1
  test "part 1 solved", %{input: input} do
    assert part1(input) == 2_430_334
  end

  @tag :solution
  @tag :year2024
  @tag :day1
  test "part 2 solved", %{input: input} do
    assert part2(input) == 28_786_472
  end
end
