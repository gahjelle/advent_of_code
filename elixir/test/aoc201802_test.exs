defmodule AOC2018.Day02Test do
  use ExUnit.Case
  require AOC

  import AOC2018.Day02, only: [parse: 1, part1: 1, part2: 1]
  @puzzle_dir "lib/2018/02_inventory_management_system/"

  # test "count characters" do
  #   counts = count_characters('abcaba')
  #   assert counts === %{?a => 3, ?b => 2, ?c => 1}
  # end

  test "parse example" do
    input = @puzzle_dir |> Path.join("example1.txt") |> AOC.read_text() |> parse()
    assert input === ['gah', 'lnd', 'kke']
  end

  test "part 1 example 2" do
    input = @puzzle_dir |> Path.join("example2.txt") |> AOC.read_text() |> parse()
    assert part1(input) == 12
  end

  test "part 2 example 3" do
    input = @puzzle_dir |> Path.join("example3.txt") |> AOC.read_text() |> parse()
    assert part2(input) == "fgij"
  end

  test "part 1 solved" do
    input = @puzzle_dir |> Path.join("input.txt") |> AOC.read_text() |> parse()
    assert part1(input) == 4693
  end

  test "part 2 solved" do
    input = @puzzle_dir |> Path.join("input.txt") |> AOC.read_text() |> parse()
    assert part2(input) == "pebjqsalrdnckzfihvtxysomg"
  end
end
