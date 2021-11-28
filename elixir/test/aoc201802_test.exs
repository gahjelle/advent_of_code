defmodule AOC2018.Day02.Test do
  @moduledoc """
  Tests for Advent of Code 2018, day 2: Inventory Management System
  """
  use ExUnit.Case, async: true
  require AOC

  import AOC2018.Day02, only: [parse: 1, part1: 1, part2: 1]
  @puzzle_dir "lib/2018/02_inventory_management_system/"

  setup_all do
    {:ok,
     [
       example1: @puzzle_dir |> Path.join("example1.txt") |> AOC.read_text() |> parse(),
       example2: @puzzle_dir |> Path.join("example2.txt") |> AOC.read_text() |> parse(),
       example3: @puzzle_dir |> Path.join("example3.txt") |> AOC.read_text() |> parse(),
       input: @puzzle_dir |> Path.join("input.txt") |> AOC.read_text() |> parse()
     ]}
  end

  # @tag :unit
  # test "count characters" do
  #   counts = count_characters('abcaba')
  #   assert counts === %{?a => 3, ?b => 2, ?c => 1}
  # end

  @tag :parse
  test "parse example", %{example1: example1} do
    assert example1 === ['gah', 'lnd', 'kke']
  end

  @tag :example
  test "part 1 example 2", %{example2: example2} do
    assert part1(example2) == 12
  end

  @tag :example
  test "part 2 example 3", %{example3: example3} do
    assert part2(example3) == "fgij"
  end

  @tag :solution
  @tag :year2018
  @tag :day2
  test "part 1 solved", %{input: input} do
    assert part1(input) == 4693
  end

  @tag :solution
  @tag :year2018
  @tag :day2
  test "part 2 solved", %{input: input} do
    assert part2(input) == "pebjqsalrdnckzfihvtxysomg"
  end
end
