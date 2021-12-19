defmodule AOC2021.Day18 do
  @moduledoc """
  Advent of Code 2021, day 18: Snailfish
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
    |> Enum.reduce(fn snailfish, acc -> acc |> add(snailfish) |> reduce() end)
    |> magnitude()
  end

  @doc """
  Solve part 2
  """
  def part2(input) do
    input
    |> Task.async_stream(fn second ->
      input
      |> Enum.reject(&(&1 == second))
      |> Enum.map(fn first -> add(first, second) |> reduce() |> magnitude() end)
    end)
    |> Stream.flat_map(fn {:ok, result} -> result end)
    |> Enum.max()
  end

  @doc """
  Add two snailfish numbers

  ## Examples:

      iex> add("[1,2]", "[[3,4],5]")
      "[[1,2],[[3,4],5]]"

      iex> add("[[[[1]]]]", "[2,3]")
      "[[[[[1]]]],[2,3]]"
  """
  def add(first, second), do: "[#{first},#{second}]"

  @doc """
  Reduce a snailfish number using explosions and splits

  ## Example:

      iex> reduce("[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]")
      "[[[[0,7],4],[[7,8],[6,0]]],[8,1]]"
  """
  def reduce(snailfish) do
    idx = explosive_index(snailfish)

    cond do
      idx |> is_number() -> explode(snailfish, idx) |> reduce()
      splitable?(snailfish) -> split(snailfish) |> reduce()
      true -> snailfish
    end
  end

  @doc """
  Find first index where snailfish number can be exploded, otherwise nil

  ## Examples:

      iex> explosive_index("[[1,2]]")
      nil

      iex> explosive_index("[1,[[[[2,3]]]]]")
      7
  """
  def explosive_index(snailfish) do
    snailfish
    |> String.to_charlist()
    |> Enum.reduce_while({0, 0}, fn char, {idx, level} ->
      idx_level =
        case char do
          ?[ -> level + 1
          ?] -> level - 1
          _ -> level
        end

      if idx_level > 4 and char >= ?0 and char <= ?9,
        do: {:halt, {idx, nil}},
        else: {:cont, {idx + 1, idx_level}}
    end)
    |> then(fn {idx, level} ->
      case level do
        nil -> idx
        0 -> nil
      end
    end)
  end

  @doc """
  Explode a snailfish number at the given index

  ## Examples:

      iex> explode("[[[[[9,8],1],2],3],4]", 5)
      "[[[[0,9],2],3],4]"

      iex> explode("[7,[6,[5,[4,[3,2]]]]]", 13)
      "[7,[6,[5,[7,0]]]]"

      iex> explode("[[6,[5,[4,[3,2]]]],1]", 11)
      "[[6,[5,[7,0]]],3]"

      iex> explode("[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]", 11)
      "[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]"

      iex> explode("[[3,[2,[1,[7,13]]]],[6,[5,[4,[3,2]]]]]", 11)
      "[[3,[2,[8,0]]],[19,[5,[4,[3,2]]]]]"

      iex> explode("[[3,[2,[1,[11,3]]]],[6,[5,[4,[3,2]]]]]", 11)
      "[[3,[2,[12,0]]],[9,[5,[4,[3,2]]]]]"
  """
  def explode(snailfish, idx) do
    inds = Regex.scan(~r/\d+/, snailfish, return: :index) |> Enum.map(fn [{idx, _}] -> idx end)

    {num_1, idx_1_end} = number(snailfish, idx)

    idx_2 = inds |> Enum.filter(&(&1 > idx_1_end)) |> Enum.min()
    {num_2, idx_2_end} = number(snailfish, idx_2)

    left_idx = inds |> Enum.filter(&(&1 < idx)) |> Enum.max(fn -> nil end)
    {left, left_idx_end} = number(snailfish, left_idx)

    right_idx = inds |> Enum.filter(&(&1 > idx_2_end)) |> Enum.min(fn -> nil end)
    {right, right_idx_end} = number(snailfish, right_idx)

    len = String.length(snailfish)

    case {left, right} do
      {nil, nil} ->
        String.slice(snailfish, 0..(idx - 2)) <>
          "0" <> String.slice(snailfish, (idx_2_end + 1)..len)

      {nil, _} ->
        String.slice(snailfish, 0..(idx - 2)) <>
          "0" <>
          String.slice(snailfish, (idx_2_end + 1)..(right_idx - 1)) <>
          "#{num_2 + right}" <> String.slice(snailfish, right_idx_end..len)

      {_, nil} ->
        String.slice(snailfish, 0..(left_idx - 1)) <>
          "#{left + num_1}" <>
          String.slice(snailfish, left_idx_end..(idx - 2)) <>
          "0" <>
          String.slice(snailfish, (idx_2_end + 1)..len)

      _ ->
        String.slice(snailfish, 0..(left_idx - 1)) <>
          "#{left + num_1}" <>
          String.slice(snailfish, left_idx_end..(idx - 2)) <>
          "0" <>
          String.slice(snailfish, (idx_2_end + 1)..(right_idx - 1)) <>
          "#{num_2 + right}" <> String.slice(snailfish, right_idx_end..len)
    end
  end

  @doc """
  Parse a number from a string and find its end index

  ## Examples:

      iex> number("[1,2]", 1)
      {1, 2}

      iex> number("[2,3]", nil)
      {nil, nil}

      iex> number("[1,23]", 3)
      {23, 5}
  """
  def number(string, idx) do
    if is_nil(idx) do
      {nil, nil}
    else
      {num, _} = String.slice(string, idx, 3) |> Integer.parse()
      num_len = if num < 10, do: 1, else: 2
      {num, idx + num_len}
    end
  end

  @doc """
  Check if a snailfish number can be split

  ## Examples:

      iex> splitable?("[1,[2,3]]")
      false

      iex> splitable?("[1,[12,3]]")
      true
  """
  def splitable?(snailfish), do: Regex.match?(~r/\d\d/, snailfish)

  @doc """
  Split one two-digit snailfish number

  ## Examples:

      iex> split("10")
      "[5,5]"

      iex> split("[1,[13,5],[7,17]]")
      "[1,[[6,7],5],[7,17]]"
  """
  def split(snailfish), do: Regex.replace(~r/\d\d/, snailfish, &split_number/1, global: false)

  defp split_number(number) do
    first = number |> String.to_integer() |> div(2)
    "[#{first},#{(number |> String.to_integer()) - first}]"
  end

  @doc """
  Calculate the magnitude of a snailfish number

  ## Examples:

      iex> magnitude("[1,2]")
      7

      iex> magnitude("[[1,2],[[3,4],5]]")
      143

      iex> magnitude("", "1", "2")
      "7"
  """
  def magnitude(snailfish) do
    if String.starts_with?(snailfish, "["),
      do: Regex.replace(~r/\[(\d+),(\d+)\]/, snailfish, &magnitude/3) |> magnitude,
      else: snailfish |> String.to_integer()
  end

  def magnitude(_, first, second),
    do: (3 * String.to_integer(first) + 2 * String.to_integer(second)) |> Integer.to_string()

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
