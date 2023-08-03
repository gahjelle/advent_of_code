defmodule AOC2018.Day09 do
  @moduledoc """
  Advent of Code 2018, day 9: Marble Mania.

  With apologies to Saša Jurić
  https://github.com/sasa1977/aoc/blob/master/lib/2018/day9.ex
  """
  require AOC
  alias AOC2018.Day09.CircularList

  @doc """
  Parse input.
  """
  def parse(puzzle_input) do
    puzzle_input
    |> String.split(" ")
    |> Enum.map(&Integer.parse/1)
    |> Enum.reject(fn num -> num == :error end)
    |> Enum.map(fn {num, _} -> num end)
    |> List.to_tuple()
  end

  @doc """
  Solve part 1.
  """
  def part1({players, marbles}), do: play(players, marbles) |> max_score()

  @doc """
  Solve part 2.
  """
  def part2({players, marbles}), do: play(players, marbles * 100) |> max_score()

  @doc """
  Play a round of marbles.

  ## Example:

      iex> play(3, 33)
      %{
          player: 1,
          players: 3,
          scores: %{2 => 32},
          state: {
            [33, 13, 3, 14, 7, 15],
            [6, 32, 12, 31, 1, 30, 11, 29, 22, 28, 5, 27, 21, 26, 10, 25, 20, 24, 2, 19, 18, 4, 17, 8, 16, 0]
          }
      }
  """
  def play(players, marbles) do
    1..marbles
    |> Enum.reduce(
      %{state: CircularList.new([0]), player: 1, players: players, scores: %{}},
      &move(&2, &1)
    )
  end

  @doc """
  Make one move in the game of marbles.

  ## Examples:

      iex> move(%{state: {[3], [1, 2, 0]}, player: 2, players: 3, scores: %{}}, 4)
      %{state: {[4, 2, 1, 3], [0]}, player: 0, players: 3, scores: %{}}

      iex> move(%{state: {[4, 2, 1, 3], [0]}, player: 0, players: 3, scores: %{}}, 23)
      %{state: {[], [1, 2, 4, 0]}, player: 1, players: 3, scores: %{0 => 26}}
  """
  def move(game = %{state: state, scores: scores, player: player}, marble)
      when rem(marble, 23) == 0 do
    {score, state} =
      Enum.reduce(1..7, state, fn _, state -> CircularList.previous(state) end)
      |> CircularList.pop()

    %{
      game
      | state: state,
        scores: scores |> Map.update(player, score + marble, &(&1 + score + marble))
    }
    |> next_player()
  end

  def move(game = %{state: state}, marble) do
    state =
      state
      |> CircularList.next()
      |> CircularList.next()
      |> CircularList.insert(marble)

    %{game | state: state} |> next_player()
  end

  @doc """
  Prepare for the next player.

  ## Examples:

      iex> next_player(%{state: {[0], []}, player: 0, players: 3, scores: %{}})
      %{state: {[0], []}, player: 1, players: 3, scores: %{}}

      iex> next_player(%{state: {[0], []}, player: 2, players: 3, scores: %{}})
      %{state: {[0], []}, player: 0, players: 3, scores: %{}}
  """
  def next_player(game = %{player: player, players: players}) do
    %{game | player: rem(player + 1, players)}
  end

  @doc """
  Calculate the max score after a game of marbles.

  ## Example:

      iex> max_score(%{state: {[0], []}, player: 0, players: 3, scores: %{0 => 99, 1 => 77, 2 => 42}})
      99
  """
  def max_score(%{scores: scores}), do: scores |> Map.values() |> Enum.max()

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end

defmodule AOC2018.Day09.CircularList do
  @moduledoc """
  A circular list where the first element follows the last one.

  Implemented as a tuple of lists containing the next elements and the
  elements before the pointer, respectively.
  """

  @doc """
  Create a new circular list.

  ## Example:

      iex> new([1, 2, 3])
      {[1, 2, 3], []}
  """
  def new(elements), do: {elements, []}

  @doc """
  Move to the next element in the list.

  ## Example:

      iex> numbers = new([1, 2, 3])
      iex> next(numbers)
      {[2, 3], [1]}
      iex> numbers |> next() |> next() |> next()
      {[], [3, 2, 1]}
      iex> numbers |> next() |> next() |> next() |> next()
      {[2, 3], [1]}
  """
  def next({[], previous}), do: {Enum.reverse(previous), []} |> next()
  def next({[current | next], previous}), do: {next, [current | previous]}

  @doc """
  Move to the previous element in the list.

  ## Example:

      iex> numbers = new([1, 2, 3])
      iex> previous(numbers)
      {[3], [2, 1]}
      iex> numbers |> previous() |> previous()
      {[2, 3], [1]}
  """
  def previous({next, []}), do: {[], Enum.reverse(next)} |> previous()
  def previous({next, [last | previous]}), do: {[last | next], previous}

  @doc """
  Insert an element into the list.

  ## Example:

      iex> numbers = new([1, 2, 3])
      iex> numbers |> insert(4)
      {[4, 1, 2, 3], []}
      iex> numbers |> next() |> next() |> insert(4)
      {[4, 3], [2, 1]}
  """
  def insert({next, previous}, element), do: {[element | next], previous}

  @doc """
  Pop the current element from the list.

  ## Example:

      iex> numbers = new([1, 2, 3])
      iex> numbers |> pop()
      {1, {[2, 3], []}}
      iex> numbers |> next() |> next() |> pop()
      {3, {[], [2, 1]}}
      iex> numbers |> previous() |> pop()
      {3, {[], [2, 1]}}
  """
  def pop({[], [last | previous]}), do: {last, {[], previous}}
  def pop({[current | next], previous}), do: {current, {next, previous}}
end
