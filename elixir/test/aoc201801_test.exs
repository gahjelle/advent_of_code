defmodule AOC2018.Day01.Test do
  @moduledoc """
  Tests for Advent of Code 2018, day 1: Chronal Calibration
  """
  use ExUnit.Case, async: true
  require AOC
  import AOC2018.Day01, only: [parse: 1, part1: 1, part2: 1]

  @puzzle_dir "lib/2018/01_chronal_calibration/"
  setup_all do
    {:ok,
     [
       example1: @puzzle_dir |> Path.join("example1.txt") |> AOC.read_text() |> parse(),
       example2: @puzzle_dir |> Path.join("example2.txt") |> AOC.read_text() |> parse(),
       example3: @puzzle_dir |> Path.join("example3.txt") |> AOC.read_text() |> parse(),
       input: @puzzle_dir |> Path.join("input.txt") |> AOC.read_text() |> parse()
     ]}
  end

  @tag :parse
  test "parse example", %{example1: example1} do
    assert example1 === [1, -2, 3, 1]
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == 3
  end

  @tag :example
  test "part 2 example 1", %{example1: example1} do
    assert part2(example1) == 2
  end

  @tag :example
  test "part 2 example 2", %{example2: example2} do
    assert part2(example2) == 10
  end

  @tag :example
  test "part 2 example 3", %{example3: example3} do
    assert part2(example3) == 0
  end

  @tag :solution
  @tag :year2018
  @tag :day1
  test "part 1 solved", %{input: input} do
    assert part1(input) == 531
  end

  @tag :solution
  @tag :year2018
  @tag :day1
  test "part 2 solved", %{input: input} do
    assert part2(input) == 76_787
  end
end
