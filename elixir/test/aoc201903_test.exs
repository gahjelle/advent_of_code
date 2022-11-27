defmodule AOC2019.Day03.Test do
  @moduledoc """
  Tests for Advent of Code 2019, day 3: Crossed Wires
  """
  use ExUnit.Case, async: true
  require AOC
  import AOC2019.Day03, only: [parse: 1, part1: 1, part2: 1]
  doctest(AOC2019.Day03, import: true)

  @puzzle_dir "lib/2019/03_crossed_wires/"
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
    assert example1 === {
             [
               {1, 0},
               {2, 0},
               {3, 0},
               {4, 0},
               {5, 0},
               {6, 0},
               {7, 0},
               {8, 0},
               {8, 1},
               {8, 2},
               {8, 3},
               {8, 4},
               {8, 5},
               {7, 5},
               {6, 5},
               {5, 5},
               {4, 5},
               {3, 5},
               {3, 4},
               {3, 3},
               {3, 2}
             ],
             [
               {0, 1},
               {0, 2},
               {0, 3},
               {0, 4},
               {0, 5},
               {0, 6},
               {0, 7},
               {1, 7},
               {2, 7},
               {3, 7},
               {4, 7},
               {5, 7},
               {6, 7},
               {6, 6},
               {6, 5},
               {6, 4},
               {6, 3},
               {5, 3},
               {4, 3},
               {3, 3},
               {2, 3}
             ]
           }
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == 6
  end

  @tag :example
  test "part 1 example 2", %{example2: example2} do
    assert part1(example2) == 159
  end

  @tag :example
  test "part 1 example 3", %{example3: example3} do
    assert part1(example3) == 135
  end

  @tag :example
  test "part 2 example 1", %{example1: example1} do
    assert part2(example1) == 30
  end

  @tag :example
  test "part 2 example 2", %{example2: example2} do
    assert part2(example2) == 610
  end

  @tag :example
  test "part 2 example 3", %{example3: example3} do
    assert part2(example3) == 410
  end

  @tag :solution
  @tag :year2019
  @tag :day3
  test "part 1 solved", %{input: input} do
    assert part1(input) == 721
  end

  @tag :solution
  @tag :year2019
  @tag :day3
  test "part 2 solved", %{input: input} do
    assert part2(input) == 7388
  end
end
