defmodule AOC2021.Day04 do
  @moduledoc """
  Advent of Code 2021, day 4: Giant Squid
  """
  require AOC

  @doc """
  Parse input
  """
  def parse(puzzle_input) do
    [moves | boards] = puzzle_input |> String.split("\n\n")

    {moves |> String.split(",") |> Enum.map(&String.to_integer/1),
     boards |> Enum.map(&parse_board/1)}
  end

  def parse_board(board) do
    board
    |> String.split("\n")
    |> Enum.map(fn line ->
      line |> String.split() |> Enum.map(&String.to_integer/1) |> Enum.with_index()
    end)
    |> Enum.with_index()
    |> Enum.reduce(
      %{},
      fn {line, row}, acc ->
        line |> Enum.reduce(acc, fn {number, col}, acc -> Map.put(acc, number, {col, row}) end)
      end
    )
  end

  @doc """
  Solve part 1
  """
  def part1(input) do
    input |> play_bingo_to_first() |> calculate_board_score()
  end

  @doc """
  Solve part 2
  """
  def part2(input) do
    input |> play_bingo_to_last() |> calculate_board_score()
  end

  @doc """
  Play bingo on all boards, return the first winning board and move

  ## Example:

      iex> play_bingo_to_first({[0,1,2,3,4,5,6], [%{0 => {1, 0}, 1 => {0, 1}, 3 => {1, 1}, 5 => {0, 0}}]})
      {3, %{0 => nil, 1 => nil, 3 => nil, 5 => {0, 0}}}
  """
  def play_bingo_to_first({moves, boards}), do: play_bingo_to_first(moves, {boards, nil, nil})

  def play_bingo_to_first([move | moves], {boards, nil, nil}),
    do: play_bingo_to_first(moves, play_move(boards, move))

  def play_bingo_to_first(_moves, {_boards, winning_move, winning_board}),
    do: {winning_move, winning_board}

  @doc """
  Play bingo on all boards, return the last board to win and its winning move

  ## Example:

      iex> play_bingo_to_last(
      ...>   {[0, 1, 2, 3, 4, 5, 6],
      ...>    [
      ...>      %{0 => {1, 0}, 1 => {0, 1}, 3 => {1, 1}, 5 => {0, 0}},
      ...>      %{1 => {1, 0}, 2 => {1, 1}, 3 => {0, 1}, 4 => {0, 0}}
      ...>    ]}
      ...> )
      {3, %{0 => nil, 1 => nil, 3 => nil, 5 => {0, 0}}}
  """
  def play_bingo_to_last({moves, boards}), do: play_bingo_to_last(moves, {boards, nil, nil})

  def play_bingo_to_last(_moves, {[], winning_move, winning_board}),
    do: {winning_move, winning_board}

  def play_bingo_to_last([move | moves], {boards, _, _}),
    do: play_bingo_to_last(moves, play_move(boards, move))

  @doc """
  Play a move on all boards, return information about winning boards

  ## Example:

      iex> play_move(
      ...>   [
      ...>     %{0 => {1, 0}, 1 => {0, 1}, 3 => {1, 1}, 5 => {0, 0}},
      ...>     %{1 => {1, 0}, 2 => {1, 1}, 3 => {0, 1}, 4 => {0, 0}}
      ...>   ],
      ...>   1
      ...> )
      {
        [
          %{0 => {1, 0}, 1 => nil, 3 => {1, 1}, 5 => {0, 0}},
          %{1 => nil, 2 => {1, 1}, 3 => {0, 1}, 4 => {0, 0}}
        ],
        nil,
        nil
      }
  """
  def play_move(boards, move) when is_list(boards) do
    boards |> Enum.map(&play_move(&1, move)) |> check_winning_position(move)
  end

  def play_move(board, move) when is_map(board), do: Map.replace(board, move, nil)

  @doc """
  Check if any board in a list represent a winning position

  ## Examples:

      iex> check_winning_position([%{0 => nil, 1 => {0, 1}, 3 => {1, 1}, 5 => {0, 0}}], 0)
      {[%{0 => nil, 1 => {0, 1}, 3 => {1, 1}, 5 => {0, 0}}], nil, nil}

      iex> check_winning_position([%{0 => nil, 1 => nil, 3 => nil, 5 => {0, 0}}], 3)
      {[], 3, %{0 => nil, 1 => nil, 3 => nil, 5 => {0, 0}}}
  """
  def check_winning_position(boards, move) when is_list(boards) do
    {winning, remaining} = boards |> Enum.split_with(&check_winning_position/1)
    winning_board = winning |> Enum.at(0)

    if winning_board, do: {remaining, move, winning_board}, else: {remaining, nil, nil}
  end

  @doc """
  Check if a board represents a winning position

  ## Examples:

      iex> check_winning_position(%{0 => {1, 0}, 1 => {0, 1}, 3 => {1, 1}, 5 => {0, 0}})
      false

      iex> check_winning_position(%{0 => nil, 1 => nil, 3 => {1, 1}, 5 => {0, 0}})
      false

      iex> check_winning_position(%{0 => nil, 1 => nil, 3 => nil, 5 => {0, 0}})
      true
  """
  def check_winning_position(board) when is_map(board) do
    num_lines = board |> Map.keys() |> length() |> :math.sqrt() |> round()
    all_lines = MapSet.new(0..(num_lines - 1))

    {columns, rows} =
      board
      |> Enum.reject(fn {_, pos} -> pos == nil end)
      |> Enum.into(%{})
      |> Map.values()
      |> Enum.unzip()
      |> then(fn {columns, rows} -> {MapSet.new(columns), MapSet.new(rows)} end)

    if MapSet.equal?(all_lines, columns) and MapSet.equal?(all_lines, rows), do: false, else: true
  end

  @doc """
  Calculate the score of a board position

  ## Example:

      iex> calculate_board_score({3, %{0 => nil, 1 => nil, 3 => nil, 5 => {0, 0}}})
      15
  """
  def calculate_board_score({last_move, board}) do
    board_sum =
      board
      |> Enum.flat_map(fn {number, pos} ->
        case pos do
          nil -> []
          _ -> [number]
        end
      end)
      |> Enum.sum()

    last_move * board_sum
  end

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
