# Custom Customs
#
# Advent of Code 2020, day 6
# Solution by Geir Arne Hjelle, 2020-12-06

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
function solve(filename)
    println("\n$(filename)")

    # Read from file
    input = open(filename) do fid
        @pipe fid |> readlines |> join(_, "\n") |> split(_, "\n\n")
    end

    # Part 1
    input .|> count_any |> sum |> println

    # Part 2
    input .|> count_all |> sum |> println
end


# Run solve on each file
ARGS .|> solve
