# Password Philosophy
#
# Advent of Code 2020, day 2
# Solution by Geir Arne Hjelle, 2020-12-02

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
function solve(filename)
    println("\n$(filename)")

    # Read from file
    input = open(filename) do fid
        fid |> readlines .|> parse_line
    end

    # Part 1
    input .|> is_valid_1 |> sum |> println

    # Part 2
    input .|> is_valid_2 |> sum |> println
end


# Run solve on each file
ARGS .|> solve
