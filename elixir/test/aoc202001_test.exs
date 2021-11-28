defmodule AOC2020.Day01.Test do
  @moduledoc """
  Tests for Advent of Code 2020, day 1: Report Repair
  """
  use ExUnit.Case, async: true
  require AOC

  import AOC2020.Day01, only: [parse: 1, part1: 1, part2: 1]
  @puzzle_dir "lib/2020/01_report_repair/"

  setup_all do
    {:ok,
     [
       example1: @puzzle_dir |> Path.join("example1.txt") |> AOC.read_text() |> parse(),
       input: @puzzle_dir |> Path.join("input.txt") |> AOC.read_text() |> parse()
     ]}
  end

  @tag :parse
  test "parse example", %{example1: example1} do
    assert example1 === MapSet.new([1721, 979, 366, 299, 675, 1456])
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == 514_579
  end

  @tag :example
  test "part 2 example 1", %{example1: example1} do
    assert part2(example1) == 241_861_950
  end

  @tag :solution
  @tag :year2020
  @tag :day1
  test "part 1 solved", %{input: input} do
    assert part1(input) == 744_475
  end

  @tag :solution
  @tag :year2020
  @tag :day1
  test "part 2 solved", %{input: input} do
    assert part2(input) == 70_276_940
  end
end
