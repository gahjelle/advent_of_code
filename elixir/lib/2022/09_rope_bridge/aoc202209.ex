defmodule AOC2022.Day09 do
  @moduledoc """
  Advent of Code 2022, day 9: Rope Bridge.
  """
  require AOC

  @doc """
  Parse input.
  """
  def parse(puzzle_input) do
    puzzle_input
    |> String.split("\n", trim: true)
    |> Enum.map(&parse_line/1)
    |> moves_to_steps()
  end

  @doc """
  Parse one line of input.

  ## Examples:

      iex> parse_line("D 3")
      {:down, 3}
      iex> parse_line("L 31")
      {:left, 31}
  """
  def parse_line(<<"U ", num::binary>>), do: {:up, String.to_integer(num)}
  def parse_line(<<"D ", num::binary>>), do: {:down, String.to_integer(num)}
  def parse_line(<<"R ", num::binary>>), do: {:right, String.to_integer(num)}
  def parse_line(<<"L ", num::binary>>), do: {:left, String.to_integer(num)}

  @doc """
  Convert a list of moves to list of individual steps.

  ## Example:

      iex> moves_to_steps([{:up, 3}, {:right, 2}, {:down, 1}])
      [:up, :up, :up, :right, :right, :down]
  """
  def moves_to_steps(moves), do: moves_to_steps(moves, [])
  def moves_to_steps([], steps), do: Enum.reverse(steps)
  def moves_to_steps([{_, 0} | moves], steps), do: moves_to_steps(moves, steps)

  def moves_to_steps([{direction, num} | moves], steps),
    do: moves_to_steps([{direction, num - 1} | moves], [direction | steps])

  @doc """
  Solve part 1.
  """
  def part1(moves), do: moves |> move_rope(2) |> hd |> Enum.uniq() |> Enum.count()

  @doc """
  Solve part 2.
  """
  def part2(moves), do: moves |> move_rope(10) |> hd |> Enum.uniq() |> Enum.count()

  @doc """
  Move a rope with n knots.

  ## Example:

      iex> move_rope([:up, :up, :left, :down, :left, :left], 2)
      [[{0, 0}, {0, 0}, {0, 1}, {0, 1}, {0, 1}, {-1, 1}, {-2, 1}],
       [{0, 0}, {0, 1}, {0, 2}, {-1, 2}, {-1, 1}, {-2, 1}, {-3, 1}]]

      iex> move_rope([:up, :up, :left, :down, :left, :left], 3)
      [[{0, 0}, {0, 0}, {0, 0}, {0, 0}, {0, 0}, {0, 0}, {-1, 1}],
       [{0, 0}, {0, 0}, {0, 1}, {0, 1}, {0, 1}, {-1, 1}, {-2, 1}],
       [{0, 0}, {0, 1}, {0, 2}, {-1, 2}, {-1, 1}, {-2, 1}, {-3, 1}]]
  """
  def move_rope(steps, knots), do: move_rope(steps, for(_ <- 1..knots, do: [{0, 0}]), [])
  def move_rope([], [], moved), do: moved |> Enum.map(&Enum.reverse/1)
  def move_rope(steps, [], moved), do: move_rope(steps, Enum.reverse(moved), [])

  def move_rope([step | steps], [[{hx, hy} = head_pos | head] | knots], []) do
    {hx, hy} =
      case step do
        :up -> {hx, hy + 1}
        :down -> {hx, hy - 1}
        :right -> {hx + 1, hy}
        :left -> {hx - 1, hy}
      end

    move_rope(steps, knots, [[{hx, hy}, head_pos | head]])
  end

  def move_rope(steps, [[knot_pos | knot] | knots], [[head_pos | head] | moved]) do
    move_rope(steps, knots, [
      [move_tail(knot_pos, head_pos), knot_pos | knot],
      [head_pos | head] | moved
    ])
  end

  @doc """
  Adjust tail position so that it's next to head.

  ## Examples:

      iex> move_tail({0, 0}, {1, 0})
      {0, 0}
      iex> move_tail({2, 2}, {0, 2})
      {1, 2}
  """
  def move_tail({tx, ty} = tail_pos, {hx, hy}) do
    {dx, dy} = {hx - tx, hy - ty}
    if abs(dx) <= 1 && abs(dy) <= 1, do: tail_pos, else: {tx + sign(dx), ty + sign(dy)}
  end

  defp sign(number), do: if(number > 0, do: 1, else: if(number < 0, do: -1, else: 0))

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
