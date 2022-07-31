defmodule AOC2020.Day03.Test do
  @moduledoc """
  Tests for Advent of Code 2020, day 3: Toboggan Trajectory
  """
  use ExUnit.Case, async: true
  require AOC

  alias AOC2020.Day03.Forest
  import AOC2020.Day03, only: [parse: 1, part1: 1, part2: 1]
  doctest(AOC2020.Day03, import: true)
  doctest(AOC2020.Day03.Forest, import: true)

  @puzzle_dir "lib/2020/03_toboggan_trajectory/"
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
    #     0123
    #   0 ..## | ..##..##..##..## ...
    #   1 #... | #...#...#...#... ...
    #   2 .... | ................ ...
    #   3 .##. | .##..##..##..##. ...

    assert example1 === Forest.new(MapSet.new([{2, 0}, {3, 0}, {0, 1}, {1, 3}, {2, 3}]), 4, 4)
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == 1
  end

  @tag :example
  test "part 1 example 2", %{example2: example2} do
    assert part1(example2) == 7
  end

  @tag :example
  test "part 2 example 1", %{example1: example1} do
    # 0 * 1 * 0 * 1 * 0
    assert part2(example1) == 0
  end

  @tag :example
  test "part 2 example 2", %{example2: example2} do
    assert part2(example2) == 2 * 7 * 3 * 4 * 2
  end

  @tag :solution
  @tag :year2020
  @tag :day3
  test "part 1 solved", %{input: input} do
    assert part1(input) == 220
  end

  @tag :solution
  @tag :year2020
  @tag :day3
  test "part 2 solved", %{input: input} do
    assert part2(input) == 2_138_320_800
  end
end
