defmodule Mix.Tasks.Solve do
  @moduledoc """
  Solve one Advent of Code puzzle with the given input files
  """
  use Mix.Task

  @shortdoc "Solve AOC"
  def run([year, day]) do
    puzzle_dir = Path.wildcard("lib/#{year}/#{String.pad_leading(day, 2, "0")}_*/") |> hd
    run([year, day, Path.join(puzzle_dir, "input.txt")])
  end

  def run([year, day | files]) do
    aoc_module =
      "Elixir.AOC#{year}.Day#{String.pad_leading(day, 2, "0")}"
      |> String.to_existing_atom()

    aoc_module.main(files)
  end
end
