defmodule AOC2017.Day01Test do
  use ExUnit.Case
  doctest AOC2017.Day01

  test "part 1 solved" do
    input = AOC2017.Day01.parse("../input.txt") |> hd
    assert AOC2017.Day01.part1(input) == 1141
  end

  test "part 2 solved" do
    input = AOC2017.Day01.parse("../input.txt") |> hd
    assert AOC2017.Day01.part2(input) == 950
  end
end
