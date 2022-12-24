defmodule AOC2022.Day24.Test do
  @moduledoc """
  Tests for Advent of Code 2022, day 24: Blizzard Basin.
  """
  use ExUnit.Case, async: true
  require AOC
  import AOC2022.Day24, only: [parse: 1, part1: 1, part2: 1]
  doctest(AOC2022.Day24, import: true)

  @puzzle_dir "lib/2022/24_blizzard_basin/"
  setup_all do
    {:ok,
     [
       example1: @puzzle_dir |> Path.join("example1.txt") |> AOC.read_text() |> parse(),
       input: @puzzle_dir |> Path.join("input.txt") |> AOC.read_text() |> parse()
     ]}
  end

  @tag :parse
  test "parse example", %{example1: example1} do
    {size, blizzards} = example1
    assert size === {4, 6}

    assert blizzards |> Enum.into(%{}, fn {cycle, pos} -> {cycle, MapSet.size(pos)} end) === %{
             0 => 19,
             1 => 14,
             2 => 14,
             3 => 14,
             4 => 14,
             5 => 14,
             6 => 15,
             7 => 15,
             8 => 14,
             9 => 16,
             10 => 14,
             11 => 15
           }
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == 18
  end

  @tag :example
  test "part 2 example 1", %{example1: example1} do
    assert part2(example1) == 54
  end

  @tag :solution
  @tag :year2022
  @tag :day24
  test "part 1 solved", %{input: input} do
    assert part1(input) == 299
  end

  @tag :solution
  @tag :year2022
  @tag :day24
  test "part 2 solved", %{input: input} do
    assert part2(input) == 899
  end
end
