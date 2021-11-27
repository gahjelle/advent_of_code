defmodule AOC2015.Day05 do
  @moduledoc """
  Advent of Code 2015, day 5: Doesn't He Have Intern-Elves For This?
  """
  require AOC

  @vowels "aeiou"
          |> String.to_charlist()
          |> MapSet.new()

  def parse(puzzle_input) do
    puzzle_input |> String.split("\n") |> Enum.map(&String.to_charlist/1)
  end

  def part1(input) do
    input
    |> Enum.filter(fn s -> count_vowels(s) >= 3 && repeated_char?(s) && not_naughty_pairs?(s) end)
    |> Enum.count()
  end

  defp count_vowels(string), do: Enum.count(string, fn c -> c in @vowels end)

  defp repeated_char?([char, char | _]), do: true
  defp repeated_char?([_ | tail]), do: repeated_char?(tail)
  defp repeated_char?(_), do: false

  defp not_naughty_pairs?([c1, c2 | _]) when [c1, c2] in ['ab', 'cd', 'pq', 'xy'], do: false
  defp not_naughty_pairs?([_ | tail]), do: not_naughty_pairs?(tail)
  defp not_naughty_pairs?(_), do: true

  def part2(input) do
    input
    |> Enum.filter(fn s -> repeated_pair?(s) && split_pair?(s) end)
    |> Enum.count()
  end

  def repeated_pair?(string) do
    case string do
      [c1, c2 | tail] -> repeated_pair?(tail, [c1, c2]) || repeated_pair?([c2 | tail])
      _ -> false
    end
  end

  def repeated_pair?(string, [c1, c2]) do
    case string do
      [t1, t2 | tail] -> (t1 == c1 and t2 == c2) || repeated_pair?([t2 | tail], [c1, c2])
      _ -> false
    end
  end

  defp split_pair?([char, _, char | _]), do: true
  defp split_pair?([_ | tail]), do: split_pair?(tail)
  defp split_pair?(_), do: false

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
