defmodule AOC2017.Day01.Test do
  @moduledoc """
  Tests for Advent of Code 2017, day 1: Inverse Captcha
  """
  use ExUnit.Case, async: true
  require AOC
  import AOC2017.Day01, only: [parse: 1, part1: 1, part2: 1]
  doctest(AOC2017.Day01, import: true)

  @puzzle_dir "lib/2017/01_inverse_captcha/"
  setup_all do
    {:ok,
     [
       example4: @puzzle_dir |> Path.join("example4.txt") |> AOC.read_text() |> parse(),
       example7: @puzzle_dir |> Path.join("example7.txt") |> AOC.read_text() |> parse(),
       example9: @puzzle_dir |> Path.join("example9.txt") |> AOC.read_text() |> parse(),
       input: @puzzle_dir |> Path.join("input.txt") |> AOC.read_text() |> parse()
     ]}
  end

  @tag :parse
  test "parse example", %{example7: example7} do
    assert example7 === [1, 2, 3, 4, 2, 5]
  end

  @tag :example
  test "part 1 example 4", %{example4: example4} do
    assert part1(example4) == 9
  end

  @tag :example
  test "part 2 example 9", %{example9: example9} do
    assert part2(example9) == 4
  end

  @tag :solution
  @tag :year2017
  @tag :day1
  test "part 1 solved", %{input: input} do
    assert part1(input) == 1141
  end

  @tag :solution
  @tag :year2017
  @tag :day1
  test "part 2 solved", %{input: input} do
    assert part2(input) == 950
  end
end
