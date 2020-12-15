# Rambunctious Recitation
#
# Advent of Code 2020, day 15
# Solution by Geir Arne Hjelle, 2020-12-15

using Pipe

function count(start, num_turns)
    last_counted = @pipe tuple(start...) |> Base.front |> enumerate |> Dict(n => e for (e, n) in _)
    previous = start |> last

    for turn in length(start):num_turns - 1
        say = turn - get(last_counted, previous, turn)
        last_counted[previous] = turn
        previous = say
    end
    previous
end

# Solve the problem for one file
function solve(filename)
    println("\n$(filename)")

    # Read from file
    input = open(filename) do fid
        @pipe fid |> readlines .|> [parse(Int, n) for n in split(_, ',')]
    end

    # Part 1
    @pipe input .|> count(_, 2020) |> println

    # Part 2
    @pipe input .|> count(_, 30_000_000) |> println
end


# Solve the problem for each file
ARGS .|> solve
