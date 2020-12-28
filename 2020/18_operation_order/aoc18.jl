# Operation Order
#
# Advent of Code 2020, day 18
# Solution by Geir Arne Hjelle, 2020-12-18

module AOC18

using Pipe


function add_to_value(value, op, number)
    if op == '+'
        value + parse(Int, number)
    elseif op == '*'
        value * parse(Int, number)
    end
end

function parse_left_right(expression)
    value, op, number = 0, '+', ""
    for char in expression
        if char ∈ ['+', '*']
            value = add_to_value(value, op, number)
            number = ""
            op = char
        elseif char ∈ "0123456789"
            number = number * char
        end
    end
    add_to_value(value, op, number)
end

function parse_plusses_first(expression)
    while true
        m = match(r"((\d+) [+] (\d+))", expression)
        if m === nothing
            break
        end
        value = parse(Int, m[2]) + parse(Int, m[3])
        expression = replace(expression, m[1] => string(value), count=1)
    end
    parse_left_right(expression)
end

function parse_parens(calculate)
    function _parse_parens(line)
        while true
            # Match unnested parentheses
            m = match(r"(\([^)(]*?\))", line)
            if m === nothing
                break
            end
            value = calculate(m[1][2:end - 1])
            line = replace(line, m[1] => string(value))
        end
        calculate(line)
    end
    _parse_parens
end

# Solve the problem for one file
function solve(input)
    # Parse input
    expressions = split(input, "\n")

    # Part 1
    part_1 = expressions .|> parse_parens(parse_left_right) |> sum

    # Part 2
    part_2 = expressions .|> parse_parens(parse_plusses_first) |> sum

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
