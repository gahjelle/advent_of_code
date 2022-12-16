defmodule AOC2022.Day16 do
  @moduledoc """
  Advent of Code 2022, day 16: Proboscidea Volcanium.
  """
  require AOC

  @doc """
  Parse input.
  """
  def parse(puzzle_input),
    do: puzzle_input |> String.split("\n", trim: true) |> Enum.into(%{}, &parse_valve/1)

  @doc """
  Parse information about one valve.

  ## Examples:

      iex> parse_valve("Valve BB has flow rate=13; tunnels lead to valves CC, AA")
      {"BB", {13, ["CC", "AA"]}}
      iex> parse_valve("Valve HH has flow rate=22; tunnel leads to valve GG")
      {"HH", {22, ["GG"]}}
  """
  def parse_valve(line) do
    [_, valve, rate, valves] =
      Regex.run(
        ~r/^Valve ([A-Z]{2}) has flow rate=(\d+); tunnel.+valves? (.+)$/,
        line
      )

    {valve,
     {rate |> String.to_integer(),
      valves |> String.split(",", trim: true) |> Enum.map(&String.trim/1)}}
  end

  @doc """
  Solve part 1.
  """
  def part1(valves), do: valves |> find_highest_flow("AA", 30) |> elem(1)

  @doc """
  Solve part 2.

  Currently too slow to be practical :(
  """
  def part2(valves),
    do: valves |> find_highest_flow_with_help("AA", 26) |> elem(1)

  @doc """
  Use Dijkstra to find the total risk of the safest path through the grid.

  """
  def find_highest_flow(valves, start, minutes) do
    total_flow = %{{start, 0, %MapSet{}} => 0}
    queue = Heap.max() |> Heap.push({0, 0, start, %MapSet{}})
    dijkstra(valves, total_flow, queue, minutes)
  end

  defp dijkstra(valves, total_flow, queue, minutes) do
    {step, queue} = Heap.split(queue)

    if step == nil do
      total_flow |> Enum.max_by(fn {path, flow} -> {flow, path} end)
    else
      {flow, minute, current, open} = step

      if(minute < minutes) do
        {rate, neighbors} = valves[current]

        {queue, total_flow} =
          if rate > 0 and not MapSet.member?(open, current) do
            new_flow = flow + rate * (minutes - minute - 1)
            queue = Heap.push(queue, {new_flow, minute + 1, current, MapSet.put(open, current)})

            total_flow =
              Map.put(total_flow, {current, minute + 1, MapSet.put(open, current)}, new_flow)

            {queue, total_flow}
          else
            {queue, total_flow}
          end

        {queue, total_flow} =
          for next <- neighbors,
              path = {next, minute + 1, open},
              Map.get(total_flow, path, -1) < flow,
              reduce: {queue, total_flow} do
            {queue, total_flow} ->
              queue = Heap.push(queue, {flow, minute + 1, next, open})
              total_flow = Map.put(total_flow, path, flow)
              {queue, total_flow}
          end

        dijkstra(valves, total_flow, queue, minutes)
      else
        dijkstra(valves, total_flow, queue, minutes)
      end
    end
  end

  def find_highest_flow_with_help(valves, start, minutes) do
    total_flow = %{{{start, start}, 0, 1, %MapSet{}} => 0}
    queue = Heap.max() |> Heap.push({0, 0, 1, {start, start}, %MapSet{}, {%MapSet{}, %MapSet{}}})
    dijkstra2(valves, total_flow, queue, minutes, 0)
  end

  defp dijkstra2(valves, total_flow, queue, minutes, max) do
    {step, queue} = Heap.split(queue)

    if step == nil do
      total_flow |> Enum.max_by(fn {path, flow} -> {flow, path} end)
    else
      {flow, minute, actor, {current1, current2}, open, {since_open1, since_open2}} = step

      if(minute < minutes) do
        if actor == 1 do
          {rate, neighbors} = valves[current1]

          {queue, total_flow} =
            if rate > 0 and not MapSet.member?(open, current1) do
              new_flow = flow + rate * (minutes - minute - 1)

              queue =
                Heap.push(
                  queue,
                  {new_flow, minute, 2, {current1, current2}, MapSet.put(open, current1),
                   {%MapSet{}, since_open2}}
                )

              total_flow =
                Map.put(
                  total_flow,
                  {{current1, current2}, minute, 2, MapSet.put(open, current1)},
                  new_flow
                )

              {queue, total_flow}
            else
              {queue, total_flow}
            end

          {queue, total_flow} =
            for next <- neighbors,
                path = {{next, current2}, minute, 2, open},
                Map.get(total_flow, path, -1) < flow,
                not MapSet.member?(since_open1, next),
                reduce: {queue, total_flow} do
              {queue, total_flow} ->
                queue =
                  Heap.push(
                    queue,
                    {flow, minute, 2, {next, current2}, open,
                     {MapSet.put(since_open1, next), since_open2}}
                  )

                total_flow = Map.put(total_flow, path, flow)
                {queue, total_flow}
            end

          dijkstra2(valves, total_flow, queue, minutes, max)
        else
          {rate, neighbors} = valves[current2]

          {queue, total_flow} =
            if rate > 0 and not MapSet.member?(open, current2) do
              new_flow = flow + rate * (minutes - minute - 1)

              queue =
                Heap.push(
                  queue,
                  {new_flow, minute + 1, 1, {current1, current2}, MapSet.put(open, current2),
                   {since_open1, %MapSet{}}}
                )

              total_flow =
                Map.put(
                  total_flow,
                  {{current1, current2}, minute + 1, 1, MapSet.put(open, current2)},
                  new_flow
                )

              {queue, total_flow}
            else
              {queue, total_flow}
            end

          {queue, total_flow} =
            for next <- neighbors,
                path = {{current1, next}, minute + 1, 1, open},
                Map.get(total_flow, path, -1) < flow,
                reduce: {queue, total_flow} do
              {queue, total_flow} ->
                queue =
                  Heap.push(
                    queue,
                    {flow, minute + 1, 1, {current1, next}, open,
                     {since_open1, MapSet.put(since_open2, next)}}
                  )

                total_flow = Map.put(total_flow, path, flow)
                {queue, total_flow}
            end

          dijkstra2(valves, total_flow, queue, minutes, max)
        end
      else
        max_flow = total_flow |> Map.values() |> Enum.max()
        if max_flow > max, do: IO.inspect({flow, max_flow})
        dijkstra2(valves, total_flow, queue, minutes, Enum.max([max, max_flow]))
      end
    end
  end

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
