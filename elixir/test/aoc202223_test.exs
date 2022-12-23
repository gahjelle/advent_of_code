defmodule AOC2022.Day23.Test do
  @moduledoc """
  Tests for Advent of Code 2022, day 23: Unstable Diffusion.
  """
  use ExUnit.Case, async: true
  require AOC
  import AOC2022.Day23, only: [parse: 1, part1: 1, part2: 1]
  doctest(AOC2022.Day23, import: true)

  @puzzle_dir "lib/2022/23_unstable_diffusion/"
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
    assert example1 === MapSet.new([{1, 2}, {1, 3}, {2, 2}, {4, 2}, {4, 3}])
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == 25
  end

  @tag :example
  test "part 1 example 2", %{example2: example2} do
    assert part1(example2) == 110
  end

  @tag :example
  test "part 2 example 1", %{example1: example1} do
    assert part2(example1) == 4
  end

  @tag :example
  test "part 2 example 2", %{example2: example2} do
    assert part2(example2) == 20
  end

  @tag :solution
  @tag :year2022
  @tag :day23
  test "part 1 solved", %{input: input} do
    assert part1(input) == 4254
  end

  @tag :solution
  @tag :year2022
  @tag :day23
  test "part 2 solved", %{input: input} do
    assert part2(input) == 992
  end
end
