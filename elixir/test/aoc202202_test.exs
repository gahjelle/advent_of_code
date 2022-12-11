defmodule AOC2022.Day02.Test do
  @moduledoc """
  Tests for Advent of Code 2022, day 2: Rock Paper Scissors.
  """
  use ExUnit.Case, async: true
  require AOC
  import AOC2022.Day02, only: [parse: 1, part1: 1, part2: 1]
  doctest(AOC2022.Day02, import: true)

  @puzzle_dir "lib/2022/02_rock_paper_scissors/"
  setup_all do
    {:ok,
     [
       example1: @puzzle_dir |> Path.join("example1.txt") |> AOC.read_text() |> parse(),
       input: @puzzle_dir |> Path.join("input.txt") |> AOC.read_text() |> parse()
     ]}
  end

  @tag :parse
  test "parse example", %{example1: example1} do
    assert example1 === [{:rock, :paper, ?Y}, {:paper, :rock, ?X}, {:scissors, :scissors, ?Z}]
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == 15
  end

  @tag :example
  test "part 2 example 1", %{example1: example1} do
    assert part2(example1) == 12
  end

  @tag :solution
  @tag :year2022
  @tag :day2
  test "part 1 solved", %{input: input} do
    assert part1(input) == 10_595
  end

  @tag :solution
  @tag :year2022
  @tag :day2
  test "part 2 solved", %{input: input} do
    assert part2(input) == 9_541
  end
end
