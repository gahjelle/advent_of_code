defmodule AOC2022.Day09.Test do
  @moduledoc """
  Tests for Advent of Code 2022, day 9: Rope Bridge.
  """
  use ExUnit.Case, async: true
  require AOC
  import AOC2022.Day09, only: [parse: 1, part1: 1, part2: 1]
  doctest(AOC2022.Day09, import: true)

  @puzzle_dir "lib/2022/09_rope_bridge/"
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
             :right,
             :right,
             :right,
             :right,
             :up,
             :up,
             :up,
             :up,
             :left,
             :left,
             :left,
             :down,
             :right,
             :right,
             :right,
             :right,
             :down,
             :left,
             :left,
             :left,
             :left,
             :left,
             :right,
             :right
           ]
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == 13
  end

  @tag :example
  test "part 1 example 2", %{example2: example2} do
    assert part1(example2) == 88
  end

  @tag :example
  test "part 2 example 1", %{example1: example1} do
    assert part2(example1) == 1
  end

  @tag :example
  test "part 2 example 2", %{example2: example2} do
    assert part2(example2) == 36
  end

  @tag :solution
  @tag :year2022
  @tag :day9
  test "part 1 solved", %{input: input} do
    assert part1(input) == 6_284
  end

  @tag :solution
  @tag :year2022
  @tag :day9
  test "part 2 solved", %{input: input} do
    assert part2(input) == 2_661
  end
end
