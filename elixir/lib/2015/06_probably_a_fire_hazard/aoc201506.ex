defmodule AOC2015.Day06 do
  @moduledoc """
  Advent of Code 2015, day 6: Probably a Fire Hazard
  """
  require AOC

  @doc """
  Parse input
  """
  def parse(puzzle_input) do
    puzzle_input |> String.split("\n") |> Enum.map(&parse_instruction/1)
  end

  @doc """
  Parse one instruction

  ## Examples:

      iex> parse_instruction("turn on 0,1 through 2,3")
      {:on, {0, 1}, {2, 3}}

      iex> parse_instruction("turn off 9,9 through 10,9")
      {:off, {9, 9}, {10, 9}}

      iex> parse_instruction("toggle 20,15 through 20,15")
      {:toggle, {20, 15}, {20, 15}}
  """
  def parse_instruction(instruction) do
    case instruction |> String.split([" ", ","]) do
      ["turn", "on" | tokens] -> {:on, tokens}
      ["toggle" | tokens] -> {:toggle, tokens}
      ["turn", "off" | tokens] -> {:off, tokens}
    end
    |> then(fn {verb, tokens} ->
      {verb, tokens |> Enum.slice(0..1) |> Enum.map(&String.to_integer/1) |> List.to_tuple(),
       tokens |> Enum.slice(3..4) |> Enum.map(&String.to_integer/1) |> List.to_tuple()}
    end)
  end

  @doc """
  Solve part 1
  """
  def part1(input) do
    input |> async_map_lights(&flick_light/2) |> Enum.sum()
  end

  @doc """
  Solve part 2
  """
  def part2(input) do
    input |> async_map_lights(&adjust_light/2) |> Enum.sum()
  end

  @doc """
  Update the lights, distribute tasks asynchronously over X

  ## Example:

      iex> async_map_lights([{:toggle, {1, 1}, {2, 1}}], &adjust_light/2) |> Enum.to_list()
      [2, 2]
  """
  def async_map_lights(instructions, update_fun) do
    {x_min, x_max, y_min, y_max} = instructions |> grid_values()

    x_min..x_max
    |> Task.async_stream(fn x ->
      focused_instructions =
        instructions
        |> Enum.filter(fn {_, {x_from, _}, {x_to, _}} ->
          x_from <= x and x <= x_to
        end)

      y_min..y_max
      |> Enum.map(fn y -> execute_instructions(focused_instructions, y, 0, update_fun) end)
    end)
    |> Stream.flat_map(fn {:ok, result} -> result end)
  end

  @doc """
  Find extent of X and Y values in grid

  ## Example:

      iex> grid_values([{:on, {20, 15}, {999, 333}}, {:off, {19, 77}, {99, 99}}])
      {19, 999, 15, 333}
  """
  def grid_values(instructions) do
    instructions
    |> Enum.reduce({nil, -1, nil, -1}, fn {_, {x_from, y_from}, {x_to, y_to}},
                                          {x_min, x_max, y_min, y_max} ->
      {min(x_min, x_from), max(x_max, x_to), min(y_min, y_from), max(y_max, y_to)}
    end)
  end

  @doc """
  Flick the light switch

  ## Examples:

      iex> flick_light(1, :on)
      1

      iex> flick_light(1, :off)
      0

      iex> flick_light(0, :toggle)
      1
  """
  def flick_light(_value, :on), do: 1
  def flick_light(_value, :off), do: 0
  def flick_light(value, :toggle), do: 1 - value

  @doc """
  Adjust the light level

  ## Examples:

      iex> adjust_light(42, :on)
      43

      iex> adjust_light(42, :off)
      41

      iex> adjust_light(0, :off)
      0

      iex> adjust_light(42, :toggle)
      44
  """
  def adjust_light(value, :on), do: value + 1
  def adjust_light(0, :off), do: 0
  def adjust_light(value, :off), do: value - 1
  def adjust_light(value, :toggle), do: value + 2

  @doc """
  Execute light switch instructions for a given Y

  ## Example:

      iex> execute_instructions([{:toggle, {1, 2}, {2, 3}}], 1, 0, &flick_light/2)
      0

      iex> execute_instructions([{:toggle, {1, 2}, {2, 3}}], 2, 0, &flick_light/2)
      1
  """
  def execute_instructions([], _, value, _), do: value

  def execute_instructions(
        [{instruction, {_, y_from}, {_, y_to}} | instructions],
        y,
        value,
        update_fun
      ) do
    if y_from <= y and y <= y_to do
      execute_instructions(instructions, y, update_fun.(value, instruction), update_fun)
    else
      execute_instructions(instructions, y, value, update_fun)
    end
  end

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
