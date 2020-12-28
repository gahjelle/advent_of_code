# The Tyranny of the Rocket Equation
#
# Advent of Code 2019, day 1
# Solution by Geir Arne Hjelle, 2020-11-30

module AOC01

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
function solve(input)
    # Parse input
    masses = @pipe split(input, "\n") .|> parse(Int64, _)

    # Part 1
    part_1 = masses .|> fuel |> sum

    # Part 2
    part_2 = masses .|> recursive_fuel |> sum

    part_1, part_2
end


# Solve the problem for one file
function solve_file(file_path)
    println("\n$(file_path)")
    input = open(file_path) do fid
        read(fid, String) |> strip
    end
    input .|> solve
end

# Solve the problem for each file
[a for a in ARGS if a[1] != '-'] .|> solve_file .|> s -> join(s, "\n") |> println

end  # module
