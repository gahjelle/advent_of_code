defmodule AOC2015.Day05Test do
  use ExUnit.Case
  require AOC

  import AOC2015.Day05, only: [parse: 1, part1: 1, part2: 1]
  @puzzle_dir "lib/2015/05_doesnt_he_have_intern-elves_for_this/"

  test "parse example" do
    input = @puzzle_dir |> Path.join("example1.txt") |> AOC.read_text() |> parse()

    assert input === [
             'ugknbfddgicrmopn',
             'aaa',
             'jchzalrnumimnmhp',
             'haegwjzuvuyypxyu',
             'dvszwmarrgswjxmb'
           ]
  end

  test "part 1 example 1" do
    input = @puzzle_dir |> Path.join("example1.txt") |> AOC.read_text() |> parse()
    assert part1(input) == 2
  end

  test "part 2 example 2" do
    input = @puzzle_dir |> Path.join("example2.txt") |> AOC.read_text() |> parse()
    assert part2(input) == 2
  end

  test "part 1 solved" do
    input = @puzzle_dir |> Path.join("input.txt") |> AOC.read_text() |> parse()
    assert part1(input) == 236
  end

  test "part 2 solved" do
    input = @puzzle_dir |> Path.join("input.txt") |> AOC.read_text() |> parse()
    assert part2(input) == 51
  end
end
