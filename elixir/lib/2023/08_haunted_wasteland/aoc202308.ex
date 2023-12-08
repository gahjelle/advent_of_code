defmodule AOC2023.Day08 do
  @moduledoc """
  Advent of Code 2023, day 8: Haunted Wasteland.
  """
  require AOC

  @doc """
  Parse input.
  """
  def parse(puzzle_input) do
    [path, nodes] = puzzle_input |> String.split("\n\n", trim: true)

    {path |> String.to_charlist() |> Enum.map(fn char -> if char == ?L, do: 0, else: 1 end),
     nodes
     |> String.replace("(", "")
     |> String.replace(")", "")
     |> String.split("\n", trim: true)
     |> Enum.map(fn line -> line |> String.split(" = ") end)
     |> Enum.map(fn [from, to] -> {from, to |> String.split(", ") |> List.to_tuple()} end)
     |> Enum.into(%{})}
  end

  @doc """
  Solve part 1.
  """
  def part1(data) do
    {path, nodes} = data
    walk_path(nodes, path)
  end

  @doc """
  Solve part 2.
  """
  def part2(data) do
    {path, nodes} = data
    walk_ghost_path(nodes, path)
  end

  @doc """
  Walk a single path from AAA to ZZZ.

  ## Example:

      iex> nodes = %{"AAA" => {"BBB", "BBB"}, "BBB" => {"AAA", "ZZZ"}, "ZZZ" => {"ZZZ", "ZZZ"}}
      iex> walk_path(nodes, [0, 0, 1])
      6
  """
  def walk_path(nodes, directions),
    do: walk_path(nodes, directions, directions, "AAA", 0)

  def walk_path(_nodes, _directions, _path, "ZZZ", num_steps), do: num_steps

  def walk_path(nodes, directions, [], current, num_steps),
    do: walk_path(nodes, directions, directions, current, num_steps)

  def walk_path(nodes, directions, [turn | path], current, num_steps) do
    walk_path(nodes, directions, path, nodes[current] |> elem(turn), num_steps + 1)
  end

  @doc """
  Walk multiple paths from all xxAs to all xxZs.

  ## Example:

      iex> nodes = %{
      ...>     "AAA" => {"11B", "XXX"},
      ...>     "11B" => {"XXX", "ZZZ"},
      ...>     "ZZZ" => {"11B", "XXX"},
      ...>     "22A" => {"22B", "XXX"},
      ...>     "22B" => {"22C", "22C"},
      ...>     "22C" => {"22Z", "22Z"},
      ...>     "22Z" => {"22B", "22B"},
      ...>     "XXX" => {"XXX", "XXX"},
      ...> }
      iex> walk_ghost_path(nodes, [0, 1])
      6
  """
  def walk_ghost_path(nodes, directions) do
    start_nodes = nodes |> Map.keys() |> Enum.filter(fn node -> String.ends_with?(node, "A") end)

    walk_ghost_path(
      nodes,
      directions,
      directions,
      start_nodes,
      start_nodes |> Enum.with_index() |> Enum.map(fn {_, idx} -> {idx, 0} end) |> Enum.into(%{}),
      0
    )
  end

  def walk_ghost_path(nodes, directions, [], current, steps, num_steps),
    do: walk_ghost_path(nodes, directions, directions, current, steps, num_steps)

  def walk_ghost_path(nodes, directions, [turn | path], current, steps, num_steps) do
    steps =
      Enum.reduce(current |> Enum.with_index(), steps, fn {node, idx}, steps ->
        if String.ends_with?(node, "Z"), do: Map.put(steps, idx, num_steps), else: steps
      end)

    if Enum.all?(Map.values(steps), &(&1 > 0)),
      do: steps |> Map.values() |> Enum.reduce(1, fn step, lcm -> Math.lcm(step, lcm) end),
      else:
        walk_ghost_path(
          nodes,
          directions,
          path,
          current |> Enum.map(fn node -> nodes[node] |> elem(turn) end),
          steps,
          num_steps + 1
        )
  end

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
