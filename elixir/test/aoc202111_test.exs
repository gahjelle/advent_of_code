defmodule AOC2021.Day11.Test do
  @moduledoc """
  Tests for Advent of Code 2021, day 11: Dumbo Octopus
  """
  use ExUnit.Case, async: true
  require AOC
  import AOC2021.Day11, only: [parse: 1, part1: 1, part2: 1]
  doctest(AOC2021.Day11, import: true)

  @puzzle_dir "lib/2021/11_dumbo_octopus/"
  setup_all do
    {:ok,
     [
       example1: @puzzle_dir |> Path.join("example1.txt") |> AOC.read_text() |> parse(),
       input: @puzzle_dir |> Path.join("input.txt") |> AOC.read_text() |> parse()
     ]}
  end

  @tag :parse
  test "parse example", %{example1: example1} do
    assert example1 |> Map.keys() |> length == 100
    assert example1[{0, 0}] == 5
    assert example1[{0, 9}] == 3
    assert example1[{9, 0}] == 5
    assert example1[{9, 9}] == 6
    assert example1[{4, 5}] == 8
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == 1656
  end

  @tag :example
  test "part 2 example 1", %{example1: example1} do
    assert part2(example1) == 195
  end

  @tag :solution
  @tag :year2021
  @tag :day11
  test "part 1 solved", %{input: input} do
    assert part1(input) == 1793
  end

  @tag :solution
  @tag :year2021
  @tag :day11
  test "part 2 solved", %{input: input} do
    assert part2(input) == 247
  end
end
