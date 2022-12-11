defmodule AOC2022.Day11.Test do
  @moduledoc """
  Tests for Advent of Code 2022, day 11: Monkey in the Middle.
  """
  use ExUnit.Case, async: true
  require AOC

  alias AOC2022.Day11.Monkey
  import AOC2022.Day11, only: [parse: 1, part1: 1, part2: 1]
  doctest(AOC2022.Day11, import: true)
  doctest(AOC2022.Day11.Monkey, import: true)

  @puzzle_dir "lib/2022/11_monkey_in_the_middle/"
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
             {%{
                0 => Monkey.new(operation: {:mul, 19}, test: 23, to_true: 2, to_false: 3),
                1 => Monkey.new(operation: {:add, 6}, test: 19, to_true: 2, to_false: 0),
                2 => Monkey.new(operation: {:pow, 2}, test: 13, to_true: 1, to_false: 3),
                3 => Monkey.new(operation: {:add, 3}, test: 17, to_true: 0, to_false: 1)
              }, %{0 => [79, 98], 1 => [54, 65, 75, 74], 2 => [79, 60, 97], 3 => [74]}}
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == 10_605
  end

  @tag :example
  test "part 2 example 1", %{example1: example1} do
    assert part2(example1) == 2_713_310_158
  end

  @tag :solution
  @tag :year2022
  @tag :day11
  test "part 1 solved", %{input: input} do
    assert part1(input) == 117_624
  end

  @tag :solution
  @tag :year2022
  @tag :day11
  test "part 2 solved", %{input: input} do
    assert part2(input) == 16_792_940_265
  end
end
