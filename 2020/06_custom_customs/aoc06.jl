# Custom Customs
#
# Advent of Code 2020, day 6
# Solution by Geir Arne Hjelle, 2020-12-06

module AOC06

using Pipe


# Count number of questions to which at least one person answered yes
function count_any(group)
    @pipe group |> split .|> Set |> foldl(union, _) |> length
end


# Count number of questions to which all people answered yes
function count_all(group)
    @pipe group |> split .|> Set |> foldl(intersect, _) |> length
end


# Solve the problem for one file
function solve(input)
    # Parse input
    groups = @pipe input |> split(_, "\n\n")

    # Part 1
    part_1 = groups .|> count_any |> sum

    # Part 2
    part_2 = groups .|> count_all |> sum

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
