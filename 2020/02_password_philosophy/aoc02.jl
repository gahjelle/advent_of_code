# Password Philosophy
#
# Advent of Code 2020, day 2
# Solution by Geir Arne Hjelle, 2020-12-02

module AOC02

using Pipe


# Parse each line into parts: "{n1}-{n2} {char}: {word}"
function parse_line(line)
    pattern = r"^(?P<n1>\d+)-(?P<n2>\d+) (?P<char>.): (?P<word>.+)$"
    parts = @pipe line |> match(pattern, _)
    Dict(
        "num_1" => parse(Int16, parts[:n1]),
        "num_2" => parse(Int16, parts[:n2]),
        "char" => parts[:char][1],
        "word" => parts[:word],
    )
end


# Check password based on first policy: the given character must occur between
# num_1 and num_2 times.
function is_valid_1(parts)
    char, word = parts["char"], parts["word"]
    parts["num_1"] <= count(c -> (c == char), word) <= parts["num_2"]
end


# Check password based on second policy: Exactly one of characters at indices
# num_1 and num_2 must match the given character.
function is_valid_2(parts)
    char, word = parts["char"], parts["word"]
    (word[parts["num_1"]] == char) ⊻ (word[parts["num_2"]] == char)
end


# Solve the problem for one file
function solve(input)
    # Read from file
    passwords = input |> i -> split(i, "\n") .|> parse_line

    # Part 1
    part_1 = passwords .|> is_valid_1 |> sum

    # Part 2
    part_2 = passwords .|> is_valid_2 |> sum

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
