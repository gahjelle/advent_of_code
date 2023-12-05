defmodule AOC2023.Day04.Test do
  @moduledoc """
  Tests for Advent of Code 2023, day 4: Scratchcards.
  """
  use ExUnit.Case, async: true
  require AOC
  import AOC2023.Day04, only: [parse: 1, part1: 1, part2: 1]
  doctest(AOC2023.Day04, import: true)

  @puzzle_dir "lib/2023/04_scratchcards/"
  setup_all do
    {:ok,
     [
       example1: @puzzle_dir |> Path.join("example1.txt") |> AOC.read_text() |> parse(),
       input: @puzzle_dir |> Path.join("input.txt") |> AOC.read_text() |> parse()
     ]}
  end

  @tag :parse
  test "parse example", %{example1: example1} do
    assert example1 === [4, 2, 2, 1, 0, 0]
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == 13
  end

  @tag :example
  test "part 2 example 1", %{example1: example1} do
    assert part2(example1) == 30
  end

  @tag :solution
  @tag :year2023
  @tag :day4
  test "part 1 solved", %{input: input} do
    assert part1(input) == 24_160
  end

  @tag :solution
  @tag :year2023
  @tag :day4
  test "part 2 solved", %{input: input} do
    assert part2(input) == 5_659_035
  end
end
