defmodule AOC2021.Day08.Test do
  @moduledoc """
  Tests for Advent of Code 2021, day 8: Seven Segment Search
  """
  use ExUnit.Case, async: true
  require AOC
  import AOC2021.Day08, only: [parse: 1, part1: 1, part2: 1]
  doctest(AOC2021.Day08, import: true)

  @puzzle_dir "lib/2021/08_seven_segment_search/"
  setup_all do
    {:ok,
     [
       example1: @puzzle_dir |> Path.join("example1.txt") |> AOC.read_text() |> parse(),
       input: @puzzle_dir |> Path.join("input.txt") |> AOC.read_text() |> parse()
     ]}
  end

  @tag :parse
  test "parse example", %{example1: {wires, output}} do
    assert wires |> hd === [
             'be',
             'abcdefg',
             'bcdefg',
             'acdefg',
             'bceg',
             'cdefg',
             'abdefg',
             'bcdef',
             'abcdf',
             'bde'
           ]

    assert output |> hd === ['abcdefg', 'bcdef', 'bcdefg', 'bceg']
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == 26
  end

  @tag :example
  test "part 2 example 1", %{example1: example1} do
    assert part2(example1) == 61_229
  end

  @tag :solution
  @tag :year2021
  @tag :day8
  test "part 1 solved", %{input: input} do
    assert part1(input) == 349
  end

  @tag :solution
  @tag :year2021
  @tag :day8
  test "part 2 solved", %{input: input} do
    assert part2(input) == 1_070_957
  end
end
