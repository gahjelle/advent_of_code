defmodule Mix.Tasks.Benchmark do
  use Mix.Task
  require AOC

  @shortdoc "Benchmark AOC"
  def run(_args) do

    # Day 1, 2017
    input = "lib/2017/01_inverse_captcha/input.txt" |> AOC.read_text() |> AOC2017.Day01.parse()
    Benchee.run(%{
      "2017 day 1, part 1" => fn -> AOC2017.Day01.part1(input) end,
      "2017 day 1, part 2" => fn -> AOC2017.Day01.part2(input) end
    })

    # Day 1, 2019
    input = "lib/2019/01_the_tyranny_of_the_rocket_equation/input.txt" |> AOC.read_text() |> AOC2019.Day01.parse()
    Benchee.run(%{
      "2019 day 1, part 1" => fn -> AOC2019.Day01.part1(input) end,
      "2019 day 1, part 2" => fn -> AOC2019.Day01.part2(input) end
    })
  end
end
