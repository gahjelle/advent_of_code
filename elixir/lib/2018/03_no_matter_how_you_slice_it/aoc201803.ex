defmodule AOC2018.Day03 do
  @moduledoc """
  Advent of Code 2018, day 3: No Matter How You Slice It
  """
  require AOC

  @doc """
  Parse input
  """
  def parse(puzzle_input) do
    puzzle_input |> String.split("\n") |> Enum.map(&parse_claim/1) |> lay_out_claims()
  end

  @doc """
  Parse one claim.

  ## Examples:

      iex> parse_claim("#1 @ 258,327: 19x22")
      {1, {258, 327}, {19, 22}}
  """
  def parse_claim(claim) do
    [id, left, top, width, height] =
      claim
      |> String.split(["#", " @ ", ",", ": ", "x"], trim: true)
      |> Enum.map(&String.to_integer/1)

    {id, {left, top}, {width, height}}
  end

  @doc """
  Lay out all claims.

  ## Examples:

      iex> lay_out_claims([{1, {2, 1}, {2, 2}}, {2, {1, 2}, {2, 1}}])
      %{{2, 1} => [1], {2, 2} => [2, 1], {3, 1} => [1], {3, 2} => [1], {1, 2} => [2]}
  """
  def lay_out_claims(claims), do: lay_out_claims(claims, %{})
  def lay_out_claims([], fabric), do: fabric

  def lay_out_claims([{id, {left, top}, {width, height}} | claims], fabric) do
    lay_out_claims(
      claims,
      Enum.reduce(left..(left + width - 1), fabric, fn x, acc ->
        Enum.reduce(top..(top + height - 1), acc, fn y, acc ->
          Map.update(acc, {x, y}, [id], &[id | &1])
        end)
      end)
    )
  end

  @doc """
  Solve part 1
  """
  def part1(input), do: input |> overlapping_squares() |> Enum.count()

  @doc """
  Solve part 2
  """
  def part2(input), do: input |> nonoverlapping_claim()

  @doc """
  Identify overlapping squares.

  ## Examples:

      iex> overlapping_squares(%{{1, 2} => [2], {2, 1} => [1], {2, 2} => [2, 1]})
      [[2, 1]]
  """
  def overlapping_squares(squares), do: for({_, [_, _ | _] = ids} <- squares, do: ids)

  @doc """
  Identify claim that is not overlapping with other claims.

  ## Examples:

      iex> nonoverlapping_claim(%{{1, 1} => [3], {1, 2} => [2], {2, 1} => [1], {2, 2} => [2, 1]})
      3
  """
  def nonoverlapping_claim(squares) do
    all_claims = squares |> Map.values() |> Enum.concat() |> MapSet.new()
    overlapping_claims = squares |> overlapping_squares() |> Enum.concat() |> MapSet.new()

    MapSet.difference(all_claims, overlapping_claims) |> MapSet.to_list() |> hd()
  end

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
