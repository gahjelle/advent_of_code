defmodule Mix.Tasks.Benchmark do
  @moduledoc """
  Benchmark Advent of code solutions
  """

  use Mix.Task
  require AOC

  @bm_args [warmup: 0.1, time: 2]

  @shortdoc "Benchmark AOC"
  def run([year, day]) do
    aoc_module =
      "Elixir.AOC#{year}.Day#{String.pad_leading(day, 2, "0")}"
      |> String.to_existing_atom()

    puzzle_dir = Path.wildcard("lib/#{year}/#{String.pad_leading(day, 2, "0")}_*/") |> hd
    input = Path.join(puzzle_dir, "input.txt") |> AOC.read_text()
    parsed_input = input |> aoc_module.parse()

    @bm_args
    |> Benchee.init()
    |> Benchee.system()
    |> Benchee.benchmark("#{year} day #{day}, parse", fn -> aoc_module.parse(input) end)
    |> Benchee.benchmark("#{year} day #{day}, part 1", fn -> aoc_module.part1(parsed_input) end)
    |> Benchee.benchmark("#{year} day #{day}, part 2", fn -> aoc_module.part2(parsed_input) end)
    |> Benchee.collect()
    |> Benchee.statistics()
    |> Benchee.Formatter.output()
    |> format_as_markdown(puzzle_dir)
  end

  defp format_as_markdown(%{scenarios: scenarios}, puzzle_path) do
    [parse, part1, part2] =
      scenarios
      |> Enum.map(fn s -> s.run_time_data.statistics.median end)

    [parse, part1, part2, total] =
      [parse, part1, part2, parse + part1 + part2] |> Enum.map(&format_as_timestring/1)

    [directory, year | _] = puzzle_path |> Path.split() |> Enum.reverse()
    day = directory |> String.slice(0..1) |> String.to_integer()
    file = "aoc#{year}#{String.slice(directory, 0..1)}.ex"

    name =
      directory
      |> String.slice(3..99)
      |> String.replace("_", " ")
      |> String.split(" ")
      |> Enum.map_join(" ", &String.capitalize/1)

    "\n\n| #{day} | #{name} | [#{file}](#{directory}/#{file}) | #{parse} | #{part1} | #{part2} | #{total} |"
    |> IO.puts()
  end

  defp format_as_timestring(nanoseconds) do
    Number.SI.number_to_si(nanoseconds / 1_000_000_000, unit: "s", separator: " ", precision: 2)
    |> String.replace(" ns", " ns ⚪️")
    |> String.replace(" µs", " µs ⚪️")
    |> String.replace(" ms", " ms 🔵")
    |> String.replace(" s", " s 🔴")
  end
end
