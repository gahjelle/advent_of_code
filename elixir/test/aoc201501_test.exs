defmodule AOC2015.Day01Test do
  use ExUnit.Case
  require AOC

  import AOC2015.Day01, only: [parse: 1, part1: 1, part2: 1]
  @puzzle_dir "lib/2015/01_not_quite_lisp/"

  test "parse example" do
    input = @puzzle_dir |> Path.join("example1.txt") |> AOC.read_text() |> parse()
    assert input === [1, 1, -1, -1]
  end

  test "part 1 example 1" do
    input = @puzzle_dir |> Path.join("example1.txt") |> AOC.read_text() |> parse()
    assert part1(input) == 0
  end

  test "part 1 example 2" do
    input = @puzzle_dir |> Path.join("example2.txt") |> AOC.read_text() |> parse()
    assert part1(input) == 3
  end

  test "part 1 example 3" do
    input = @puzzle_dir |> Path.join("example3.txt") |> AOC.read_text() |> parse()
    assert part1(input) == -3
  end

  test "part 2 example" do
    input = @puzzle_dir |> Path.join("example4.txt") |> AOC.read_text() |> parse()
    assert part2(input) == 5
  end

  test "part 1 solved" do
    input = @puzzle_dir |> Path.join("input.txt") |> AOC.read_text() |> parse()
    assert part1(input) == 232
  end

  test "part 2 solved" do
    input = @puzzle_dir |> Path.join("input.txt") |> AOC.read_text() |> parse()
    assert part2(input) == 1783
  end
end
