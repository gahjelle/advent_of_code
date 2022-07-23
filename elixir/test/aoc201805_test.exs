defmodule AOC2018.Day05.Test do
  @moduledoc """
  Tests for Advent of Code 2018, day 5: Alchemical Reduction
  """
  use ExUnit.Case, async: true
  require AOC
  import AOC2018.Day05, only: [parse: 1, part1: 1, part2: 1]
  doctest(AOC2018.Day05, import: true)

  @puzzle_dir "lib/2018/05_alchemical_reduction/"
  setup_all do
    {:ok,
     [
       example1: @puzzle_dir |> Path.join("example1.txt") |> AOC.read_text() |> parse(),
       input: @puzzle_dir |> Path.join("input.txt") |> AOC.read_text() |> parse()
     ]}
  end

  @tag :parse
  test "parse example", %{example1: example1} do
    assert example1 === 'dabAcCaCBAcCcaDA'
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == 10
  end

  @tag :example
  test "part 2 example 1", %{example1: example1} do
    assert part2(example1) == 4
  end

  @tag :solution
  @tag :year2018
  @tag :day5
  test "part 1 solved", %{input: input} do
    assert part1(input) == 9370
  end

  @tag :solution
  @tag :year2018
  @tag :day5
  test "part 2 solved", %{input: input} do
    assert part2(input) == 6390
  end
end
