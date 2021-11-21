defmodule AOC2020.Day01Test do
  use ExUnit.Case
  require AOC

  import AOC2020.Day01, only: [parse: 1, part1: 1, part2: 1]
  @puzzle_dir "lib/2020/01_report_repair/"

  test "parse example" do
    input = @puzzle_dir |> Path.join("example1.txt") |> AOC.read_text() |> parse()
    assert input === MapSet.new([1721, 979, 366, 299, 675, 1456])
  end

  test "part 1 example 1" do
    input = @puzzle_dir |> Path.join("example1.txt") |> AOC.read_text() |> parse()
    assert part1(input) == 514_579
  end

  test "part 2 example 1" do
    input = @puzzle_dir |> Path.join("example1.txt") |> AOC.read_text() |> parse()
    assert part2(input) == 241_861_950
  end

  test "part 1 solved" do
    input = @puzzle_dir |> Path.join("input.txt") |> AOC.read_text() |> parse()
    assert part1(input) == 744_475
  end

  test "part 2 solved" do
    input = @puzzle_dir |> Path.join("input.txt") |> AOC.read_text() |> parse()
    assert part2(input) == 70_276_940
  end
end
