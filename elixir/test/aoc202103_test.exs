defmodule AOC2021.Day03.Test do
  @moduledoc """
  Tests for Advent of Code 2021, day 3: Binary Diagnostic
  """
  use ExUnit.Case, async: true
  require AOC
  import AOC2021.Day03, only: [parse: 1, part1: 1, part2: 1]
  doctest(AOC2021.Day03, import: true)

  @puzzle_dir "lib/2021/03_binary_diagnostic/"
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
             [0, 0, 1, 0, 0],
             [1, 1, 1, 1, 0],
             [1, 0, 1, 1, 0],
             [1, 0, 1, 1, 1],
             [1, 0, 1, 0, 1],
             [0, 1, 1, 1, 1],
             [0, 0, 1, 1, 1],
             [1, 1, 1, 0, 0],
             [1, 0, 0, 0, 0],
             [1, 1, 0, 0, 1],
             [0, 0, 0, 1, 0],
             [0, 1, 0, 1, 0]
           ]
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == 198
  end

  @tag :example
  test "part 2 example 1", %{example1: example1} do
    assert part2(example1) == 230
  end

  @tag :solution
  @tag :year2021
  @tag :day3
  test "part 1 solved", %{input: input} do
    assert part1(input) == 2_250_414
  end

  @tag :solution
  @tag :year2021
  @tag :day3
  test "part 2 solved", %{input: input} do
    assert part2(input) == 6_085_575
  end
end
