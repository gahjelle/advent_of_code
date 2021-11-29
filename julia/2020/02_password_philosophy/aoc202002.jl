# Advent of Code 2020, day 2: Password Philosophy

module AOC202002

# Parse each line into parts: "{n1}-{n2} {char}: {word}"
function parse_line(line)
    pattern = r"^(?P<n1>\d+)-(?P<n2>\d+) (?P<char>.): (?P<word>.+)$"
    parts = match(pattern, line)
    Dict(
        "num_1" => parse(Int16, parts[:n1]),
        "num_2" => parse(Int16, parts[:n2]),
        "char" => parts[:char][1],
        "word" => parts[:word],
    )
end


# Check password based on first policy: the given character must occur between
# num_1 and num_2 times.
function is_valid_count(parts)
    char, word = parts["char"], parts["word"]
    parts["num_1"] <= count(c -> (c == char), word) <= parts["num_2"]
end


# Check password based on second policy: Exactly one of characters at indices
# num_1 and num_2 must match the given character.
function is_valid_position(parts)
    char, word = parts["char"], parts["word"]
    (word[parts["num_1"]] == char) ⊻ (word[parts["num_2"]] == char)
end

# Parse input
function parse_data(puzzle_input)
    split(puzzle_input, "\n") .|> parse_line
end


# Solve part 1
function part1(data)
    data .|> is_valid_count |> sum
end

# Solve part 2
function part2(data)
    data .|> is_valid_position |> sum
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
