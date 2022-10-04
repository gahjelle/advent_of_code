defmodule AOC2021.Day13.Test do
  @moduledoc """
  Tests for Advent of Code 2021, day 13: Transparent Origami
  """
  use ExUnit.Case, async: true
  require AOC
  import AOC2021.Day13, only: [parse: 1, part1: 1, part2: 1]
  doctest(AOC2021.Day13, import: true)

  @puzzle_dir "lib/2021/13_transparent_origami/"
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
    assert example1 === {
             MapSet.new([
               {6, 10},
               {0, 14},
               {9, 10},
               {0, 3},
               {10, 4},
               {4, 11},
               {6, 0},
               {6, 12},
               {4, 1},
               {0, 13},
               {10, 12},
               {3, 4},
               {3, 0},
               {8, 4},
               {1, 10},
               {2, 14},
               {8, 10},
               {9, 0}
             ]),
             [y: 7, x: 5]
           }
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == 17
  end

  @tag :example
  test "part 2 example 1", %{example1: example1} do
    # The letter 'O'
    assert part2(example1) == "█████\n█   █\n█   █\n█   █\n█████"
  end

  @tag :example
  test "part 2 example 2", %{example2: example2} do
    # The letters 'AOC'
    assert part2(example2) ==
             " ██   ██   ██ \n█  █ █  █ █  █\n█  █ █  █ █   \n████ █  █ █   \n█  █ █  █ █  █\n█  █  ██   ██ "
  end

  @tag :solution
  @tag :year2021
  @tag :day13
  test "part 1 solved", %{input: input} do
    assert part1(input) == 653
  end

  @tag :solution
  @tag :year2021
  @tag :day13
  test "part 2 solved", %{input: input} do
    # The letters 'LKREBPRK'
    assert part2(input) ==
             "█    █  █ ███  ████ ███  ███  ███  █  █\n█    █ █  █  █ █    █  █ █  █ █  █ █ █ \n█    ██   █  █ ███  ███  █  █ █  █ ██  \n█    █ █  ███  █    █  █ ███  ███  █ █ \n█    █ █  █ █  █    █  █ █    █ █  █ █ \n████ █  █ █  █ ████ ███  █    █  █ █  █"
  end
end
