# Report Repair
#
# Advent of Code 2020, day 1
# Solution by Geir Arne Hjelle, 2020-12-01

module AOC01

using Pipe

# Find two numbers that add up to target. Will return all numbers that are part
# of such pairs.
function find_adders(numbers, target=2020)
    lookup = Set(numbers)
    [n for n in numbers if target - n ∈ lookup]
end


# Solve the problem for the given input
function solve(input)
    # Parse input
    numbers = @pipe input |> split .|> parse(Int32, _)

    # Part 1
    part_1 = numbers |> find_adders |> prod

    # Part 2
    part_2 = nothing
    for (idx, first) in enumerate(numbers)
        pairs = @pipe numbers[idx + 1:end] |> find_adders(_, 2020 - first)
        if !isempty(pairs)
            part_2 = [[first]; pairs] |> prod
            break
        end
    end
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
