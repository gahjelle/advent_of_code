defmodule AOC2019.Day01Test do
  use ExUnit.Case
  require AOC

  import AOC2019.Day01, only: [parse: 1, part1: 1, part2: 1]
  @puzzle_dir "lib/2019/01_the_tyranny_of_the_rocket_equation/"

  test "parse example" do
    input = @puzzle_dir |> Path.join("example1.txt") |> AOC.read_text() |> parse()
    assert input === [12, 14, 1969, 100_756]
  end

  test "part 1 example" do
    input = @puzzle_dir |> Path.join("example1.txt") |> AOC.read_text() |> parse()
    assert part1(input) == 2 + 2 + 654 + 33583
  end

  test "part 2 example" do
    input = @puzzle_dir |> Path.join("example1.txt") |> AOC.read_text() |> parse()
    assert part2(input) == 2 + 2 + 966 + 50346
  end

  test "part 1 solved" do
    input = @puzzle_dir |> Path.join("input.txt") |> AOC.read_text() |> parse()
    assert part1(input) == 3_550_236
  end

  test "part 2 solved" do
    input = @puzzle_dir |> Path.join("input.txt") |> AOC.read_text() |> parse()
    assert part2(input) == 5_322_455
  end
end
