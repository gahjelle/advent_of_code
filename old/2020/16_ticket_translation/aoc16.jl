# Ticket Translation
#
# Advent of Code 2020, day 16
# Solution by Geir Arne Hjelle, 2020-12-16

module AOC16

using Pipe


function parse_inputs(rules, ticket, tickets)
    (rules |> r -> split(r, "\n") .|> parse_rule |> Dict,
     ticket |> t -> split(t, "\n") |> last |> parse_ticket,
     tickets |> t -> split(t, "\n") |> t -> t[2:end] .|> parse_ticket)
end

function parse_rule(rule)
    m = match(r"^(?P<field>[\w ]+): (?P<s1>\d+)-(?P<e1>\d+) or (?P<s2>\d+)-(?P<e2>\d+)$", rule)
    m[:field], union(Set(parse(Int, m[:s1]):parse(Int, m[:e1])), Set(parse(Int, m[:s2]):parse(Int, m[:e2])))
end

function parse_ticket(ticket)
    @pipe ticket |> split(_, ",") |> map(f -> parse(Int, f), _)
end

function valid(rules)
    all_rules = rules |> values |> r -> foldl(union, r)
    tickets -> [t for t in tickets if setdiff(Set(t), all_rules) |> isempty]
end

function infer_fields(rules)
    candidates = [num => rules |> keys |> Set for num in 1:length(rules)] |> Dict

    # Remove candidates where column values don't match the rules
    function _valid_fields(rules, candidates, tickets)
        for ticket in tickets
            for (column, value) in enumerate(ticket)
                for rule in candidates[column]
                    if value ∉ rules[rule]
                        pop!(candidates[column], rule)
                    end
                end
            end
        end
        candidates
    end

    # Find unique candidates for each column
    function _unique_fields(candidates)
        fields = Dict()
        while !isempty(candidates)
            for (column, names) in candidates
                if length(names) != 1
                    continue
                end

                # We know the name of this field,
                name = pop!(names)
                fields[name] = column
                delete!(candidates, column)

                # Remove this name as a candidate for other columns
                for other in values(candidates)
                    delete!(other, name)
                end
            end
        end
        fields
    end
    
    function _infer_fields(tickets)
        _valid_fields(rules, candidates, tickets) |> _unique_fields
    end
end

function use_values(ticket)
    fields -> [f => ticket[c] for (f, c) in fields] |> Dict
end

# Solve the problem for one file
function solve(input)
    # Parse input
    rules, ticket, tickets = @pipe (
        split(input, "\n")
        |> join(_, "\n")
        |> split(_, "\n\n")
        |> parse_inputs(_...)
    )

    # Part 1
    all_rules = rules |> values |> r -> foldl(union, r)
    part_1 = (
        tickets
        |> t -> foldl(vcat, t)  # Concatenate all ticket values
        |> values -> filter(n -> n ∉ all_rules, values) # Filter out invalid values
        |> sum
    )

    # Part 2
    part_2 = (
        tickets
        |> valid(rules)  # Only keep valid tickets
        |> infer_fields(rules)  # Infer field names from ticket values
        |> use_values(ticket)  # Use values on the ticket
        |> fields -> filter(f -> startswith(first(f), "departure "), fields)  # Look up departures
        |> values
        |> prod
    )

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
