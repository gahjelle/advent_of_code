defmodule AOC2018.Day04.Test do
  @moduledoc """
  Tests for Advent of Code 2018, day 4: Repose Record
  """
  use ExUnit.Case, async: true
  require AOC
  import AOC2018.Day04, only: [parse: 1, part1: 1, part2: 1]
  doctest(AOC2018.Day04, import: true)

  @puzzle_dir "lib/2018/04_repose_record/"
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
             10 => Enum.concat([24..28, 5..24, 30..54]),
             99 => Enum.concat([45..54, 36..45, 40..49])
           }
  end

  @tag :parse
  test "parse unsorted", %{example1: unsorted, example2: sorted} do
    assert unsorted === sorted
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == 240
  end

  @tag :example
  test "part 2 example 1", %{example1: example1} do
    assert part2(example1) == 4455
  end

  @tag :example
  test "part 1 example 2", %{example2: example2} do
    assert part1(example2) == 240
  end

  @tag :example
  test "part 2 example 2", %{example2: example2} do
    assert part2(example2) == 4455
  end

  @tag :solution
  @tag :year2018
  @tag :day4
  test "part 1 solved", %{input: input} do
    assert part1(input) == 39_584
  end

  @tag :solution
  @tag :year2018
  @tag :day4
  test "part 2 solved", %{input: input} do
    assert part2(input) == 55_053
  end
end
