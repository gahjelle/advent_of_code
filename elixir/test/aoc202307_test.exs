defmodule AOC2023.Day07.Test do
  @moduledoc """
  Tests for Advent of Code 2023, day 7: Camel Cards.
  """
  use ExUnit.Case, async: true
  require AOC
  import AOC2023.Day07, only: [parse: 1, part1: 1, part2: 1]
  doctest(AOC2023.Day07, import: true)

  @puzzle_dir "lib/2023/07_camel_cards/"
  setup_all do
    {:ok,
     [
       example1: @puzzle_dir |> Path.join("example1.txt") |> AOC.read_text() |> parse(),
       input: @puzzle_dir |> Path.join("input.txt") |> AOC.read_text() |> parse()
     ]}
  end

  @tag :parse
  test "parse example", %{example1: example1} do
    assert example1 === [
             {~c"32T3K", 765},
             {~c"T55J5", 684},
             {~c"KK677", 28},
             {~c"KTJJT", 220},
             {~c"QQQJA", 483}
           ]
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == 6_440
  end

  @tag :example
  test "part 2 example 1", %{example1: example1} do
    assert part2(example1) == 5_905
  end

  @tag :solution
  @tag :year2023
  @tag :day7
  test "part 1 solved", %{input: input} do
    assert part1(input) == 249_204_891
  end

  @tag :solution
  @tag :year2023
  @tag :day7
  test "part 2 solved", %{input: input} do
    assert part2(input) == 249_666_369
  end
end
