defmodule AOC2022.Day18 do
  @moduledoc """
  Advent of Code 2022, day 18: Boiling Boulders.
  """
  require AOC
  @directions [{-1, 0, 0}, {0, -1, 0}, {0, 0, -1}, {1, 0, 0}, {0, 1, 0}, {0, 0, 1}]

  @doc """
  Parse input.
  """
  def parse(puzzle_input),
    do: puzzle_input |> String.split("\n", trim: true) |> Enum.into(%MapSet{}, &parse_droplet/1)

  def parse_droplet(line),
    do: line |> String.split(",") |> Enum.map(&String.to_integer/1) |> List.to_tuple()

  @doc """
  Solve part 1.
  """
  def part1(droplets), do: droplets |> surface_area()

  @doc """
  Solve part 2.
  """
  def part2(droplets), do: droplets |> exposed_surface_area()

  @doc """
  Find the total surface area of the droplets.

  ## Example:

      iex> surface_area(MapSet.new([{1, 1, 1}, {1, 1, 2}]))
      10
  """
  def surface_area(droplets) do
    droplets
    |> Enum.map(fn droplet ->
      neighbors(droplet) |> Enum.count(&(not MapSet.member?(droplets, &1)))
    end)
    |> Enum.sum()
  end

  @doc """
  Find the surface area that is exposed to the outside.

  ## Example:

      iex> droplets = MapSet.new([{0, 1, 1}, {2, 1, 1}, {1, 0, 1}, {1, 2, 1}, {1, 1, 0}, {1, 1, 2}])
      iex> surface_area(droplets)
      36
      iex> exposed_surface_area(droplets)
      30
  """
  def exposed_surface_area(droplets) do
    water = bounding_box(droplets)

    {_, outside} =
      droplets
      |> all_sides()
      |> Enum.reduce({MapSet.new(), water}, fn droplet, {inside, outside} ->
        exposed_to_water(droplet, droplets, inside, outside)
      end)

    droplets |> all_sides() |> Enum.count(&MapSet.member?(outside, &1))
  end

  @doc """
  Create a bounding box around the droplets.

  ## Examples:

      iex> bounding_box(MapSet.new([{1, 1, 1}])) |> MapSet.size()
      26
      iex> bounding_box(MapSet.new([{1, 1, 1}, {1, 1, 2}])) |> MapSet.size()
      34
  """
  def bounding_box(droplets) do
    xs =
      droplets
      |> Enum.map(&elem(&1, 0))
      |> Enum.min_max()
      |> then(fn {min, max} -> (min - 1)..(max + 1) end)

    ys =
      droplets
      |> Enum.map(&elem(&1, 1))
      |> Enum.min_max()
      |> then(fn {min, max} -> (min - 1)..(max + 1) end)

    zs =
      droplets
      |> Enum.map(&elem(&1, 2))
      |> Enum.min_max()
      |> then(fn {min, max} -> (min - 1)..(max + 1) end)

    [
      for(y <- ys, z <- zs, do: [{xs.first, y, z}, {xs.last, y, z}]),
      for(x <- xs, z <- zs, do: [{x, ys.first, z}, {x, ys.last, z}]),
      for(x <- xs, y <- ys, do: [{x, y, zs.first}, {x, y, zs.last}])
    ]
    |> Enum.flat_map(& &1)
    |> Enum.flat_map(& &1)
    |> Enum.into(MapSet.new())
  end

  @doc """
  Search for a path to the outside.

  ## Examples:

      iex> droplets = MapSet.new([{0, 1, 1}, {2, 1, 1}, {1, 0, 1}, {1, 2, 1}, {1, 1, 0}, {1, 1, 2}])
      iex> water = {-1, -1, -1}
      iex> {inside, outside} = exposed_to_water({1, 1, 1}, droplets, MapSet.new(), MapSet.new([water]))
      iex> inside
      MapSet.new([{1, 1, 1}])
      iex> {inside, outside} = exposed_to_water({0, 1, 1}, droplets, inside, outside)
      iex> MapSet.member?(inside, {0, 1, 1})
      false
      iex> MapSet.member?(outside, {0, 1, 1})
      false
      iex> {inside, outside} = exposed_to_water({2, 2, 2}, droplets, inside, outside)
      iex> MapSet.member?(outside, {2, 2, 2})
      true
      iex> MapSet.intersection(inside, outside)
      MapSet.new()
  """
  def exposed_to_water(start, droplets, inside, outside),
    do:
      exposed_to_water(
        [start],
        droplets,
        inside,
        outside,
        MapSet.new()
      )

  def exposed_to_water([], _, inside, outside, seen),
    do: {MapSet.union(inside, seen), outside}

  def exposed_to_water([current | queue], droplets, inside, outside, seen) do
    cond do
      MapSet.member?(outside, current) ->
        {inside, MapSet.union(outside, seen)}

      MapSet.member?(seen, current) or MapSet.member?(droplets, current) ->
        exposed_to_water(queue, droplets, inside, outside, seen)

      true ->
        exposed_to_water(
          queue ++ neighbors(current),
          droplets,
          inside,
          outside,
          MapSet.put(seen, current)
        )
    end
  end

  @doc """
  List neighbors of a cube.

  ## Example:

      iex> neighbors({1, 2, 3})
      [{0, 2, 3}, {1, 1, 3}, {1, 2, 2}, {2, 2, 3}, {1, 3, 3}, {1, 2, 4}]
  """
  def neighbors({x, y, z}),
    do: @directions |> Enum.map(fn {dx, dy, dz} -> {x + dx, y + dy, z + dz} end)

  @doc """
  List all sides of the droplets.

  ## Example:

      iex> all_sides(MapSet.new([{1, 1, 1}, {2, 1, 1}]))
      [{0, 1, 1}, {1, 0, 1}, {1, 1, 0}, {2, 1, 1}, {1, 2, 1}, {1, 1, 2},
       {1, 1, 1}, {2, 0, 1}, {2, 1, 0}, {3, 1, 1}, {2, 2, 1}, {2, 1, 2}]
  """
  def all_sides(droplets),
    do: for({x, y, z} <- droplets, {dx, dy, dz} <- @directions, do: {x + dx, y + dy, z + dz})

  def main(args) do
    Enum.map(args, fn path -> AOC.solve(path, &parse/1, &part1/1, &part2/1) end)
  end
end
