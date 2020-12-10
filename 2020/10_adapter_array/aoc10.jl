# Adapter Array
#
# Advent of Code 2020, day 10
# Solution by Geir Arne Hjelle, 2020-12-10

using Pipe
using StatsBase: countmap


# Solve the problem for one file
function solve(filename)
    println("\n$(filename)")

    # Read from file
    input = open(filename) do fid
        @pipe fid |> readlines .|> parse(Int32, _) |> sort
    end

    # Add charger (0) and adapter (max + 3)
    jumps = vcat(0, input, maximum(input) + 3) |> diff

    # Part 1
    @pipe (
        jumps
        |> countmap  # Count occurences of each unique element
        |> [_[1], _[3]]  # Pick out 1 and 3
        |> prod
        |> println
    )

    # Part 2
    @pipe (
        vcat(3, jumps)  # Add 3 in front to control where runs of 1 start
        |> diff
        |> findall(x -> x != 0, _)  # Indices of starts of runs
        |> diff
        |> _[1:2:end]  # Pick out runs of 1s
        |> map(r -> 2^(r-1) - floor(Int, 2.0^(r-4)), _)  # Run lengths to #combinations
        |> prod  # Total number of combinations
        |> println
    )
end


# Solve the problem for each file
ARGS .|> solve
