defmodule Mix.Tasks.Solve do
  use Mix.Task

  @shortdoc "Solve AOC"
  def run(args) do
    case args do
      ["2015", "1" | files] -> AOC2015.Day01.main(files)
      ["2017", "1" | files] -> AOC2017.Day01.main(files)
      ["2019", "1" | files] -> AOC2019.Day01.main(files)
    end
  end
end
