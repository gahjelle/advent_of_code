defmodule AOC2021.Day10.Test do
  @moduledoc """
  Tests for Advent of Code 2021, day 10: Syntax Scoring
  """
  use ExUnit.Case, async: true
  require AOC
  import AOC2021.Day10, only: [parse: 1, part1: 1, part2: 1]
  doctest(AOC2021.Day10, import: true)

  @puzzle_dir "lib/2021/10_syntax_scoring/"
  setup_all do
    {:ok,
     [
       example1: @puzzle_dir |> Path.join("example1.txt") |> AOC.read_text() |> parse(),
       #  example2: @puzzle_dir |> Path.join("example2.txt") |> AOC.read_text() |> parse(),
       input: @puzzle_dir |> Path.join("input.txt") |> AOC.read_text() |> parse()
     ]}
  end

  @tag :parse
  test "parse example", %{example1: example1} do
    assert example1 === [
             '[({(<(())[]>[[{[]{<()<>>',
             '[(()[<>])]({[<{<<[]>>(',
             '{([(<{}[<>[]}>{[]{[(<()>',
             '(((({<>}<{<{<>}{[]{[]{}',
             '[[<[([]))<([[{}[[()]]]',
             '[{[{({}]{}}([{[{{{}}([]',
             '{<[[]]>}<{[{[{[]{()[[[]',
             '[<(<(<(<{}))><([]([]()',
             '<{([([[(<>()){}]>(<<{{',
             '<{([{{}}[<[[[<>{}]]]>[]]'
           ]
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == 26_397
  end

  @tag :example
  test "part 2 example 1", %{example1: example1} do
    assert part2(example1) == 288_957
  end

  @tag :solution
  @tag :year2021
  @tag :day10
  test "part 1 solved", %{input: input} do
    assert part1(input) == 364_389
  end

  @tag :solution
  @tag :year2021
  @tag :day10
  test "part 2 solved", %{input: input} do
    assert part2(input) == 2_870_201_088
  end
end
