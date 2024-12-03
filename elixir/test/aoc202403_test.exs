defmodule AOC2024.Day03.Test do
  @moduledoc """
  Tests for Advent of Code 2024, day 3: Mull it Over.
  """
  use ExUnit.Case, async: true
  require AOC
  import AOC2024.Day03, only: [parse: 1, part1: 1, part2: 1]
  doctest(AOC2024.Day03, import: true)

  @puzzle_dir "lib/2024/03_mull_it_over/"
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
             "xmul(2,4)&mul[3,7]!^",
             "_mul(5,5)+mul(32,64](mul(11,8)un",
             "?mul(8,5))"
           ]
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == 161
  end

  @tag :example
  test "part 2 example 1", %{example1: example1} do
    assert part2(example1) == 48
  end

  @tag :solution
  @tag :year2024
  @tag :day3
  test "part 1 solved", %{input: input} do
    assert part1(input) == 166_630_675
  end

  @tag :solution
  @tag :year2024
  @tag :day3
  test "part 2 solved", %{input: input} do
    assert part2(input) == 93_465_710
  end
end
