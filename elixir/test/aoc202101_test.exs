defmodule AOC2021.Day01.Test do
  @moduledoc """
  Tests for Advent of Code 2021, day 1: Sonar Sweep
  """
  use ExUnit.Case, async: true
  require AOC
  import AOC2021.Day01, only: [parse: 1, part1: 1, part2: 1]
  doctest(AOC2021.Day01, import: true)

  @puzzle_dir "lib/2021/01_sonar_sweep/"
  setup_all do
    {:ok,
     [
       example1: @puzzle_dir |> Path.join("example1.txt") |> AOC.read_text() |> parse(),
       input: @puzzle_dir |> Path.join("input.txt") |> AOC.read_text() |> parse()
     ]}
  end

  @tag :parse
  test "parse example", %{example1: example1} do
    assert example1 === [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == 7
  end

  @tag :example
  test "part 2 example 1", %{example1: example1} do
    assert part2(example1) == 5
  end

  @tag :solution
  @tag :year2021
  @tag :day1
  test "part 1 solved", %{input: input} do
    assert part1(input) == 1475
  end

  @tag :solution
  @tag :year2021
  @tag :day1
  test "part 2 solved", %{input: input} do
    assert part2(input) == 1516
  end
end
