defmodule AOC2021.Day12 do
  @moduledoc """
  Advent of Code 2021, day 12: Passage Pathing
  """
  require AOC

  @doc """
  Parse input
  """
  def parse(puzzle_input), do: puzzle_input |> String.split() |> Enum.reduce(%{}, &parse_line/2)

  @doc """
  Parse one line of input and add it to the current graph

  ## Examples:

      iex> parse_line("A-bc", %{})
      %{"A" => ["bc"], "bc" => ["A"]}

      iex> parse_line("A-end", %{"A" => ["bc"], "bc" => ["A"]})
      %{"A" => ["end", "bc"], "bc" => ["A"]}
  """
  def parse_line(connection, graph) do
    [from, to] = String.split(connection, "-")
    graph |> add_path(from, to) |> add_path(to, from)
  end

  @doc """
  Add a path between two nodes. Don't add paths to start or from end

  ## Examples:

      iex> add_path(%{}, "start", "A")
      %{"start" => ["A"]}
      iex> add_path(%{}, "start", "end")
      %{"start" => ["end"]}
      iex> add_path(%{}, "end", "A")
      %{}
      iex> add_path(%{}, "A", "start")
      %{}
  """
  def add_path(graph, _from, "start"), do: graph
  def add_path(graph, "end", _to), do: graph
  def add_path(graph, from, to), do: Map.update(graph, from, [to], &[to | &1])

  @doc """
  Solve part 1
  """
  def part1(input), do: input |> find_paths(false) |> length()

  @doc """
  Solve part 2
  """
  def part2(input), do: input |> find_paths(true) |> length()

  @doc """
  Find all possible paths in a graph

  Lowercase rooms can only be passed through once. Uppercase rooms can be visited
  several times.

  ## Example:

            start
            /   \
        c--a-----B--d
            \   /
             end

      iex> graph = parse("start-a\\nstart-B\\na-c\\na-B\\nB-d\\na-end\\nB-end\\n")
      iex> find_paths(graph, false) |> length()
      10
      iex> find_paths(graph, true) |> length()
      36
  """
  def find_paths(graph, extra? \\ false),
    do: find_paths(graph["start"], graph, MapSet.new(), extra?, ["start"], [])

  def find_paths([], _graph, _seen, _extra?, _path, paths), do: paths

  def find_paths(["end" | caves], graph, seen, extra?, path, paths),
    do: find_paths(caves, graph, seen, extra?, path, [Enum.reverse(["end" | path]) | paths])

  def find_paths([cave | caves], graph, seen, extra?, path, paths) do
    paths =
      cond do
        cave in seen and extra? ->
          find_paths(graph[cave], graph, seen, false, [cave | path], paths)

        cave in seen ->
          paths

        small_cave?(cave) ->
          find_paths(graph[cave], graph, MapSet.put(seen, cave), extra?, [cave | path], paths)

        true ->
          find_paths(graph[cave], graph, seen, extra?, [cave | path], paths)
      end

    find_paths(caves, graph, seen, extra?, path, paths)
  end

  @doc """
  Check if cave is small by checking if its name is lower cased

  ## Examples:

      iex> small_cave?("a")
      true
      iex> small_cave?("A")
      false
  """
  def small_cave?(cave) do
    cave |> String.to_charlist() |> Enum.all?(fn c -> c in 'abcdefghijklmnopqrstuvwxyz' end)
  end

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
