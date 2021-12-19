defmodule AOC2021.Day17 do
  @moduledoc """
  Advent of Code 2021, day 17: Trick Shot
  """
  require AOC

  @doc """
  Parse input
  """
  def parse(puzzle_input) do
    Regex.run(~r/x=(\d+)..(\d+), y=(-?\d+)..(-?\d+)/, puzzle_input, capture: :all_but_first)
    |> Enum.map(&String.to_integer/1)
    |> then(fn [x_min, x_max, y_min, y_max] -> {x_min..x_max, y_min..y_max} end)
  end

  @doc """
  Solve part 1
  """
  def part1({x_range, y_range}) do
    max_y = y_range |> Enum.map(&abs/1) |> Enum.max()

    for y0 <- max_y..0,
        x0 <- 0..(x_range |> Enum.max()) do
      {y0, x0}
    end
    |> Enum.reduce_while(nil, fn {y0, x0}, _ ->
      case simulate(x0, y0, x_range, y_range) do
        {true, height} -> {:halt, height}
        {false, _} -> {:cont, nil}
      end
    end)
  end

  @doc """
  Solve part 2
  """
  def part2({x_range, y_range}) do
    max_y = y_range |> Enum.map(&abs/1) |> Enum.max()

    for x0 <- 0..(x_range |> Enum.max()),
        y0 <- -max_y..max_y do
      simulate(x0, y0, x_range, y_range) |> elem(0)
    end
    |> Enum.count(& &1)
  end

  @doc """
  Simulate a shot to check if it ends up within the target area

  ## Examples:

      iex> simulate(3, 4, 4..7, -5..-2)
      {true, 10}

      iex> simulate(3, 5, 4..7, -5..-2)
      {false, 15}
  """
  def simulate(x0, y0, x_range, y_range), do: simulate(0, 0, 0, x0, y0, x_range, y_range)

  def simulate(x, y, max_y, vx, vy, x_range, y_range) do
    cond do
      x in x_range and y in y_range -> {true, max_y}
      vx == 0 and x not in x_range -> {false, max_y}
      vy < 0 and y < Enum.min(y_range) -> {false, max_y}
      vx == 0 -> simulate(x, y + vy, max(y, max_y), 0, vy - 1, x_range, y_range)
      true -> simulate(x + vx, y + vy, max(y, max_y), vx - 1, vy - 1, x_range, y_range)
    end
  end

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
