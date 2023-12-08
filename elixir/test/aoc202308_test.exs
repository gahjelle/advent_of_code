defmodule AOC2023.Day08.Test do
  @moduledoc """
  Tests for Advent of Code 2023, day 8: Haunted Wasteland.
  """
  use ExUnit.Case, async: true
  require AOC
  import AOC2023.Day08, only: [parse: 1, part1: 1, part2: 1]
  doctest(AOC2023.Day08, import: true)

  @puzzle_dir "lib/2023/08_haunted_wasteland/"
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
    {path, nodes} = example1
    assert path === [1, 0]

    assert nodes === %{
             "AAA" => {"BBB", "CCC"},
             "BBB" => {"DDD", "EEE"},
             "CCC" => {"ZZZ", "GGG"},
             "DDD" => {"DDD", "DDD"},
             "EEE" => {"EEE", "EEE"},
             "GGG" => {"GGG", "GGG"},
             "ZZZ" => {"ZZZ", "ZZZ"}
           }
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == 2
  end

  @tag :example
  test "part 1 example 2", %{example2: example2} do
    assert part1(example2) == 6
  end

  @tag :example
  test "part 2 example 1", %{example1: example1} do
    assert part2(example1) == 2
  end

  @tag :example
  test "part 2 example 3", %{example3: example3} do
    assert part2(example3) == 6
  end

  @tag :solution
  @tag :year2023
  @tag :day8
  test "part 1 solved", %{input: input} do
    assert part1(input) == 11_911
  end

  @tag :solution
  @tag :year2023
  @tag :day8
  test "part 2 solved", %{input: input} do
    assert part2(input) == 10_151_663_816_849
  end
end
