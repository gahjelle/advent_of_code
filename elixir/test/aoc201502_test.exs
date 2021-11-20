defmodule AOC2015.Day02Test do
  use ExUnit.Case
  require AOC

  alias AOC2015.Day02.Present
  import AOC2015.Day02, only: [parse: 1, part1: 1, part2: 1]
  @puzzle_dir "lib/2015/02_i_was_told_there_would_be_no_math/"

  test "parse example" do
    input = @puzzle_dir |> Path.join("example1.txt") |> AOC.read_text() |> parse()

    assert input === [
             %Present{length: 2, width: 3, height: 4},
             %Present{length: 1, width: 1, height: 10}
           ]
  end

  test "part 1 example 1" do
    input = @puzzle_dir |> Path.join("example1.txt") |> AOC.read_text() |> parse()
    assert part1(input) == 101
  end

  test "part 2 example" do
    input = @puzzle_dir |> Path.join("example1.txt") |> AOC.read_text() |> parse()
    assert part2(input) == 48
  end

  test "part 1 solved" do
    input = @puzzle_dir |> Path.join("input.txt") |> AOC.read_text() |> parse()
    assert part1(input) == 1_598_415
  end

  test "part 2 solved" do
    input = @puzzle_dir |> Path.join("input.txt") |> AOC.read_text() |> parse()
    assert part2(input) == 3_812_909
  end
end
