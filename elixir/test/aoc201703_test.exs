defmodule AOC2017.Day03.Test do
  @moduledoc """
  Tests for Advent of Code 2017, day 3: Spiral Memory
  """
  use ExUnit.Case, async: true
  require AOC
  import AOC2017.Day03, only: [parse: 1, part1: 1, part2: 1]
  doctest(AOC2017.Day03, import: true)

  @puzzle_dir "lib/2017/03_spiral_memory/"
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
    assert example1 === 23
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == 2
  end

  @tag :example
  test "part 1 example 2", %{example2: example2} do
    assert part1(example2) == 31
  end

  @tag :example
  test "part 2 example 1", %{example1: example1} do
    assert part2(example1) == 25
  end

  @tag :example
  test "part 2 example 2", %{example2: example2} do
    assert part2(example2) == 1968
  end

  @tag :solution
  @tag :year2017
  @tag :day3
  test "part 1 solved", %{input: input} do
    assert part1(input) == 419
  end

  @tag :solution
  @tag :year2017
  @tag :day3
  test "part 2 solved", %{input: input} do
    assert part2(input) == 295_229
  end
end
