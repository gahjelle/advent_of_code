defmodule AOC2022.Day05 do
  @moduledoc """
  Advent of Code 2022, day 5: Supply Stacks.
  """
  require AOC

  @doc """
  Parse input.
  """
  def parse(puzzle_input) do
    [crates, moves] = String.split(puzzle_input, "\n\n")
    {parse_crates(crates), parse_moves(moves)}
  end

  @doc """
  Parse the stacks of crates in the input.

  ## Example:

      iex> parse_crates("    [D]    \\n[N] [C]    \\n[Z] [M] [P]\\n 1   2   3 ")
      %{1 => 'NZ', 2 => 'DCM', 3 => 'P'}
  """
  def parse_crates(crates) do
    crates
    |> String.split("\n")
    |> Enum.reverse()
    |> Enum.map(fn crate ->
      1..33//4
      |> Enum.map(fn idx -> String.at(crate, idx) end)
      |> Enum.filter(& &1)
      |> Enum.map(fn char -> char |> String.to_charlist() |> Enum.at(0) end)
    end)
    |> crates_to_stacks()
  end

  defp crates_to_stacks(crates) do
    for(
      line <- crates,
      {crate, stack} <- Enum.with_index(line),
      crate >= ?A,
      do: {stack + 1, crate}
    )
    |> Enum.reduce(%{}, fn {stack, crate}, stacks ->
      Map.update(stacks, stack, [crate], fn top -> [crate | top] end)
    end)
  end

  @doc """
  Parse moves in input.

  ## Example:

      iex> parse_moves("move 1 from 1 to 2\\nmove 42 from 6 to 3")
      [{1, 1, 2}, {42, 6, 3}]
  """
  def parse_moves(moves), do: moves |> String.split("\n") |> Enum.map(&parse_move/1)

  defp parse_move(<<"move ", num, " from ", from, " to ", to>>),
    do: {num - ?0, from - ?0, to - ?0}

  defp parse_move(<<"move ", num1, num2, " from ", from, " to ", to>>),
    do: {(num1 - ?0) * 10 + num2 - ?0, from - ?0, to - ?0}

  @doc """
  Solve part 1.
  """
  def part1({stacks, moves}), do: do_moves(stacks, moves) |> get_stack_tops()

  @doc """
  Solve part 2.
  """
  def part2({stacks, moves}), do: do_moves_multiple(stacks, moves) |> get_stack_tops()

  @doc """
  Do a list of moves on the stacks.

  ## Example:

      iex> stacks = %{1 => 'GAH', 2 => 'A', 3 => 'OC'}
      iex> moves = [{2, 1, 3}, {4, 3, 2}, {1, 2, 1}, {1, 2, 3}]
      iex> do_moves(stacks, [moves |> hd])
      %{1 => 'H', 2 => 'A', 3 => 'AGOC'}
      iex> do_moves(stacks, moves)
      %{1 => 'CH', 2 => 'GAA', 3 => 'O'}
  """
  def do_moves(stacks, []), do: stacks

  def do_moves(stacks, [{num, from, to} | moves]) do
    Enum.reduce(1..num, stacks, fn _, stacks ->
      stacks
      |> Map.update!(from, fn [_ | tail] -> tail end)
      |> Map.update!(to, fn stack -> [stacks[from] |> hd | stack] end)
    end)
    |> do_moves(moves)
  end

  @doc """
  Do a list of moves on the stacks, moving multiple crates at once.

  ## Example:

      iex> stacks = %{1 => 'GAH', 2 => 'A', 3 => 'OC'}
      iex> moves = [{2, 1, 3}, {4, 3, 2}, {1, 2, 1}, {1, 2, 3}]
      iex> do_moves_multiple(stacks, [moves |> hd])
      %{1 => 'H', 2 => 'A', 3 => 'GAOC'}
      iex> do_moves_multiple(stacks, moves)
      %{1 => 'GH', 2 => 'OCA', 3 => 'A'}
  """
  def do_moves_multiple(stacks, []), do: stacks

  def do_moves_multiple(stacks, [{num, from, to} | moves]) do
    {stacks, moved} =
      Enum.reduce(1..num, {stacks, []}, fn _, {stacks, moved} ->
        {stacks
         |> Map.update!(from, fn [_ | tail] -> tail end), [stacks[from] |> hd | moved]}
      end)

    stacks
    |> Map.update!(to, fn stack -> Enum.reverse(moved) ++ stack end)
    |> do_moves_multiple(moves)
  end

  @doc """
  Get the top element of each stack.

  ## Example:

      iex> get_stack_tops(%{1 => 'GH', 2 => 'OCA', 3 => 'A'})
      'GOA'
  """
  def get_stack_tops(stacks), do: get_stack_tops(stacks, 1, [])
  def get_stack_tops(stacks, _, tops) when stacks == %{}, do: tops |> Enum.reverse()

  def get_stack_tops(stacks, key, tops) do
    {[top | _], stacks} = Map.pop!(stacks, key)
    get_stack_tops(stacks, key + 1, [top | tops])
  end

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
