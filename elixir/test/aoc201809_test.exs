defmodule AOC2018.Day09.Test do
  @moduledoc """
  Tests for Advent of Code 2018, day 9: Marble Mania.
  """
  use ExUnit.Case, async: true
  require AOC
  import AOC2018.Day09, only: [parse: 1, part1: 1, part2: 1]
  doctest(AOC2018.Day09, import: true)
  doctest(AOC2018.Day09.CircularList, import: true)

  @puzzle_dir "lib/2018/09_marble_mania/"
  setup_all do
    {:ok,
     [
       example1: @puzzle_dir |> Path.join("example1.txt") |> AOC.read_text() |> parse(),
       example2: @puzzle_dir |> Path.join("example2.txt") |> AOC.read_text() |> parse(),
       example3: @puzzle_dir |> Path.join("example3.txt") |> AOC.read_text() |> parse(),
       example4: @puzzle_dir |> Path.join("example4.txt") |> AOC.read_text() |> parse(),
       example5: @puzzle_dir |> Path.join("example5.txt") |> AOC.read_text() |> parse(),
       example6: @puzzle_dir |> Path.join("example6.txt") |> AOC.read_text() |> parse(),
       input: @puzzle_dir |> Path.join("input.txt") |> AOC.read_text() |> parse()
     ]}
  end

  @tag :parse
  test "parse example", %{example1: example1} do
    assert example1 === {9, 25}
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == 32
  end

  @tag :example
  test "part 1 example 2", %{example2: example2} do
    assert part1(example2) == 8_317
  end

  @tag :example
  test "part 1 example 3", %{example3: example3} do
    assert part1(example3) == 146_373
  end

  @tag :example
  test "part 1 example 4", %{example4: example4} do
    assert part1(example4) == 2_764
  end

  @tag :example
  test "part 1 example 5", %{example5: example5} do
    assert part1(example5) == 54_718
  end

  @tag :example
  test "part 1 example 6", %{example6: example6} do
    assert part1(example6) == 37_305
  end

  @tag :example
  test "part 2 example 1", %{example1: example1} do
    assert part2(example1) == 22_563
  end

  @tag :example
  test "part 2 example 2", %{example2: example2} do
    assert part2(example2) == 74_765_078
  end

  @tag :solution
  @tag :year2018
  @tag :day9
  test "part 1 solved", %{input: input} do
    assert part1(input) == 388_024
  end

  @tag :solution
  @tag :year2018
  @tag :day9
  test "part 2 solved", %{input: input} do
    assert part2(input) == 3_180_929_875
  end
end
