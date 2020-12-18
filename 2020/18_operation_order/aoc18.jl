# Operation Order
#
# Advent of Code 2020, day 18
# Solution by Geir Arne Hjelle, 2020-12-18
module AOC
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
function solve(filename)
    println("\n$(filename)")

    # Read from file
    input = open(filename) do fid
        fid |> readlines
    end

    # Part 1
    input .|> parse_parens(parse_left_right) |> sum |> println

    # Part 2
    input .|> parse_parens(parse_plusses_first) |> sum |> println

end


# Solve the problem for each file
ARGS .|> solve
end