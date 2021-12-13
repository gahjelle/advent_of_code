defmodule AOC2021.Day09.Test do
  @moduledoc """
  Tests for Advent of Code 2021, day 9: Smoke Basin
  """
  use ExUnit.Case, async: true
  require AOC

  alias AOC2021.Day09.HeightMap
  import AOC2021.Day09, only: [parse: 1, part1: 1, part2: 1]
  doctest(AOC2021.Day09, import: true)
  doctest(AOC2021.Day09.HeightMap, import: true)

  @puzzle_dir "lib/2021/09_smoke_basin/"
  setup_all do
    {:ok,
     [
       example1: @puzzle_dir |> Path.join("example1.txt") |> AOC.read_text() |> parse(),
       input: @puzzle_dir |> Path.join("input.txt") |> AOC.read_text() |> parse()
     ]}
  end

  @tag :parse
  test "parse example", %{example1: example1} do
    assert example1.heights |> Map.keys() |> length() == 50
    assert example1.heights[{0, 0}] == 2
    assert example1.heights[{4, 0}] == 9
    assert example1.heights[{0, 9}] == 0
    assert example1.heights[{4, 9}] == 8
    assert example1.heights[{2, 5}] == 8
    assert example1.heights |> Map.keys() == example1.positions |> MapSet.to_list()
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == 15
  end

  @tag :example
  test "part 2 example 1", %{example1: example1} do
    assert part2(example1) == 1134
  end

  @tag :solution
  @tag :year2021
  @tag :day9
  test "part 1 solved", %{input: input} do
    assert part1(input) == 462
  end

  @tag :solution
  @tag :year2021
  @tag :day9
  test "part 2 solved", %{input: input} do
    assert part2(input) == 1_397_760
  end
end
