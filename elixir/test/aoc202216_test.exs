defmodule AOC2022.Day16.Test do
  @moduledoc """
  Tests for Advent of Code 2022, day 16: Proboscidea Volcanium.
  """
  use ExUnit.Case, async: true
  require AOC
  import AOC2022.Day16, only: [parse: 1, part1: 1, part2: 1]
  doctest(AOC2022.Day16, import: true)

  @puzzle_dir "lib/2022/16_proboscidea_volcanium/"
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
    assert example1 === %{
             "AA" => {0, ["DD", "II", "BB"]},
             "BB" => {13, ["CC", "AA"]},
             "CC" => {2, ["DD", "BB"]},
             "DD" => {20, ["CC", "AA", "EE"]},
             "EE" => {3, ["FF", "DD"]},
             "FF" => {0, ["EE", "GG"]},
             "GG" => {0, ["FF", "HH"]},
             "HH" => {22, ["GG"]},
             "II" => {0, ["AA", "JJ"]},
             "JJ" => {21, ["II"]}
           }
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == 1651
  end

  @tag :example
  test "part 2 example 1", %{example1: example1} do
    assert part2(example1) == 1707
  end

  @tag :solution
  @tag :year2022
  @tag :day16
  test "part 1 solved", %{input: input} do
    assert part1(input) == 1716
  end

  @tag :solution
  @tag :year2022
  @tag :day16
  test "part 2 solved", %{input: input} do
    assert part2(input) == 2504
  end
end
