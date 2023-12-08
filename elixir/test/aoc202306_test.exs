defmodule AOC2023.Day06.Test do
  @moduledoc """
  Tests for Advent of Code 2023, day 6: Wait For It.
  """
  use ExUnit.Case, async: true
  require AOC
  import AOC2023.Day06, only: [parse: 1, part1: 1, part2: 1]
  doctest(AOC2023.Day06, import: true)

  @puzzle_dir "lib/2023/06_wait_for_it/"
  setup_all do
    {:ok,
     [
       example1: @puzzle_dir |> Path.join("example1.txt") |> AOC.read_text() |> parse(),
       input: @puzzle_dir |> Path.join("input.txt") |> AOC.read_text() |> parse()
     ]}
  end

  @tag :parse
  test "parse example", %{example1: example1} do
    assert example1 === {[{7, 9}, {15, 40}, {30, 200}], {71_530, 940_200}}
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == 288
  end

  @tag :example
  test "part 2 example 1", %{example1: example1} do
    assert part2(example1) == 71_503
  end

  @tag :solution
  @tag :year2023
  @tag :day6
  test "part 1 solved", %{input: input} do
    assert part1(input) == 2_612_736
  end

  @tag :solution
  @tag :year2023
  @tag :day6
  test "part 2 solved", %{input: input} do
    assert part2(input) == 29_891_250
  end
end
