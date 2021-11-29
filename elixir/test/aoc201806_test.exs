defmodule AOC2018.Day06.Test do
  @moduledoc """
  Tests for Advent of Code 2018, day 6: Chronal Coordinates
  """
  use ExUnit.Case, async: true
  require AOC
  import AOC2018.Day06, only: [parse: 1, part1: 1, part2: 1, part2: 2]
  doctest(AOC2018.Day06, import: true)

  @puzzle_dir "lib/2018/06_chronal_coordinates/"
  setup_all do
    {:ok,
     [
       example1: @puzzle_dir |> Path.join("example1.txt") |> AOC.read_text() |> parse(),
       input: @puzzle_dir |> Path.join("input.txt") |> AOC.read_text() |> parse()
     ]}
  end

  @tag :parse
  test "parse example", %{example1: example1} do
    assert example1 === [{1, 1}, {1, 6}, {8, 3}, {3, 4}, {5, 5}, {8, 9}]
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == 17
  end

  @tag :example
  test "part 2 example 1", %{example1: example1} do
    assert part2(example1, 32) == 16
  end

  @tag :solution
  @tag :year2018
  @tag :day6
  test "part 1 solved", %{input: input} do
    assert part1(input) == 3909
  end

  @tag :solution
  @tag :year2018
  @tag :day6
  test "part 2 solved", %{input: input} do
    assert part2(input) == 36_238
  end
end
