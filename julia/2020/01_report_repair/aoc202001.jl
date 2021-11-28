# Advent of Code 2020, day 1: Report Repair

module AOC202001

# Parse input
function parse_data(puzzle_input)
    [parse(Int32, n) for n ∈ split(puzzle_input, "\n")] |> Set
end


# Solve part 1
function part1(data)
    data |> find_summands |> prod
end

# Solve part 2
function part2(data)
    summands = nothing
    for first in data
        pairs = find_summands(data, 2020 - first)
        if !isempty(pairs)
            summands = [[first]; pairs]
            break
        end
    end
    summands |> prod
end

function find_summands(numbers, target = 2020)
    [n for n in numbers if target - n ∈ numbers]
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
