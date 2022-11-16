# Rambunctious Recitation
#
# Advent of Code 2020, day 15
# Solution by Geir Arne Hjelle, 2020-12-15

module AOC15

using Pipe


function count(start, num_turns)
    last_counted = zeros(Int32, num_turns + 1)
    for (e, n) in tuple(start...) |> Base.front |> enumerate
        last_counted[n + 1] = e
    end
    previous = start |> last

    for turn in length(start):num_turns - 1
        say = turn - last_counted[previous + 1]
        if say == turn
            say = 0
        end
        last_counted[previous + 1] = turn
        previous = say
    end
    previous
end


# Solve the problem for one file
function solve(input)
    # Parse input
    initial = @pipe split(input, "\n") .|> [parse(Int, n) for n in split(_, ',')]

    # Part 1
    part_1 = @pipe initial .|> count(_, 2020)

    # Part 2
    part_2 = @pipe initial .|> count(_, 30_000_000)

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
