defmodule AOC2019.Day01.Test do
  @moduledoc """
  Tests for Advent of Code 2019, day 1: The Tyranny of the Rocket Equation
  """
  use ExUnit.Case, async: true
  require AOC

  import AOC2019.Day01, only: [parse: 1, part1: 1, part2: 1]
  @puzzle_dir "lib/2019/01_the_tyranny_of_the_rocket_equation/"

  setup_all do
    {:ok,
     [
       example1: @puzzle_dir |> Path.join("example1.txt") |> AOC.read_text() |> parse(),
       input: @puzzle_dir |> Path.join("input.txt") |> AOC.read_text() |> parse()
     ]}
  end

  @tag :parse
  test "parse example", %{example1: example1} do
    assert example1 === [12, 14, 1969, 100_756]
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == 2 + 2 + 654 + 33_583
  end

  @tag :example
  test "part 2 example 1", %{example1: example1} do
    assert part2(example1) == 2 + 2 + 966 + 50_346
  end

  @tag :solution
  @tag :year2019
  @tag :day1
  test "part 1 solved", %{input: input} do
    assert part1(input) == 3_550_236
  end

  @tag :solution
  @tag :year2019
  @tag :day1
  test "part 2 solved", %{input: input} do
    assert part2(input) == 5_322_455
  end
end
