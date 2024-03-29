defmodule AOC2015.Day04.Test do
  @moduledoc """
  Tests for Advent of Code 2015, day 4: The Ideal Stocking Stuffer
  """
  use ExUnit.Case, async: true
  require AOC
  import AOC2015.Day04, only: [parse: 1, part1: 1, part1: 2, part2: 1, part2: 2]
  doctest(AOC2015.Day04, import: true)

  @puzzle_dir "lib/2015/04_the_ideal_stocking_stuffer/"
  setup_all do
    {:ok,
     [
       example1: @puzzle_dir |> Path.join("example1.txt") |> AOC.read_text() |> parse(),
       example2: @puzzle_dir |> Path.join("example2.txt") |> AOC.read_text() |> parse(),
       input: @puzzle_dir |> Path.join("input.txt") |> AOC.read_text() |> parse()
     ]}
  end

  @tag :parse
  test "parse example", %{example1: example1} do
    assert example1 === "abcdef"
  end

  @tag :example
  test "part 1 example 1 short", %{example1: example1} do
    assert part1(example1, "00") == 298
  end

  @tag :slow
  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == 609_043
  end

  @tag :slow
  @tag :example
  test "part 1 example 2", %{example2: example2} do
    assert part1(example2) == 1_048_970
  end

  @tag :example
  test "part 2 example 2 short", %{example2: example2} do
    assert part2(example2, "000") == 6982
  end

  @tag :solution
  @tag :year2015
  @tag :day4
  test "part 1 solved", %{input: input} do
    assert part1(input) == 117_946
  end

  @tag :solution
  @tag :year2015
  @tag :day4
  test "part 2 solved", %{input: input} do
    assert part2(input) == 3_938_038
  end
end
