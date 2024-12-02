defmodule AOC2024.Day02.Test do
  @moduledoc """
  Tests for Advent of Code 2024, day 2: Red-Nosed Reports.
  """
  use ExUnit.Case, async: true
  require AOC
  import AOC2024.Day02, only: [parse: 1, part1: 1, part2: 1]
  doctest(AOC2024.Day02, import: true)

  @puzzle_dir "lib/2024/02_red-nosed_reports/"
  setup_all do
    {:ok,
     [
       example1: @puzzle_dir |> Path.join("example1.txt") |> AOC.read_text() |> parse(),
       input: @puzzle_dir |> Path.join("input.txt") |> AOC.read_text() |> parse()
     ]}
  end

  @tag :parse
  test "parse example", %{example1: example1} do
    assert example1 === [
             [7, 6, 4, 2, 1],
             [1, 2, 7, 8, 9],
             [9, 7, 6, 2, 1],
             [1, 3, 2, 4, 5],
             [8, 6, 4, 4, 1],
             [1, 3, 6, 7, 9]
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
  @tag :year2024
  @tag :day2
  test "part 1 solved", %{input: input} do
    assert part1(input) == 631
  end

  @tag :solution
  @tag :year2024
  @tag :day2
  test "part 2 solved", %{input: input} do
    assert part2(input) == 665
  end
end
