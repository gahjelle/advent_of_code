defmodule AOC2018.Day07 do
  @moduledoc """
  Advent of Code 2018, day 7: The Sum of Its Parts
  """
  require AOC

  @doc """
  Parse input
  """
  def parse(puzzle_input) do
    puzzle_input
    |> String.split("\n")
    |> Enum.map(&parse_condition/1)
    |> Enum.reduce(%{}, fn {prereq, step}, acc ->
      Map.update(acc, step, [prereq], &[prereq | &1])
    end)
  end

  @doc """
  Parse one condition.

  ## Example:

      iex> parse_condition("Step C must be finished before step A can begin.")
      {?C, ?A}
  """
  def parse_condition(
        "Step " <> <<prereq>> <> " must be finished before step " <> <<step>> <> " can begin."
      ),
      do: {prereq, step}

  @doc """
  Solve part 1
  """
  def part1(input), do: input |> traverse()

  @doc """
  Solve part 2
  """
  def part2(input, opts \\ [num_workers: 5, steptime: 60]), do: input |> work(opts) |> elem(0)

  @doc """
  Find all nodes in the graph. List them alphabetically.

  ## Example:

      iex> all_nodes(%{?A => 'BD', ?B => 'C', ?D => 'BC'})
      'ABCD'
  """
  def all_nodes(graph) do
    [Map.keys(graph) | Map.values(graph)] |> Enum.concat() |> Enum.uniq() |> Enum.sort()
  end

  @doc """
  Remove one node from all values in a map.

  ## Example:

      iex> remove_node('ABCD', ?C)
      'ABD'

      iex> remove_node(%{?A => 'BD', ?B => 'C', ?D => 'BC'}, ?C)
      %{?A => 'BD', ?D => 'B'}
  """
  def remove_node(nodes, node) when is_list(nodes), do: Enum.reject(nodes, fn n -> n == node end)

  def remove_node(graph, node) when is_map(graph) do
    graph
    |> Enum.map(fn {key, value} -> {key, value |> Enum.reject(fn n -> n == node end)} end)
    |> Enum.reject(fn {_, value} -> value |> Enum.empty?() end)
    |> Map.new()
  end

  @doc """
  Traverse a graph.

  ## Example:

      iex> traverse(%{?A => 'BD', ?B => 'C', ?D => 'BC'})
      'CBDA'
  """
  def traverse(graph), do: traverse(graph, all_nodes(graph), [])
  def traverse(graph, nodes, path) when map_size(graph) == 0, do: Enum.reverse(nodes ++ path)

  def traverse(graph, nodes, path) do
    next_node = nodes |> Enum.find(fn node -> not Map.has_key?(graph, node) end)
    traverse(remove_node(graph, next_node), remove_node(nodes, next_node), [next_node | path])
  end

  @doc """
  Carry out work as specified by a graph.

  ## Examples:

      Second:   Worker 1:   Worker 2:   Done:
        0         C           E
        1         C           E
        2         C           E
        3         A           E         C
        4         .           E         CA
        5         B           D         CAE
        6         B           D         CAE
        7         .           D         CAEB
        8         .           D         CAEB
        9         .           .         CAEBD

      iex> work(%{?A => 'C', ?B => 'AE', ?D => 'CE'}, num_workers: 2, steptime: 0)
      {9, 'CAEBD'}

      Second:   Worker 1:   Worker 2:   Done:
        0         C           E
        1         C           E
        2         C           E
        3         C           E
        4         A           E         C
        5         A           E         C
        6         B           D         CAE
        7         B           D         CAE
        8         B           D         CAE
        9         .           D         CAEB
        10        .           D         CAEB
        11        .           .         CAEBD

      iex> work(%{?A => 'C', ?B => 'AE', ?D => 'AC'}, num_workers: 2, steptime: 1)
      {11, 'CAEBD'}
  """
  def work(graph, opts) do
    Enum.reduce_while(Stream.iterate(0, &(&1 + 1)), new_state(graph, opts), fn count, state ->
      next_state = tick(state)

      if Enum.empty?(next_state.nodes) and Enum.empty?(next_state.processing),
        do: {:halt, {count, next_state.path |> Enum.reverse()}},
        else: {:cont, next_state}
    end)
  end

  defp new_state(graph, opts) do
    %{
      remaining: graph,
      nodes: all_nodes(graph),
      available_workers: Keyword.fetch!(opts, :num_workers),
      processing: [],
      path: [],
      steptime: Keyword.fetch!(opts, :steptime)
    }
  end

  defp tick(state) do
    state |> dismiss_workers() |> engage_workers() |> process_current()
  end

  defp dismiss_workers(state) do
    work_done = for {work, 0} <- state.processing, do: work

    %{
      state
      | remaining: Enum.reduce(work_done, state.remaining, &remove_node(&2, &1)),
        available_workers: state.available_workers + length(work_done),
        processing:
          Enum.reject(state.processing, fn {work, _} -> Enum.member?(work_done, work) end),
        path: Enum.reverse(work_done) ++ state.path
    }
  end

  defp engage_workers(state) do
    new_work = Enum.filter(state.nodes, fn node -> not Map.has_key?(state.remaining, node) end)

    Enum.reduce_while(new_work, state, fn work, current_state ->
      if current_state.available_workers > 0,
        do:
          {:cont,
           %{
             current_state
             | nodes: remove_node(current_state.nodes, work),
               available_workers: current_state.available_workers - 1,
               processing: [
                 {work, current_state.steptime + (work - ?A + 1)}
                 | current_state.processing
               ]
           }},
        else: {:halt, current_state}
    end)
  end

  defp process_current(state) do
    %{
      state
      | processing: Enum.map(state.processing, fn {work, time_left} -> {work, time_left - 1} end)
    }
  end

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
