#
#
# Advent of Code 2020, day
# Solution by Geir Arne Hjelle, 2020-12-

module AOC__

using Pipe

# Solve the problem for one file
function solve(input)
    # Parse input
    stuff = split(input, "\n")

    # Part 1
    part_1 = stuff

    # Part 2
    part_2 = stuff

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
