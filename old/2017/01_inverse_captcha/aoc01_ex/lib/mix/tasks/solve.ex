defmodule Mix.Tasks.Solve do
  use Mix.Task

  @shortdoc "Solve AOC"
  def run(args) do
    AOC2017.Day01.main(args)
  end
end
