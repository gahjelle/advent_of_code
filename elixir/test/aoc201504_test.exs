defmodule AOC2015.Day04Test do
  use ExUnit.Case
  require AOC

  import AOC2015.Day04, only: [parse: 1, part1: 1, part2: 1]
  @puzzle_dir "lib/2015/04_the_ideal_stocking_stuffer/"

  test "parse example" do
    input = @puzzle_dir |> Path.join("example1.txt") |> AOC.read_text() |> parse()

    assert input === "abcdef"
  end

  test "part 1 example 1" do
    input = @puzzle_dir |> Path.join("example1.txt") |> AOC.read_text() |> parse()
    assert part1(input) == 609_043
  end

  test "part 1 example 2" do
    input = @puzzle_dir |> Path.join("example2.txt") |> AOC.read_text() |> parse()
    assert part1(input) == 1_048_970
  end

  test "part 1 solved" do
    input = @puzzle_dir |> Path.join("input.txt") |> AOC.read_text() |> parse()
    assert part1(input) == 117_946
  end

  test "part 2 solved" do
    input = @puzzle_dir |> Path.join("input.txt") |> AOC.read_text() |> parse()
    assert part2(input) == 3_938_038
  end
end
