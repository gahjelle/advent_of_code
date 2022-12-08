defmodule AOC2022.Day07.Test do
  @moduledoc """
  Tests for Advent of Code 2022, day 7: No Space Left On Device.
  """
  use ExUnit.Case, async: true
  require AOC
  import AOC2022.Day07, only: [parse: 1, part1: 1, part2: 1]
  doctest(AOC2022.Day07, import: true)

  @puzzle_dir "lib/2022/07_no_space_left_on_device/"
  setup_all do
    {:ok,
     [
       example1: @puzzle_dir |> Path.join("example1.txt") |> AOC.read_text() |> parse(),
       input: @puzzle_dir |> Path.join("input.txt") |> AOC.read_text() |> parse()
     ]}
  end

  @tag :parse
  test "parse example", %{example1: example1} do
    assert example1 === %{
             "/" => 0,
             "/a" => 0,
             "/b.txt" => 14_848_514,
             "/c.dat" => 8_504_156,
             "/d" => 0,
             "/a/e" => 0,
             "/a/f" => 29_116,
             "/a/g" => 2_557,
             "/a/h.lst" => 62_596,
             "/a/e/i" => 584,
             "/d/j" => 4_060_174,
             "/d/d.log" => 8_033_020,
             "/d/d.ext" => 5_626_152,
             "/d/k" => 7_214_296
           }
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == 95_437
  end

  @tag :example
  test "part 2 example 1", %{example1: example1} do
    assert part2(example1) == 24_933_642
  end

  @tag :solution
  @tag :year2022
  @tag :day7
  test "part 1 solved", %{input: input} do
    assert part1(input) == 1_390_824
  end

  @tag :solution
  @tag :year2022
  @tag :day7
  test "part 2 solved", %{input: input} do
    assert part2(input) == 7_490_863
  end
end
