defmodule Mix.Tasks.Benchmark do
  use Mix.Task
  require AOC

  @shortdoc "Benchmark AOC"
  def run(["2015", "1"]) do
    # Day 1, 2015
    input = "lib/2015/01_not_quite_lisp/input.txt" |> AOC.read_text() |> AOC2015.Day01.parse()

    Benchee.run(%{
      "2015 day 1, part 1" => fn -> AOC2015.Day01.part1(input) end,
      "2015 day 1, part 2" => fn -> AOC2015.Day01.part2(input) end
    })
  end

  def run(["2015", "2"]) do
    # Day 2, 2015
    input =
      "lib/2015/02_i_was_told_there_would_be_no_math/input.txt"
      |> AOC.read_text()
      |> AOC2015.Day02.parse()

    Benchee.run(%{
      "2015 day 2, part 1" => fn -> AOC2015.Day02.part1(input) end,
      "2015 day 2, part 2" => fn -> AOC2015.Day02.part2(input) end
    })
  end

  def run(["2017", "1"]) do
    # Day 1, 2017
    input = "lib/2017/01_inverse_captcha/input.txt" |> AOC.read_text() |> AOC2017.Day01.parse()

    Benchee.run(%{
      "2017 day 1, part 1" => fn -> AOC2017.Day01.part1(input) end,
      "2017 day 1, part 2" => fn -> AOC2017.Day01.part2(input) end
    })
  end

  def run(["2019", "1"]) do
    # Day 1, 2019
    input =
      "lib/2019/01_the_tyranny_of_the_rocket_equation/input.txt"
      |> AOC.read_text()
      |> AOC2019.Day01.parse()

    Benchee.run(%{
      "2019 day 1, part 1" => fn -> AOC2019.Day01.part1(input) end,
      "2019 day 1, part 2" => fn -> AOC2019.Day01.part2(input) end
    })
  end
end
