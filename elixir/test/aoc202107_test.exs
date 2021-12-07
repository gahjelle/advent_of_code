defmodule AOC2021.Day07.Test do
  @moduledoc """
  Tests for Advent of Code 2021, day 7: The Treachery of Whales
  """
  use ExUnit.Case, async: true
  require AOC
  import AOC2021.Day07, only: [parse: 1, part1: 1, part2: 1]
  doctest(AOC2021.Day07, import: true)

  @puzzle_dir "lib/2021/07_the_treachery_of_whales/"
  setup_all do
    {:ok,
     [
       example1: @puzzle_dir |> Path.join("example1.txt") |> AOC.read_text() |> parse(),
       input: @puzzle_dir |> Path.join("input.txt") |> AOC.read_text() |> parse()
     ]}
  end

  @tag :parse
  test "parse example", %{example1: example1} do
    assert example1 === [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == 37
  end

  @tag :example
  test "part 2 example 1", %{example1: example1} do
    assert part2(example1) == 168
  end

  @tag :solution
  @tag :year2021
  @tag :day7
  test "part 1 solved", %{input: input} do
    assert part1(input) == 336_040
  end

  @tag :solution
  @tag :year2021
  @tag :day7
  test "part 2 solved", %{input: input} do
    assert part2(input) == 94_813_675
  end
end
