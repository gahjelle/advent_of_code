defmodule AOC do
  @moduledoc """
  Advent of Code helper functions and macros
  """

  defmacro __using__(_) do
    quote do
      import AOC
    end
  end

  def read_text(path) do
    with {:ok, file} <- File.read(path) do
      file
      |> String.trim()
    end
  end

  def solve(path, parse_func, part1_func, part2_func) do
    IO.puts("\n#{path}:")

    input = read_text(path) |> parse_func.()
    input |> part1_func.() |> IO.puts()
    input |> part2_func.() |> IO.puts()
  end
end
