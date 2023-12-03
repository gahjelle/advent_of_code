defmodule AOC2023.Day02.Test do
  @moduledoc """
  Tests for Advent of Code 2023, day 2: Cube Conundrum.
  """
  use ExUnit.Case, async: true
  require AOC
  import AOC2023.Day02, only: [parse: 1, part1: 1, part2: 1]
  doctest(AOC2023.Day02, import: true)

  @puzzle_dir "lib/2023/02_cube_conundrum/"
  setup_all do
    {:ok,
     [
       example1: @puzzle_dir |> Path.join("example1.txt") |> AOC.read_text() |> parse(),
       input: @puzzle_dir |> Path.join("input.txt") |> AOC.read_text() |> parse()
     ]}
  end

  @tag :parse
  test "parse example", %{example1: example1} do
    assert example1 === [{4, 2, 6}, {1, 3, 4}, {20, 13, 6}, {14, 3, 15}, {6, 3, 2}]
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == 8
  end

  @tag :example
  test "part 2 example 1", %{example1: example1} do
    assert part2(example1) == 2286
  end

  @tag :solution
  @tag :year2023
  @tag :day2
  test "part 1 solved", %{input: input} do
    assert part1(input) == 2617
  end

  @tag :solution
  @tag :year2023
  @tag :day2
  test "part 2 solved", %{input: input} do
    assert part2(input) == 59_795
  end
end
