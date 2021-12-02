defmodule AOC2021.Day02.Test do
  @moduledoc """
  Tests for Advent of Code 2021, day 2: Dive!
  """
  use ExUnit.Case, async: true
  require AOC
  import AOC2021.Day02, only: [parse: 1, part1: 1, part2: 1]
  doctest(AOC2021.Day02, import: true)

  @puzzle_dir "lib/2021/02_dive/"
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
             {:forward, 5},
             {:down, 5},
             {:forward, 8},
             {:up, 3},
             {:down, 8},
             {:forward, 2}
           ]
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == 150
  end

  @tag :example
  test "part 2 example 1", %{example1: example1} do
    assert part2(example1) == 900
  end

  @tag :solution
  @tag :year2021
  @tag :day2
  test "part 1 solved", %{input: input} do
    assert part1(input) == 1_690_020
  end

  @tag :solution
  @tag :year2021
  @tag :day2
  test "part 2 solved", %{input: input} do
    assert part2(input) == 1_408_487_760
  end
end
