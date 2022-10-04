defmodule AOC2021.Day13 do
  @moduledoc """
  Advent of Code 2021, day 13: Transparent Origami
  """
  require AOC

  @doc """
  Parse input
  """
  def parse(puzzle_input) do
    {dots, folds} =
      puzzle_input
      |> String.split("\n", trim: true)
      |> Enum.split_with(&(not String.starts_with?(&1, "fold along ")))

    {parse_points(dots), parse_folds(folds)}
  end

  @doc """
  Parse a list of dots and store them in a MapSet.

  ## Example:

      iex> parse_points(["1,2", "2,0", "1,2", "99,1"])
      MapSet.new([{1, 2}, {2, 0}, {99, 1}])
  """
  def parse_points(dots) do
    dots
    |> Enum.map(fn line ->
      line |> String.split(",") |> Enum.map(&String.to_integer/1) |> List.to_tuple()
    end)
    |> Enum.into(MapSet.new())
  end

  @doc """
  Parse a list of folds and store them in a keyword list.

  ## Example:

      iex> parse_folds(["fold along y=2", "fold along x=8", "fold along y=1"])
      [y: 2, x: 8, y: 1]
  """
  def parse_folds(folds) do
    folds
    |> Enum.map(fn "fold along " <> <<direction::utf8, "=", line::binary>> ->
      {List.to_atom([direction]), String.to_integer(line)}
    end)
  end

  @doc """
  Solve part 1
  """
  # |> Enum.to_list() |> length()
  def part1({dots, folds}), do: folds |> hd() |> fold_one(dots) |> Enum.to_list() |> length()

  @doc """
  Solve part 2
  """
  def part2({dots, folds}), do: folds |> fold_all(dots) |> dots_to_string()

  @doc """
  Make one fold along a horizontal (:y) or vertical (:x) line.

  ## Examples:

                           x: 3         y: 2      x: 3, y: 2
           ..O|.O          .OO|        ..O|.O        .OO|
           .O.|.O          .O.|        OO.|.O        OO.|
           ---+--          ---+        ---+--        ---+
           O..|.O          OO.|

      iex> dots = MapSet.new([{2, 0}, {5, 0}, {1, 1}, {5, 1}, {0, 3}, {5, 3}])
      iex> fold_one({:x, 3}, dots)
      MapSet.new([{1, 0}, {2, 0}, {1, 1}, {0, 3}, {1, 3}])
      iex> fold_one({:y, 2}, dots)
      MapSet.new([{2, 0}, {5, 0}, {0, 1}, {1, 1}, {5, 1}])
  """
  def fold_one({:x, line}, dots), do: fold_one(dots, fn {x, y} -> {line - abs(line - x), y} end)
  def fold_one({:y, line}, dots), do: fold_one(dots, fn {x, y} -> {x, line - abs(line - y)} end)
  def fold_one(dots, fold), do: dots |> Enum.map(&fold.(&1)) |> Enum.into(MapSet.new())

  @doc """
  Make several folds along horizontal and vertical lines.

  ## Example:

      iex> dots = MapSet.new([{2, 0}, {5, 0}, {1, 1}, {5, 1}, {0, 3}, {5, 3}])
      iex> fold_all([x: 3, y: 2], dots)
      MapSet.new([{1, 0}, {2, 0}, {0, 1}, {1, 1}])
  """
  def fold_all(folds, dots), do: Enum.reduce(folds, dots, &fold_one/2)

  @doc """
  Convert a set of dots to a printable string.

  ## Example:

      iex> dots_to_string(MapSet.new([{1, 0}, {0, 1}, {2, 1}, {1, 2}]))
      " █ \\n█ █\\n █ "
  """
  def dots_to_string(dots) do
    {width, _} = Enum.max_by(dots, &elem(&1, 0))
    {_, height} = Enum.max_by(dots, &elem(&1, 1))

    for y <- 0..height do
      for x <- 0..width do
        if {x, y} in dots, do: "█", else: " "
      end
    end
    |> Enum.map_join("\n", &Enum.join/1)
  end

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
