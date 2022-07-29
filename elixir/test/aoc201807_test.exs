defmodule AOC2018.Day07.Test do
  @moduledoc """
  Tests for Advent of Code 2018, day 7: The Sum of Its Parts
  """
  use ExUnit.Case, async: true
  require AOC
  import AOC2018.Day07, only: [parse: 1, part1: 1, part2: 1, part2: 2]
  doctest(AOC2018.Day07, import: true)

  @puzzle_dir "lib/2018/07_the_sum_of_its_parts/"
  setup_all do
    {:ok,
     [
       example1: @puzzle_dir |> Path.join("example1.txt") |> AOC.read_text() |> parse(),
       input: @puzzle_dir |> Path.join("input.txt") |> AOC.read_text() |> parse()
     ]}
  end

  @tag :parse
  test "parse example", %{example1: example1} do
    assert example1 === %{?A => 'C', ?F => 'C', ?B => 'A', ?D => 'A', ?E => 'FDB'}
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == 'CABDFE'
  end

  @tag :example
  test "part 2 example 1", %{example1: example1} do
    assert part2(example1, num_workers: 2, steptime: 0) == 15
  end

  @tag :solution
  @tag :year2018
  @tag :day7
  test "part 1 solved", %{input: input} do
    assert part1(input) == 'BGKDMJCNEQRSTUZWHYLPAFIVXO'
  end

  @tag :solution
  @tag :year2018
  @tag :day7
  test "part 2 solved", %{input: input} do
    assert part2(input) == 941
  end
end
