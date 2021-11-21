defmodule AOC2016.Day01Test do
  use ExUnit.Case
  require AOC

  import AOC2016.Day01, only: [parse: 1, part1: 1, part2: 1]
  @puzzle_dir "lib/2016/01_no_time_for_a_taxicab/"

  test "parse example" do
    input = @puzzle_dir |> Path.join("example1.txt") |> AOC.read_text() |> parse()
    assert input === [{:right, 5}, {:left, 5}, {:right, 5}, {:right, 3}]
  end

  test "part 1 example 1" do
    input = @puzzle_dir |> Path.join("example1.txt") |> AOC.read_text() |> parse()
    assert part1(input) == 12
  end

  test "part 2 example 2" do
    input = @puzzle_dir |> Path.join("example2.txt") |> AOC.read_text() |> parse()
    assert part2(input) == 4
  end

  test "part 1 solved" do
    input = @puzzle_dir |> Path.join("input.txt") |> AOC.read_text() |> parse()
    assert part1(input) == 246
  end

  test "part 2 solved" do
    input = @puzzle_dir |> Path.join("input.txt") |> AOC.read_text() |> parse()
    assert part2(input) == 124
  end
end
