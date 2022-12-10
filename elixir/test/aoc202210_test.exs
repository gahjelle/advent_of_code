defmodule AOC2022.Day10.Test do
  @moduledoc """
  Tests for Advent of Code 2022, day 10: Cathode-Ray Tube.
  """
  use ExUnit.Case, async: true
  require AOC
  import AOC2022.Day10, only: [parse: 1, part1: 1, part2: 1]
  doctest(AOC2022.Day10, import: true)

  @puzzle_dir "lib/2022/10_cathode-ray_tube/"
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
    assert example1 === [1, 1, 1, 4, 4, -1, -1]
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == 0
  end

  @tag :example
  test "part 1 example 2", %{example2: example2} do
    assert part1(example2) == 13_140
  end

  @tag :example
  test "part 2 example 1", %{example1: example1} do
    assert part2(example1) == "█████  "
  end

  @tag :example
  test "part 2 example 2", %{example2: example2} do
    assert part2(example2) ==
             "██  ██  ██  ██  ██  ██  ██  ██  ██  ██  \n███   ███   ███   ███   ███   ███   ███ \n████    ████    ████    ████    ████    \n█████     █████     █████     █████     \n██████      ██████      ██████      ████\n███████       ███████       ███████     "
  end

  @tag :solution
  @tag :year2022
  @tag :day10
  test "part 1 solved", %{input: input} do
    assert part1(input) == 14_760
  end

  @tag :solution
  @tag :year2022
  @tag :day10
  test "part 2 solved", %{input: input} do
    assert part2(input) ==
             "████ ████  ██  ████ ███  █  █ ███  ████ \n█    █    █  █ █    █  █ █  █ █  █ █    \n███  ███  █    ███  █  █ █  █ █  █ ███  \n█    █    █ ██ █    ███  █  █ ███  █    \n█    █    █  █ █    █ █  █  █ █ █  █    \n████ █     ███ ████ █  █  ██  █  █ ████ "
  end
end
