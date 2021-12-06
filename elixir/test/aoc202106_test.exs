defmodule AOC2021.Day06.Test do
  @moduledoc """
  Tests for Advent of Code 2021, day 6: Lanternfish
  """
  use ExUnit.Case, async: true
  require AOC
  import AOC2021.Day06, only: [parse: 1, part1: 1, part2: 1]
  doctest(AOC2021.Day06, import: true)

  @puzzle_dir "lib/2021/06_lanternfish/"
  setup_all do
    {:ok,
     [
       example1: @puzzle_dir |> Path.join("example1.txt") |> AOC.read_text() |> parse(),
       input: @puzzle_dir |> Path.join("input.txt") |> AOC.read_text() |> parse()
     ]}
  end

  @tag :parse
  test "parse example", %{example1: example1} do
    assert example1 === [3, 4, 3, 1, 2]
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == 5934
  end

  @tag :example
  test "part 2 example 1", %{example1: example1} do
    assert part2(example1) == 26_984_457_539
  end

  @tag :solution
  @tag :year2021
  @tag :day6
  test "part 1 solved", %{input: input} do
    assert part1(input) == 395_627
  end

  @tag :solution
  @tag :year2021
  @tag :day6
  test "part 2 solved", %{input: input} do
    assert part2(input) == 1_767_323_539_209
  end
end
