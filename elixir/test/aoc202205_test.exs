defmodule AOC2022.Day05.Test do
  @moduledoc """
  Tests for Advent of Code 2022, day 5: Supply Stacks.
  """
  use ExUnit.Case, async: true
  require AOC
  import AOC2022.Day05, only: [parse: 1, part1: 1, part2: 1]
  doctest(AOC2022.Day05, import: true)

  @puzzle_dir "lib/2022/05_supply_stacks/"
  setup_all do
    {:ok,
     [
       example1: @puzzle_dir |> Path.join("example1.txt") |> AOC.read_text() |> parse(),
       input: @puzzle_dir |> Path.join("input.txt") |> AOC.read_text() |> parse()
     ]}
  end

  @tag :parse
  test "parse example", %{example1: example1} do
    assert example1 ===
             {%{1 => [?N, ?Z], 2 => [?D, ?C, ?M], 3 => [?P]},
              [{1, 2, 1}, {3, 1, 3}, {2, 2, 1}, {1, 1, 2}]}
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == 'CMZ'
  end

  @tag :example
  test "part 2 example 1", %{example1: example1} do
    assert part2(example1) == 'MCD'
  end

  @tag :solution
  @tag :year2022
  @tag :day5
  test "part 1 solved", %{input: input} do
    assert part1(input) == 'TLNGFGMFN'
  end

  @tag :solution
  @tag :year2022
  @tag :day5
  test "part 2 solved", %{input: input} do
    assert part2(input) == 'FGLQJCMBD'
  end
end
