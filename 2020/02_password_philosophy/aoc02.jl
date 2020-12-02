# Password Philosophy
#
# Advent of Code 2020, day 2
# Solution by Geir Arne Hjelle, 2020-12-02

"""
    parse_line(line)

Parse each line into parts: "{n1}-{n2} {char}: {word}"
"""
function parse_line(line)
    parts = match(r"^(?P<n1>\d+)-(?P<n2>\d+) (?P<char>.): (?P<word>.+)$", line)
    return Dict(
        "num_1" => parse(Int16, parts[:n1]),
        "num_2" => parse(Int16, parts[:n2]),
        "char" => parts[:char][1],
        "word" => parts[:word],
    )
end


"""
    is_valid_1(parts)

Check password based on first policy: the given character must occur between
num_1 and num_2 times.
"""
function is_valid_1(parts)
    char, word = parts["char"], parts["word"]
    return parts["num_1"] <= count(c -> (c == char), word) <= parts["num_2"]
end


"""
    is_valid_2(parts)

Check password based on second policy: Exactly one of characters at indices
num_1 and num_2 must match the given character.
"""
function is_valid_2(parts)
    char, word = parts["char"], parts["word"]
    return (word[parts["num_1"]] == char) ⊻ (word[parts["num_2"]] == char)
end


"""
    main(filename)

Solve the problem for one file
"""
function main(filename)
    println("\n$(filename)")

    # Read from file
    input = open(filename) do fid
        parse_line.(readlines(fid))
    end

    # Part 1
    println(sum(is_valid_1.(input)))

    # Part 2
    println(sum(is_valid_2.(input)))
end


# Run main on each file
main.(ARGS)
