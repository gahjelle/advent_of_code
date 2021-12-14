defmodule AOC2021.Day14.Test do
  @moduledoc """
  Tests for Advent of Code 2021, day 14: Extended Polymerization
  """
  use ExUnit.Case, async: true
  require AOC
  import AOC2021.Day14, only: [parse: 1, part1: 1, part2: 1]
  doctest(AOC2021.Day14, import: true)

  @puzzle_dir "lib/2021/14_extended_polymerization/"
  setup_all do
    {:ok,
     [
       example1: @puzzle_dir |> Path.join("example1.txt") |> AOC.read_text() |> parse(),
       input: @puzzle_dir |> Path.join("input.txt") |> AOC.read_text() |> parse()
     ]}
  end

  @tag :parse
  test "parse example", %{example1: example1} do
    assert example1 === {
             'N',
             %{'NN' => 1, 'NC' => 1, 'CB' => 1},
             %{
               'CH' => ['CB', 'BH'],
               'HH' => ['HN', 'NH'],
               'CB' => ['CH', 'HB'],
               'NH' => ['NC', 'CH'],
               'HB' => ['HC', 'CB'],
               'HC' => ['HB', 'BC'],
               'HN' => ['HC', 'CN'],
               'NN' => ['NC', 'CN'],
               'BH' => ['BH', 'HH'],
               'NC' => ['NB', 'BC'],
               'NB' => ['NB', 'BB'],
               'BN' => ['BB', 'BN'],
               'BB' => ['BN', 'NB'],
               'BC' => ['BB', 'BC'],
               'CC' => ['CN', 'NC'],
               'CN' => ['CC', 'CN']
             }
           }
  end

  @tag :example
  test "part 1 example 1", %{example1: example1} do
    assert part1(example1) == 1588
  end

  @tag :example
  test "part 2 example 1", %{example1: example1} do
    assert part2(example1) == 2_188_189_693_529
  end

  @tag :solution
  @tag :year2021
  @tag :day14
  test "part 1 solved", %{input: input} do
    assert part1(input) == 2937
  end

  @tag :solution
  @tag :year2021
  @tag :day14
  test "part 2 solved", %{input: input} do
    assert part2(input) == 3_390_034_818_249
  end
end
