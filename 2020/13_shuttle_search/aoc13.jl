# Shuttle Search
#
# Advent of Code 2020, day 13
# Solution by Geir Arne Hjelle, 2020-12-13

module AOC13

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
function solve(input)
    # Parse input
    schedule = split(input, "\n") |> parse_busses

    # Part 1
    part_1 = (
        [(mod(-schedule.current_time, bus.id), bus.id) for bus in schedule.busses]
        |> minimum
        |> prod
    )

    # Part 2
    part_2 = @pipe schedule.busses |> find_first_timestamp |> _[2] |> first

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
