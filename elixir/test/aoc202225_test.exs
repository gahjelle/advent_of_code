defmodule AOC2022.Day25.Test do
  @moduledoc """
  Tests for Advent of Code 2022, day 25: Full of Hot Air.
  """
  use ExUnit.Case, async: true
  require AOC
  import AOC2022.Day25, only: [parse: 1, part1: 1, part2: 1]
  doctest(AOC2022.Day25, import: true)

  @puzzle_dir "lib/2022/25_full_of_hot_air/"
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
             "1=-0-2",
             "12111",
             "2=0=",
             "21",
             "2=01",
             "111",
             "20012",
             "112",
             "1=-1=",
             "1-12",
             "12",
             "1=",
             "122"
           ]
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == "2=-1=0"
  end

  @tag :solution
  @tag :year2022
  @tag :day25
  test "part 1 solved", %{input: input} do
    assert part1(input) == "2=01-0-2-0=-0==-1=01"
  end
end
