defmodule AOC2022.Day06.Test do
  @moduledoc """
  Tests for Advent of Code 2022, day 6: Tuning Trouble.
  """
  use ExUnit.Case, async: true
  require AOC
  import AOC2022.Day06, only: [parse: 1, part1: 1, part2: 1]
  doctest(AOC2022.Day06, import: true)

  @puzzle_dir "lib/2022/06_tuning_trouble/"
  setup_all do
    {:ok,
     [
       example1: @puzzle_dir |> Path.join("example1.txt") |> AOC.read_text() |> parse(),
       example2: @puzzle_dir |> Path.join("example2.txt") |> AOC.read_text() |> parse(),
       example3: @puzzle_dir |> Path.join("example3.txt") |> AOC.read_text() |> parse(),
       example4: @puzzle_dir |> Path.join("example4.txt") |> AOC.read_text() |> parse(),
       example5: @puzzle_dir |> Path.join("example5.txt") |> AOC.read_text() |> parse(),
       input: @puzzle_dir |> Path.join("input.txt") |> AOC.read_text() |> parse()
     ]}
  end

  @tag :parse
  test "parse example", %{example1: example1} do
    assert example1 === 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == 7
  end

  @tag :example
  test "part 2 example 1", %{example1: example1} do
    assert part2(example1) == 19
  end

  @tag :example
  test "part 1 example 2", %{example2: example2} do
    assert part1(example2) == 5
  end

  @tag :example
  test "part 2 example 2", %{example2: example2} do
    assert part2(example2) == 23
  end

  @tag :example
  test "part 1 example 3", %{example3: example3} do
    assert part1(example3) == 6
  end

  @tag :example
  test "part 2 example 3", %{example3: example3} do
    assert part2(example3) == 23
  end

  @tag :example
  test "part 1 example 4", %{example4: example4} do
    assert part1(example4) == 10
  end

  @tag :example
  test "part 2 example 4", %{example4: example4} do
    assert part2(example4) == 29
  end

  @tag :example
  test "part 1 example 5", %{example5: example5} do
    assert part1(example5) == 11
  end

  @tag :example
  test "part 2 example 5", %{example5: example5} do
    assert part2(example5) == 26
  end

  @tag :solution
  @tag :year2022
  @tag :day6
  test "part 1 solved", %{input: input} do
    assert part1(input) == 1987
  end

  @tag :solution
  @tag :year2022
  @tag :day6
  test "part 2 solved", %{input: input} do
    assert part2(input) == 3059
  end
end
