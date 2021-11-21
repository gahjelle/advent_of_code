defmodule AOC2018.Day01Test do
  use ExUnit.Case
  require AOC

  import AOC2018.Day01, only: [parse: 1, part1: 1, part2: 1]
  @puzzle_dir "lib/2018/01_chronal_calibration/"

  test "parse example" do
    input = @puzzle_dir |> Path.join("example1.txt") |> AOC.read_text() |> parse()
    assert input === [1, -2, 3, 1]
  end

  test "part 1 example" do
    input = @puzzle_dir |> Path.join("example1.txt") |> AOC.read_text() |> parse()
    assert part1(input) == 3
  end

  test "part 2 example" do
    input = @puzzle_dir |> Path.join("example1.txt") |> AOC.read_text() |> parse()
    assert part2(input) == 2
  end

  test "part 2 example 2" do
    input = @puzzle_dir |> Path.join("example2.txt") |> AOC.read_text() |> parse()
    assert part2(input) == 10
  end

  test "part 2 example 3" do
    input = @puzzle_dir |> Path.join("example3.txt") |> AOC.read_text() |> parse()
    assert part2(input) == 0
  end

  test "part 1 solved" do
    input = @puzzle_dir |> Path.join("input.txt") |> AOC.read_text() |> parse()
    assert part1(input) == 531
  end

  test "part 2 solved" do
    input = @puzzle_dir |> Path.join("input.txt") |> AOC.read_text() |> parse()
    assert part2(input) == 76787
  end
end
