defmodule Mix.Tasks.Benchmark do
  use Mix.Task

  @shortdoc "Benchmark AOC"
  def run(_args) do
    input = AOC2017.Day01.parse("../input.txt") |> hd

    Benchee.run(%{
      "part 1" => fn -> AOC2017.Day01.part1(input) end,
      "part 2" => fn -> AOC2017.Day01.part2(input) end
    })
  end
end
