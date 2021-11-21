defmodule Mix.Tasks.Solve do
  use Mix.Task

  @shortdoc "Solve AOC"
  def run(args) do
    case args do
      ["2015", "1" | files] -> AOC2015.Day01.main(files)
      ["2015", "2" | files] -> AOC2015.Day02.main(files)
      ["2015", "3" | files] -> AOC2015.Day03.main(files)
      ["2015", "4" | files] -> AOC2015.Day04.main(files)
      ["2016", "1" | files] -> AOC2016.Day01.main(files)
      ["2017", "1" | files] -> AOC2017.Day01.main(files)
      ["2018", "1" | files] -> AOC2018.Day01.main(files)
      ["2019", "1" | files] -> AOC2019.Day01.main(files)
    end
  end
end
