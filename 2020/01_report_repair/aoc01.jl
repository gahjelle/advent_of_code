# Report Repair
#
# Advent of Code 2020, day 1
# Solution by Geir Arne Hjelle, 2020-12-01

using Pipe

# Find two numbers that add up to target. Will return all numbers that are part
# of such pairs.
function find_adders(numbers, target=2020)
    lookup = Set(numbers)
    [n for n in numbers if target - n in lookup]
end


# Solve the problem for one file
function solve(filename)
    println("\n$(filename)")

    # Read from file
    input = open(filename) do fid
        @pipe fid |> readlines .|> parse(Int32, _)
    end

    # Part 1
    input |> find_adders |> prod |> println

    # Part 2
    for (idx, first) in enumerate(input)
        pairs = @pipe input[idx + 1:end] |> find_adders(_, 2020 - first)
        if !isempty(pairs)
            [[first]; pairs] |> prod |> println
            break
        end
    end
end


# Run solve on each file
ARGS .|> solve
