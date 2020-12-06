#
#
# Advent of Code 2020, day
# Solution by Geir Arne Hjelle, 2020-12-

using Pipe

# Solve the problem for one file
function solve(filename)
    println("\n$(filename)")

    # Read from file
    input = open(filename) do fid
        fid |> readlines
    end

    # Part 1
    println.(input)
end


# Solve the problem for each file
solve.(ARGS)
