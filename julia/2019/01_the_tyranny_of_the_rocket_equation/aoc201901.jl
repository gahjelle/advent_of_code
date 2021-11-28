# Advent of Code 2019, day 1: The Tyranny of the Rocket Equation

module AOC201901

# Calculate fuel for one module
function fuel(mass)
    mass ÷ 3 - 2
end

# Calculate fuel for one module, including fuel for the fuel
function all_fuel(mass)
    mass_fuel = mass |> fuel
    mass_fuel > 0 ? mass_fuel + all_fuel(mass_fuel) : 0
end

# Parse input
function parse_data(puzzle_input)
    [parse(Int64, n) for n ∈ split(puzzle_input, "\n")]
end

# Solve part 1
function part1(data)
    data .|> fuel |> sum
end

# Solve part 2
function part2(data)
    data .|> all_fuel |> sum
end

# Solve the puzzle for the given input
function solve(puzzle_input)
    data = puzzle_input |> parse_data
    part1(data), part2(data)
end


# Solve the problem for one file
function solve_file(file_path)
    "\n$(file_path)" |> println
    open(file_path) do fid
        read(fid, String) |> strip .|> solve
    end
end

# Solve the problem for each file
[a for a in ARGS if a[1] != '-'] .|> solve_file .|> s -> join(s, "\n") |> println

end  # module
