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
    input |> flick_lights() |> Map.values() |> Enum.sum()
  end

  def part2(input) do
    input |> adjust_lights() |> Map.values() |> Enum.sum()
  end

  defp flick_lights(instructions),
    do: execute_instructions(%{}, instructions, &flick_lights/4)

  defp flick_lights(lights, :on, from, to),
    do: update_lights(lights, from, to, 1, fn _ -> 1 end)

  defp flick_lights(lights, :toggle, from, to),
    do: update_lights(lights, from, to, 1, fn lt -> 1 - lt end)

  defp flick_lights(lights, :off, from, to),
    do: update_lights(lights, from, to, 0, fn _ -> 0 end)

  defp adjust_lights(instructions),
    do: execute_instructions(%{}, instructions, &adjust_lights/4)

  defp adjust_lights(lights, :on, from, to),
    do: update_lights(lights, from, to, 1, fn lt -> lt + 1 end)

  defp adjust_lights(lights, :toggle, from, to),
    do: update_lights(lights, from, to, 2, fn lt -> lt + 2 end)

  defp adjust_lights(lights, :off, from, to),
    do:
      update_lights(lights, from, to, 0, fn
        0 -> 0
        lt -> lt - 1
      end)

  defp execute_instructions(lights, [], _),
    do: lights

  defp execute_instructions(lights, [{instruction, from, to} | instructions], update_fun),
    do:
      lights
      |> update_fun.(instruction, from, to)
      |> execute_instructions(instructions, update_fun)

  defp update_lights(lights, {x1, y1}, {x2, y2}, default, fun) do
    Enum.reduce(x1..x2, lights, fn x, acc ->
      Enum.reduce(y1..y2, acc, fn y, acc ->
        Map.update(acc, {x, y}, default, fun)
      end)
    end)
  end

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
