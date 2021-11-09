defmodule AOC2017.Day01Test do
  use ExUnit.Case
  require AOC

  import AOC2017.Day01, only: [parse: 1, part1: 1, part2: 1]
  @puzzle_dir "lib/2017/01_inverse_captcha/"

  test "parse example" do
    input = @puzzle_dir |> Path.join("example7.txt") |> AOC.read_text() |> parse()
    assert input === [1, 2, 3, 4, 2, 5]
  end

  test "part 1 example" do
    input = @puzzle_dir |> Path.join("example4.txt") |> AOC.read_text() |> parse()
    assert part1(input) == 9
  end

  test "part 2 example" do
    input = @puzzle_dir |> Path.join("example9.txt") |> AOC.read_text() |> parse()
    assert part2(input) == 4
  end

  test "part 1 solved" do
    input = @puzzle_dir |> Path.join("input.txt") |> AOC.read_text() |> parse()
    assert part1(input) == 1141
  end

  test "part 2 solved" do
    input = @puzzle_dir |> Path.join("input.txt") |> AOC.read_text() |> parse()
    assert part2(input) == 950
  end
end
