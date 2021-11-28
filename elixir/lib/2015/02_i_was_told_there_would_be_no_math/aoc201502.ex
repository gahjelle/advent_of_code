defmodule AOC2015.Day02 do
  @moduledoc """
  Advent of Code 2015, day 2: I Was Told There Would Be No Math
  """
  require AOC
  alias AOC2015.Day02.Present

  @doc """
  Parse input
  """
  def parse(puzzle_input) do
    puzzle_input
    |> String.split("\n")
    |> Enum.map(&parse_line/1)
  end

  @doc """
  Parse one line of input

  ## Example:

      iex> parse_line("3x9x27")
      %Present{height: 27, length: 3, width: 9}
  """
  def parse_line(line) do
    line
    |> String.split("x")
    |> Enum.map(&String.to_integer/1)
    |> Present.from_list()
  end

  @doc """
  Solve part 1
  """
  def part1(input) do
    input |> Enum.map(&(Present.surface(&1) + Present.smallest_area(&1))) |> Enum.sum()
  end

  @doc """
  Solve part 2
  """
  def part2(input) do
    input |> Enum.map(&(Present.smallest_perimeter(&1) + Present.volume(&1))) |> Enum.sum()
  end

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end

defmodule AOC2015.Day02.Present do
  @moduledoc """
  Struct representing a present
  """
  defstruct length: 0, width: 0, height: 0

  @doc """
  Create a present from a list of dimensions

  ## Example:

      iex> from_list([3, 9, 27])
      %Present{height: 27, length: 3, width: 9}
  """
  def from_list([length, width, height]) do
    struct(__MODULE__, %{:length => length, :width => width, :height => height})
  end

  @doc """
  Calculate area of all surfaces

  ## Example:

      iex> surface(%Present{length: 2, width: 4, height: 8})
      112
  """
  def surface(present) do
    (present.length * present.width + present.length * present.height +
       present.width * present.height) * 2
  end

  @doc """
  List the side lengths of a present

  ## Example:

      iex> sides(%Present{length: 2, width: 4, height: 8}) |> Enum.sort()
      [2, 4, 8]
  """
  def sides(present), do: present |> Map.from_struct() |> Map.values()

  @doc """
  Calculate the volume of a present

  ## Example:

      iex> volume(%Present{length: 2, width: 4, height: 8})
      64
  """
  def volume(present), do: present |> sides() |> Enum.product()

  @doc """
  Sum the side lengths of a present

  ## Example:

      iex> sum_of_sides(%Present{length: 2, width: 4, height: 8})
      14
  """
  def sum_of_sides(present), do: present |> sides() |> Enum.sum()

  @doc """
  Find the longest side length of a present

  ## Example:

      iex> longest_side(%Present{length: 2, width: 4, height: 8})
      8
  """
  def longest_side(present), do: present |> sides() |> Enum.max()

  @doc """
  Find the area of the smallest side of a present

  ## Example:

      iex> smallest_area(%Present{length: 2, width: 4, height: 8})
      8
  """
  def smallest_area(present), do: div(volume(present), longest_side(present))

  @doc """
  Find the smallest perimeter of a present

  ## Example:

      iex> smallest_perimeter(%Present{length: 2, width: 4, height: 8})
      12
  """
  def smallest_perimeter(present), do: (sum_of_sides(present) - longest_side(present)) * 2
end
