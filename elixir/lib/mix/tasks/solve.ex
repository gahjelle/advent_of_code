defmodule Mix.Tasks.Solve do
  use Mix.Task

  @shortdoc "Solve AOC"
  def run([year, day | files]) do
    aoc_module =
      "Elixir.AOC#{year}.Day#{String.pad_leading(day, 2, "0")}"
      |> String.to_existing_atom()

    aoc_module.main(files)
  end
end
