# Seating System
#
# Advent of Code 2020, day 11
# Solution by Geir Arne Hjelle, 2020-12-30

module AOC11

using Pipe


function simulate(seats, los_range, rules)
    flip = Dict('L' => '#', '#' => 'L')
    idxs = findall(s -> s != '.', seats)
    while true
        next_generation = seats |> copy
        for idx in idxs
            if count(==('#'), neighbors(idx, seats, los_range)) ∈ rules[seats[idx]]
                next_generation[idx] = flip[next_generation[idx]]
            end
        end
        next_generation == seats && break
        seats = next_generation
    end
    seats
end

function neighbors(idx, seats, los_range)
    neighbors = []
    for dir ∈ CartesianIndex.([(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)])
        for dist ∈ 1:los_range
            pos = idx + dir * dist
            if checkbounds(Bool, seats, pos) && seats[pos] != '.'
                push!(neighbors, seats[pos])
                break
            end
        end
    end
    neighbors
end

# Solve the problem for one file
function solve(input)
    # Parse input (similar to AOC03)
    seats = @pipe input |> split .|> collect(_) |> hcat(_...) |> permutedims

    # Part 1
    part_1 = @pipe (
        simulate(seats |> copy, 1, Dict('L' => [0], '#' => 4:8))
        |> count(==('#'), _)
    )

    # Part 2
    ∞ = seats |> size |> maximum
    part_2 = @pipe (
        simulate(seats |> copy, ∞, Dict('L' => [0], '#' => 5:8))
        |> count(==('#'), _)
    )

    part_1, part_2
end


# Solve the problem for one file
function solve_file(file_path)
    println("\n$(file_path)")
    input = open(file_path) do fid
        read(fid, String) |> strip
    end
    input |> solve
end

# Solve the problem for each file
[a for a in ARGS if a[1] != '-'] .|> solve_file .|> s -> join(s, "\n") |> println

end  # module
