defmodule AOC2016.Day02 do
  @moduledoc """
  Advent of Code 2016, day 2: Bathroom Security
  """
  require AOC

  @doc """
  Parse input
  """
  def parse(puzzle_input) do
    puzzle_input |> String.split("\n")
  end

  @doc """
  Solve part 1
  """
  def part1(input) do
    input
    |> moves_to_keys(%{
      {-1, 1} => "1",
      {0, 1} => "2",
      {1, 1} => "3",
      {-1, 0} => "4",
      {0, 0} => "5",
      {1, 0} => "6",
      {-1, -1} => "7",
      {0, -1} => "8",
      {1, -1} => "9"
    })
    |> Enum.join()
  end

  @doc """
  Solve part 2
  """
  def part2(input) do
    input
    |> moves_to_keys(%{
      {2, 2} => "1",
      {1, 1} => "2",
      {2, 1} => "3",
      {3, 1} => "4",
      {0, 0} => "5",
      {1, 0} => "6",
      {2, 0} => "7",
      {3, 0} => "8",
      {4, 0} => "9",
      {1, -1} => "A",
      {2, -1} => "B",
      {3, -1} => "C",
      {2, -2} => "D"
    })
    |> Enum.join()
  end

  @doc """
  Convert a list of moves to a list of keys

  ## Examples:

      iex> moves_to_keys(["L", "RUD"], %{{-1, 0} => "1", {0, -1} => "2", {0, 0} => "3"})
      ["1", "2"]
  """
  def moves_to_keys(moves, keypad), do: moves_to_keys(moves, keypad, {0, 0}, [])
  def moves_to_keys([], _keypad, _pos, keys), do: Enum.reverse(keys)

  def moves_to_keys([move | moves], keypad, pos, keys) do
    {new_pos, key} = move |> String.to_charlist() |> make_moves(keypad, pos)
    moves_to_keys(moves, keypad, new_pos, [key | keys])
  end

  @doc """
  Make one sequence of moves

  ## Examples:

      iex> make_moves('UD', %{{-1, 0} => "1", {0, -1} => "2", {0, 0} => "3"}, {0, 0})
      {{0, -1}, "2"}
  """
  def make_moves([], keypad, pos), do: {pos, Map.get(keypad, pos)}

  def make_moves([move | moves], keypad, pos) do
    maybe_pos = make_move(move, pos)
    new_pos = if Map.has_key?(keypad, maybe_pos), do: maybe_pos, else: pos
    make_moves(moves, keypad, new_pos)
  end

  @doc """
  Make one move

  ## Examples:

      iex> make_move(?D, {2, 3})
      {2, 2}
      iex> make_move(?L, {0, 0})
      {-1, 0}
  """
  def make_move(?U, {x, y}), do: {x, y + 1}
  def make_move(?D, {x, y}), do: {x, y - 1}
  def make_move(?L, {x, y}), do: {x - 1, y}
  def make_move(?R, {x, y}), do: {x + 1, y}

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
