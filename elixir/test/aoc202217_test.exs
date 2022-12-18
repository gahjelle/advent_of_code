defmodule AOC2022.Day17.Test do
  @moduledoc """
  Tests for Advent of Code 2022, day 17: Pyroclastic Flow.
  """
  use ExUnit.Case, async: true
  require AOC
  import AOC2022.Day17, only: [parse: 1, part1: 1, part2: 1, find_tower_height: 2]
  doctest(AOC2022.Day17, import: true)

  @puzzle_dir "lib/2022/17_pyroclastic_flow/"
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
             {[
                :right,
                :right,
                :right,
                :left,
                :left,
                :right,
                :left,
                :right,
                :right,
                :left,
                :left,
                :left,
                :right,
                :right,
                :left,
                :right,
                :right,
                :right,
                :left,
                :left,
                :left,
                :right,
                :right,
                :right,
                :left,
                :left,
                :left,
                :right,
                :left,
                :left,
                :left,
                :right,
                :right,
                :left,
                :right,
                :right,
                :left,
                :left,
                :right,
                :right
              ], 0, 40}
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == 3_068
  end

  @tag :example
  test "part 2 example 1", %{example1: example1} do
    assert part2(example1) == 1_514_285_714_288
  end

  test "short jets" do
    assert find_tower_height({[:left], 0, 1}, 5555) == 12221
  end

  @tag :solution
  @tag :year2022
  @tag :day17
  test "part 1 solved", %{input: input} do
    assert part1(input) == 3_177
  end

  @tag :solution
  @tag :year2022
  @tag :day17
  test "part 2 solved", %{input: input} do
    assert part2(input) == 1_565_517_241_382
  end
end
