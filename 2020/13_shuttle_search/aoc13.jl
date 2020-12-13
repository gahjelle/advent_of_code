# Shuttle Search
#
# Advent of Code 2020, day 13
# Solution by Geir Arne Hjelle, 2020-12-13

using Pipe

INFINITY = 661  # Highest bus id in my input

function find_first_timestamp(busses)
    other_busses, bus = busses[1:end - 1], busses[end]
    if isempty(other_busses)
        first_timestamp = mod(bus.id - bus.dt, bus.id)
        return bus.id, (first_timestamp + n * bus.id for n in 0:INFINITY)
    end

    step, timestamps = find_first_timestamp(other_busses)
    for timestamp in timestamps
        if (timestamp + bus.dt) % bus.id == 0
            new_step = lcm(step, bus.id)
            return new_step, (timestamp + n * new_step for n in 0:INFINITY)
        end
    end
end

function parse_busses(lines)
    (busses = [
            (id = parse(Int, id), dt = t - 1)
            for (t, id) in enumerate(split(lines[2], ","))
            if id != "x"
        ],
        current_time = (@pipe lines[1] |> parse(Int, _)))
end

# Solve the problem for one file
function solve(filename)
    println("\n$(filename)")

    # Read from file
    input = open(filename) do fid
        fid |> readlines |> parse_busses
    end

    # Part 1
    (
        [(mod(-input.current_time, bus.id), bus.id) for bus in input.busses]
        |> minimum
        |> prod
        |> println
    )

    # Part 2
    @pipe input.busses |> find_first_timestamp |> _[2] |> first |> println
end


# Solve the problem for each file
ARGS .|> solve
