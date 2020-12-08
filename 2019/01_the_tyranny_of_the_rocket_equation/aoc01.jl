# The Tyranny of the Rocket Equation
#
# Advent of Code 2019, day 1
# Solution by Geir Arne Hjelle, 2020-11-30

using Pipe

# Calculate fuel based on mass
function fuel(mass)
    floor(mass / 3) - 2 |> Int64
end


# Calculate fuel based on mass, include fuel to cover mass of fuel
function recursive_fuel(mass)
    fuel_for_mass = mass |> fuel

    if fuel_for_mass <= 0
        return 0
    else
        return fuel_for_mass + recursive_fuel(fuel_for_mass)
    end
end


# Solve the problem for one file
function solve(filename)
    println("\n$(filename)")

    # Read from file
    input = open(filename) do fid
        @pipe fid |> readlines .|> parse(Int64, _)
    end

    # Part 1
    input .|> fuel |> sum |> println

    # Part 2
    input .|> recursive_fuel |> sum |> println
end


# Run solve on each file
ARGS .|> solve