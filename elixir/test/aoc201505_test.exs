defmodule AOC2015.Day05.Test do
  @moduledoc """
  Tests for Advent of Code 2015, day 5: Doesn't He Have Intern-Elves For This?
  """
  use ExUnit.Case, async: true
  require AOC

  import AOC2015.Day05, only: [parse: 1, part1: 1, part2: 1]
  @puzzle_dir "lib/2015/05_doesnt_he_have_intern-elves_for_this/"

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
    assert example1 === [
             'ugknbfddgicrmopn',
             'aaa',
             'jchzalrnumimnmhp',
             'haegwjzuvuyypxyu',
             'dvszwmarrgswjxmb'
           ]
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == 2
  end

  @tag :example
  test "part 2 example 2", %{example2: example2} do
    assert part2(example2) == 2
  end

  @tag :solution
  @tag :year2015
  @tag :day5
  test "part 1 solved", %{input: input} do
    assert part1(input) == 236
  end

  @tag :solution
  @tag :year2015
  @tag :day5
  test "part 2 solved", %{input: input} do
    assert part2(input) == 51
  end
end
