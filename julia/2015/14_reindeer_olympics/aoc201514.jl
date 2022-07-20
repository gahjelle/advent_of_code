# Advent of Code 2015, day 14: Reindeer Olympics

module AOC201514

using Pipe


struct Reindeer
    name::String
    speed::Int16
    stamina::Int16
    rest::Int16
    period::Int16

    function Reindeer(line)
        m = match(
            (
                r"^(?<name>\w+) can fly (?<speed>\d+) km/s for (?<stamina>\d+) "
                *
                r"seconds, but then must rest for (?<rest>\d+) seconds.$"
            ),
            line,
        )
        attributes = parse.(Int, [m[:speed], m[:stamina], m[:rest]])
        new(m[:name], attributes..., attributes[2:3] |> sum)
    end
end


# Calculate the distance one reindeer flies
function calculate_distance(rd, time=2503)
    periods, leftover = divrem(time, rd.period)
    periods * rd.speed * rd.stamina + rd.speed * min(rd.stamina, leftover)
end

# Calculate the position of one reindeer at all times
function calculate_position(rd, time)
    periods = (time ÷ rd.period) + 1
    period_score = ((1:time) .+ (rd.rest - 1)) .÷ rd.period .* (rd.speed * rd.stamina)
    speed_score = @pipe vcat((1:rd.stamina) .* rd.speed, zeros(rd.rest)) |> repeat(_, periods) |> _[1:time]
    @pipe period_score + speed_score .|> round(Int, _)
end

# Calculate the scores of all reindeers
function calculate_scores(reindeers, time=2503)
    @pipe (
        reindeers
        .|> calculate_position(_, time)
        |> hcat(_...)  # Convert array of arrays to 2D-array
        |> (_ .== maximum(_, dims=2))
        |> sum(_, dims=1)
    )
end

# Parse input
function parse_data(puzzle_input)
    split(puzzle_input, "\n") .|> Reindeer
end

# Solve part 1
function part1(data)
    data .|> calculate_distance |> maximum
end

# Solve part 2
function part2(data)
    data |> calculate_scores |> maximum
end

# Solve the puzzle for the given input
function solve(puzzle_input)
    data = puzzle_input |> parse_data
    part1(data), part2(data)
end


# Solve the problem for one file
function solve_file(file_path)
    "\n$(file_path)" |> println
    open(file_path) do fid
        read(fid, String) |> strip .|> solve
    end
end

# Solve the problem for each file
[a for a in ARGS if a[1] != '-'] .|> solve_file .|> s -> join(s, "\n") |> println

end  # module
