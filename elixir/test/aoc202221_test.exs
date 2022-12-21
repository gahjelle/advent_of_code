defmodule AOC2022.Day21.Test do
  @moduledoc """
  Tests for Advent of Code 2022, day 21: Monkey Math.
  """
  use ExUnit.Case, async: true
  require AOC
  import AOC2022.Day21, only: [parse: 1, part1: 1, part2: 1]
  doctest(AOC2022.Day21, import: true)

  @puzzle_dir "lib/2022/21_monkey_math/"
  setup_all do
    {:ok,
     [
       example1: @puzzle_dir |> Path.join("example1.txt") |> AOC.read_text() |> parse(),
       input: @puzzle_dir |> Path.join("input.txt") |> AOC.read_text() |> parse()
     ]}
  end

  @tag :parse
  test "parse example", %{example1: example1} do
    assert example1 === {
             %{
               "dbpl" => 5,
               "zczc" => 2,
               "dvpt" => 3,
               "lfqf" => 4,
               "humn" => 5,
               "ljgn" => 2,
               "sllz" => 4,
               "hmdt" => 32
             },
             %{
               "root" => {:add, {"pppw", "sjmn"}},
               "cczh" => {:add, {"sllz", "lgvd"}},
               "ptdq" => {:sub, {"humn", "dvpt"}},
               "sjmn" => {:mul, {"drzm", "dbpl"}},
               "pppw" => {:div, {"cczh", "lfqf"}},
               "lgvd" => {:mul, {"ljgn", "ptdq"}},
               "drzm" => {:sub, {"hmdt", "zczc"}}
             }
           }
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == 152
  end

  @tag :example
  test "part 2 example 1", %{example1: example1} do
    assert part2(example1) == 301
  end

  @tag :solution
  @tag :year2022
  @tag :day21
  test "part 1 solved", %{input: input} do
    assert part1(input) == 21_208_142_603_224
  end

  @tag :solution
  @tag :year2022
  @tag :day21
  test "part 2 solved", %{input: input} do
    assert part2(input) == 3_882_224_466_191
  end
end
