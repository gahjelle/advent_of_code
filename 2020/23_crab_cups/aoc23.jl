# Crab Cups
#
# Advent of Code 2020, day 23
# Solution by Geir Arne Hjelle, 2020-12-23

function pick_up(cups)
    vcat(cups[1], cups[5:end]), cups[2:4]
end

function target(cups, num_cups)
    target = cups[1] == 1 ? num_cups : cups[1] - 1
    while target ∉ cups
        target = target == 1 ? num_cups : target - 1
    end
    target
end

function place(cups, target, to_place)
    target_idx = findfirst(n -> n == target, cups)
    vcat(cups[1:target_idx], to_place, cups[target_idx + 1:end])
end

function cycle(cups)
    vcat(cups[2:end], cups[1])
end

function slow_move(cups)
    rest, picked_up = pick_up(cups)
    place(rest, target(rest, length(cups)), picked_up) |> cycle
end

function slow_move(num_times::Int)
    function _move(cups)
        for _ in 1:num_times
            cups = slow_move(cups)
        end
        cups
    end
    _move
end

function label(cups)
    idx = findfirst(n -> n == 1, cups)
    vcat(cups[idx + 1:end], cups[1:idx - 1])
end

function circular(cups)
    zip(cups, vcat(cups[2:end], cups[1])) |> Dict
end

function fast_move(ptr, num_moves)
    function _move(cups)
        max_cup = cups |> values |> maximum

        for _ in 1:num_moves
            pick_up = cups[cups[cups[ptr]]]
            pick_ups = Set([cups[ptr], cups[cups[ptr]], pick_up])
            target = ptr > 1 ? ptr - 1 : max_cup
            while target ∈ pick_ups
                target = target > 1 ? target - 1 : max_cup
            end

            cups[ptr], cups[target], cups[pick_up] = cups[pick_up], cups[ptr], cups[target]
            ptr = cups[ptr]
        end
        cups
    end
    _move
end

function friends_of_1(cups)
    cups[1], cups[cups[1]]
end

# Solve the problem for one file
function solve(filename)
    println("\n$(filename)")

    # Read from file
    cups = open(filename) do fid
        fid |> readlines |> first |> n -> split(n, "") .|> n -> parse(Int, n)
    end

    # Part 1
    cups |> slow_move(100) |> label .|> string |> s -> join(s, "") |> println

    # Part 2
    many_cups = vcat(cups, length(cups) + 1:1_000_000)
    many_cups |> circular |> fast_move(cups[1], 10_000_000) |> friends_of_1 |> prod |> println
end


# Solve the problem for each file
ARGS .|> solve
