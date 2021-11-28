defmodule AOC2020.Day02.Test do
  @moduledoc """
  Tests for Advent of Code 2020, day 2: Password Philosophy
  """
  use ExUnit.Case, async: true
  require AOC
  import AOC2020.Day02, only: [parse: 1, part1: 1, part2: 1]
  doctest(AOC2020.Day02, import: true)

  @puzzle_dir "lib/2020/02_password_philosophy/"
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
             {1, 3, ?a, 'abcde'},
             {1, 3, ?b, 'cdefg'},
             {2, 9, ?c, 'ccccccccc'}
           ]
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == 2
  end

  @tag :example
  test "part 2 example 1", %{example1: example1} do
    assert part2(example1) == 1
  end

  @tag :solution
  @tag :year2020
  @tag :day2
  test "part 1 solved", %{input: input} do
    assert part1(input) == 524
  end

  @tag :solution
  @tag :year2020
  @tag :day2
  test "part 2 solved", %{input: input} do
    assert part2(input) == 485
  end
end
