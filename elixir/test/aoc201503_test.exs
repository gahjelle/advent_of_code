defmodule AOC2015.Day03Test do
  use ExUnit.Case
  require AOC

  import AOC2015.Day03, only: [parse: 1, part1: 1, part2: 1]
  @puzzle_dir "lib/2015/03_perfectly_spherical_houses_in_a_vacuum/"

  test "parse example" do
    input = @puzzle_dir |> Path.join("example1.txt") |> AOC.read_text() |> parse()

    assert input === [{0, 1}, {1, 0}, {0, -1}, {-1, 0}]
  end

  test "part 1 example 1" do
    input = @puzzle_dir |> Path.join("example1.txt") |> AOC.read_text() |> parse()
    assert part1(input) == 4
  end

  test "part 1 example 2" do
    input = @puzzle_dir |> Path.join("example2.txt") |> AOC.read_text() |> parse()
    assert part1(input) == 2
  end

  test "part 2 example 1" do
    input = @puzzle_dir |> Path.join("example1.txt") |> AOC.read_text() |> parse()
    assert part2(input) == 3
  end

  test "part 2 example 2" do
    input = @puzzle_dir |> Path.join("example2.txt") |> AOC.read_text() |> parse()
    assert part2(input) == 11
  end

  test "part 1 solved" do
    input = @puzzle_dir |> Path.join("input.txt") |> AOC.read_text() |> parse()
    assert part1(input) == 2565
  end

  test "part 2 solved" do
    input = @puzzle_dir |> Path.join("input.txt") |> AOC.read_text() |> parse()
    assert part2(input) == 2639
  end
end
