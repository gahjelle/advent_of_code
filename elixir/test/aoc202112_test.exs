defmodule AOC2021.Day12.Test do
  @moduledoc """
  Tests for Advent of Code 2021, day 12: Passage Pathing
  """
  use ExUnit.Case, async: true
  require AOC
  import AOC2021.Day12, only: [parse: 1, part1: 1, part2: 1]
  doctest(AOC2021.Day12, import: true)

  @puzzle_dir "lib/2021/12_passage_pathing/"
  setup_all do
    {:ok,
     [
       example1: @puzzle_dir |> Path.join("example1.txt") |> AOC.read_text() |> parse(),
       example2: @puzzle_dir |> Path.join("example2.txt") |> AOC.read_text() |> parse(),
       example3: @puzzle_dir |> Path.join("example3.txt") |> AOC.read_text() |> parse(),
       input: @puzzle_dir |> Path.join("input.txt") |> AOC.read_text() |> parse()
     ]}
  end

  @tag :parse
  test "parse example", %{example1: example1} do
    assert example1 === %{
             "start" => ["b", "A"],
             "A" => ["end", "b", "c"],
             "b" => ["end", "d", "A"],
             "c" => ["A"],
             "d" => ["b"]
           }
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == 10
  end

  @tag :example
  test "part 1 example 2", %{example2: example2} do
    assert part1(example2) == 19
  end

  @tag :example
  test "part 1 example 3", %{example3: example3} do
    assert part1(example3) == 226
  end

  @tag :example
  test "part 2 example 1", %{example1: example1} do
    assert part2(example1) == 36
  end

  @tag :example
  test "part 2 example 2", %{example2: example2} do
    assert part2(example2) == 103
  end

  @tag :example
  test "part 2 example 3", %{example3: example3} do
    assert part2(example3) == 3509
  end

  @tag :solution
  @tag :year2021
  @tag :day12
  test "part 1 solved", %{input: input} do
    assert part1(input) == 3410
  end

  @tag :solution
  @tag :year2021
  @tag :day12
  test "part 2 solved", %{input: input} do
    assert part2(input) == 98_796
  end
end
