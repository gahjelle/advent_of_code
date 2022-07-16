defmodule AOC2018.Day04 do
  @moduledoc """
  Advent of Code 2018, day 4: Repose Record
  """
  require AOC
  import NimbleParsec

  @doc """
  Parse input
  """
  def parse(puzzle_input) do
    puzzle_input
    |> String.split("\n")
    |> Enum.sort()
    |> Enum.map(&parse_log_line/1)
    |> group_by_shifts()
    |> group_by_guards()
  end

  @doc """
  Parse one line from the guard log.

  ## Examples:

      iex> parse_log_line("[1518-11-03 00:05] Guard #10 begins shift")
      {{:guard, 10}, 5}

      iex> parse_log_line("[1518-11-01 00:30] falls asleep")
      {:sleep, 30}

      iex> parse_log_line("[1518-11-04 00:46] wakes up")
      {:wakeup, 46}
  """
  def parse_log_line(log) do
    {:ok, [minute, event], "", %{}, {1, 0}, _} = parsec_log_line(log)
    {event, minute}
  end

  parse_guard =
    ignore(string("Guard #"))
    |> integer(min: 1)
    |> ignore(string(" begins shift"))
    |> unwrap_and_tag(:guard)

  defparsecp(
    :parsec_log_line,
    ignore(string("[1518-"))
    |> ignore(integer(2))
    |> ignore(string("-"))
    |> ignore(integer(2))
    |> ignore(string(" "))
    |> ignore(integer(2))
    |> ignore(string(":"))
    |> integer(2)
    |> ignore(string("] "))
    |> choice([
      parse_guard,
      ignore(string("falls asleep")) |> replace(:sleep),
      ignore(string("wakes up")) |> replace(:wakeup)
    ])
  )

  @doc """
  Group information about each shift.

  ## Examples:

      iex> group_by_shifts(
      ...> [
      ...>   {{:guard, 10}, 0},
      ...>   {:sleep, 5},
      ...>   {:wakeup, 9},
      ...>   {:sleep, 30},
      ...>   {:wakeup, 35},
      ...>   {{:guard, 99}, 58},
      ...>   {:sleep, 40},
      ...>   {:wakeup, 50},
      ...>   {{:guard, 10}, 5},
      ...>   {:sleep, 24},
      ...>   {:wakeup, 29}
      ...> ])
      [
        {10, [5, 6, 7, 8, 30, 31, 32, 33, 34]},
        {99, [40, 41, 42, 43, 44, 45, 46, 47, 48, 49]},
        {10, [24, 25, 26, 27, 28]}
      ]
  """
  def group_by_shifts(events), do: group_by_shifts(events, [])
  def group_by_shifts([], shifts), do: Enum.reverse(shifts)

  def group_by_shifts([{{:guard, guard_id}, _} | events], shifts) do
    {minutes, next_events} = collect_shift(events)
    group_by_shifts(next_events, [{guard_id, minutes} | shifts])
  end

  @doc """
  Collect minutes for one shift.

  ## Example:
      iex> collect_shift([
      ...>   {:sleep, 5},
      ...>   {:wakeup, 8},
      ...>   {:sleep, 30},
      ...>   {:wakeup, 35},
      ...>   {{:guard, 99}, 58}
      ...> ])
      {[5, 6, 7, 30, 31, 32, 33, 34], [{{:guard, 99}, 58}]}
  """
  def collect_shift(events), do: collect_shift(events, [])

  def collect_shift([{:sleep, sleep}, {:wakeup, wakeup} | events], minutes),
    do: collect_shift(events, [sleep..(wakeup - 1) | minutes])

  def collect_shift(events, minutes), do: {minutes |> Enum.concat() |> Enum.sort(), events}

  @doc """
  Group all the shifts by guards and aggregate their sleeping minutes.

  ## Example:

        iex> group_by_guards([
        ...>   {10, [5, 6, 7, 8, 30, 31, 32, 33, 34]},
        ...>   {99, [40, 41, 42, 43, 44, 45, 46, 47, 48, 49]},
        ...>   {10, [24, 25, 26, 27, 28]}
        ...> ])
        %{
          10 => [24, 25, 26, 27, 28, 5, 6, 7, 8, 30, 31, 32, 33, 34],
          99 => [40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
        }
  )
  """
  def group_by_guards(shifts) do
    Enum.reduce(shifts, %{}, fn {guard, minutes}, guards ->
      Map.update(guards, guard, minutes, fn mins -> minutes ++ mins end)
    end)
  end

  @doc """
  Solve part 1
  """
  def part1(input), do: input |> find_heavy_sleeper() |> Tuple.product()

  @doc """
  Solve part 2
  """
  def part2(input), do: input |> find_regular_sleeper() |> Tuple.product()

  @doc """
  Find the guard that sleeps the most and find the minute they're most asleep.

  ## Examples:

      iex> find_heavy_sleeper(%{
      ...>   10 => Enum.concat([24..28, 5..24, 30..54]),
      ...>   99 => Enum.concat([45..54, 36..45, 40..49])
      ...> })
      {10, 24}
  """
  def find_heavy_sleeper(guard_schedules) do
    {guard, minutes} = Enum.max_by(guard_schedules, fn {_, minutes} -> length(minutes) end)
    minute = minutes |> Enum.frequencies() |> Enum.max_by(&elem(&1, 1)) |> elem(0)
    {guard, minute}
  end

  @doc """
  Find the guard that sleeps the most and find the minute they're most asleep.

  ## Examples:

      iex> find_regular_sleeper(%{
      ...>   10 => Enum.concat([24..28, 5..24, 30..54]),
      ...>   99 => Enum.concat([45..54, 36..45, 40..49])
      ...> })
      {99, 45}
  """
  def find_regular_sleeper(guard_schedules) do
    guard_schedules
    |> Enum.map(fn {guard, minutes} ->
      minutes
      |> Enum.frequencies()
      |> Enum.map(fn {minute, count} -> {{guard, minute}, count} end)
    end)
    |> Enum.concat()
    |> Enum.max_by(&elem(&1, 1))
    |> elem(0)
  end

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
