# Reindeer Olympics
#
# Advent of Code 2015, day 14
# Solution by Geir Arne Hjelle, 2020-12-12

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
                * r"seconds, but then must rest for (?<rest>\d+) seconds.$"
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

# Solve the problem for one file
function solve(filename)
    println("\n$(filename)")

    # Read from file
    reindeers = open(filename) do fid
        fid |> readlines .|> Reindeer
    end

    # Part 1
    reindeers .|> calculate_distance |> maximum |> println

    # Part 2
    reindeers |> calculate_scores |> maximum |> println
end


# Solve the problem for each file
ARGS .|> solve
