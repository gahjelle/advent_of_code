defmodule AOC2021.Day17.Test do
  @moduledoc """
  Tests for Advent of Code 2021, day 17: Trick Shot
  """
  use ExUnit.Case, async: true
  require AOC
  import AOC2021.Day17, only: [parse: 1, part1: 1, part2: 1]
  doctest(AOC2021.Day17, import: true)

  @puzzle_dir "lib/2021/17_trick_shot/"
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
    assert example1 === {20..30, -10..-5}
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == 45
  end

  @tag :example
  test "part 1 example 2", %{example2: example2} do
    assert part1(example2) == 15
  end

  @tag :example
  test "part 2 example 1", %{example1: example1} do
    assert part2(example1) == 112
  end

  @tag :example
  test "part 2 example 2", %{example2: example2} do
    assert part2(example2) == 10
  end

  @tag :solution
  @tag :year2021
  @tag :day17
  test "part 1 solved", %{input: input} do
    assert part1(input) == 25_200
  end

  @tag :solution
  @tag :year2021
  @tag :day17
  test "part 2 solved", %{input: input} do
    assert part2(input) == 3012
  end
end
