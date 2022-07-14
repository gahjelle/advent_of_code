defmodule AOC2019.Day02.Test do
  @moduledoc """
  Tests for Advent of Code 2019, day 2: 1202 Program Alarm
  """
  use ExUnit.Case, async: true
  require AOC
  import AOC2019.Day02, only: [parse: 1, part1: 1, part2: 1]
  doctest(AOC2019.Day02, import: true)

  @puzzle_dir "lib/2019/02_1202_program_alarm/"
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
             0 => 1,
             1 => 9,
             2 => 10,
             3 => 3,
             4 => 2,
             5 => 3,
             6 => 11,
             7 => 0,
             8 => 99,
             9 => 30,
             10 => 40,
             11 => 50
           }
  end

  @tag :solution
  @tag :year2019
  @tag :day2
  test "part 1 solved", %{input: input} do
    assert part1(input) == 3_562_624
  end

  @tag :solution
  @tag :year2019
  @tag :day2
  test "part 2 solved", %{input: input} do
    assert part2(input) == 8298
  end
end
