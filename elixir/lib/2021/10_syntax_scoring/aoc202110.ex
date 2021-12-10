defmodule AOC2021.Day10 do
  @moduledoc """
  Advent of Code 2021, day 10: Syntax Scoring
  """
  require AOC

  @pairs %{?( => ?), ?[ => ?], ?{ => ?}, ?< => ?>}
  @scores %{?) => 3, ?] => 57, ?} => 1197, ?> => 25_137}
  @chunk_scores %{?) => 1, ?] => 2, ?} => 3, ?> => 4}

  @doc """
  Parse input
  """
  def parse(puzzle_input),
    do: puzzle_input |> String.split("\n") |> Enum.map(&String.to_charlist/1)

  @doc """
  Solve part 1
  """
  def part1(input), do: input |> Enum.map(&illegal_char/1) |> score_chars() |> Enum.sum()

  @doc """
  Solve part 2
  """
  def part2(input) do
    input
    |> Enum.map(&illegal_char/1)
    |> Enum.reject(&Map.has_key?(@scores, &1))
    |> Enum.map(&score_chunk/1)
    |> Statistics.median()
  end

  @doc """
  Find the first illegal character in a corrupt chunk

  ## Example:

      iex> illegal_char('({}>)')
      ?>
  """
  def illegal_char(chunk), do: illegal_char(chunk, [])
  def illegal_char([], seen), do: seen |> Enum.reverse() |> close_chunk()

  def illegal_char([char | chunk], []),
    do: if(Map.has_key?(@pairs, char), do: illegal_char(chunk, [char]), else: char)

  def illegal_char([char | chunk], [prev | seen]) do
    cond do
      Map.has_key?(@pairs, char) -> illegal_char(chunk, [char, prev | seen])
      char == @pairs[prev] -> illegal_char(chunk, seen)
      true -> char
    end
  end

  @doc """
  Close the given chunk

  ## Example:

      iex> close_chunk('<{([')
      '])}>'
  """
  def close_chunk(chunk), do: chunk |> Enum.reduce([], fn char, acc -> [@pairs[char] | acc] end)

  @doc """
  Score illegal characters

  ## Example:

      iex> score_chars([?), ?], ')}])', ?}, ?>, ?)])
      [3, 57, 0, 1197, 25137, 3]
  """
  def score_chars(characters), do: characters |> Enum.map(&Map.get(@scores, &1, 0))

  @doc """
  Score closing chunks

  ## Example:

      iex> score_chunk('])}>')
      294
  """
  def score_chunk(chunk),
    do: chunk |> Enum.reduce(0, fn char, sum -> 5 * sum + @chunk_scores[char] end)

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
