defmodule AOC2015.Day06 do
  @moduledoc """
  Advent of Code 2015, day 6: Probably a Fire Hazard
  """
  require AOC

  def parse(puzzle_input) do
    puzzle_input |> String.split("\n") |> Enum.map(&parse_instruction/1)
  end

  defp parse_instruction(instruction) do
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

  def part1(input) do
    input |> async_map_lights(&flick_light/2) |> Enum.sum()
  end

  def part2(input) do
    input |> async_map_lights(&adjust_light/2) |> Enum.sum()
  end

  defp async_map_lights(instructions, update_fun) do
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

  defp grid_values(instructions) do
    instructions
    |> Enum.reduce({nil, -1, nil, -1}, fn {_, {x_from, y_from}, {x_to, y_to}},
                                          {x_min, x_max, y_min, y_max} ->
      {min(x_min, x_from), max(x_max, x_to), min(y_min, y_from), max(y_max, y_to)}
    end)
  end

  defp flick_light(_value, :on), do: 1
  defp flick_light(_value, :off), do: 0
  defp flick_light(value, :toggle), do: 1 - value

  defp adjust_light(value, :on), do: value + 1
  defp adjust_light(0, :off), do: 0
  defp adjust_light(value, :off), do: value - 1
  defp adjust_light(value, :toggle), do: value + 2

  defp execute_instructions([], _, value, _), do: value

  defp execute_instructions(
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
