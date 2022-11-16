# Adapter Array
#
# Advent of Code 2020, day 10
# Solution by Geir Arne Hjelle, 2020-12-10

module AOC10

using Pipe
using StatsBase: countmap

FORBIDDEN = Dict(0 => Set(), 1 => Set(), 2 => Set(), 3 => Set(), 4 => Set(["000"]))


# Count number of combinations for a given run length
function count_combinations(run_length)
    2^(run_length - 1) - length(invalid_combinations(run_length))
end

# Which combinations are invalid because of jumps >= 3
function invalid_combinations(run_length)
    if !(run_length in keys(FORBIDDEN))
        previous = invalid_combinations(run_length - 1)
        FORBIDDEN[run_length] = @pipe [
            Set("0$(p)" for p in previous),
            Set("1$(p)" for p in previous),
            Set("$(p)0" for p in previous),
            Set("$(p)1" for p in previous),
        ] |> foldl(union, _)
    end
    FORBIDDEN[run_length]
end

# Solve the problem for one file
function solve(input)
    # Parse input
    adapters = @pipe split(input, "\n") .|> parse(Int32, _) |> sort

    # Add charger (0) and adapter (max + 3)
    jumps = vcat(0, adapters, maximum(adapters) + 3) |> diff

    # Part 1
    part_1 = @pipe (
        jumps
        |> countmap  # Count occurences of each unique element
        |> [_[1], _[3]]  # Pick out 1 and 3
        |> prod
    )

    # Part 2
    part_2 = @pipe (
        vcat(3, jumps)  # Add 3 in front to control where runs of 1 start
        |> diff
        |> findall(x -> x != 0, _)  # Indices of starts of runs
        |> diff
        |> _[1:2:end]  # Pick out runs of 1s
        |> map(count_combinations, _)
        |> prod  # Total number of combinations
    )

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
