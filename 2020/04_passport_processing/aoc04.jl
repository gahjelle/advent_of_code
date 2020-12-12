# Passport Processing
#
# Advent of Code 2020, day 4
# Solution by Geir Arne Hjelle, 2020-12-12

using Pipe

struct Height
    value::Union{Int16,Missing}
    unit::String

    function Height(height)
        m = match(r"^(?<value>\d+)(?<unit>(cm|in))$", height)
        if isnothing(m)
            new(missing, height)
        else
            new(parse(Int, m[:value]), m[:unit])
        end
    end
end

Passport = @NamedTuple begin
    byr::Union{Int16,Nothing}
    iyr::Union{Int16,Nothing}
    eyr::Union{Int16,Nothing}
    hgt::Union{Height,Nothing}
    hcl::Union{String,Nothing}
    ecl::Union{String,Nothing}
    pid::Union{String,Nothing}
end

function parse_passport(line)
    fields = @pipe line |> split .|> split(_, ":") |> Dict
    Passport(
        [
            get(fields, "byr", "") |> byr -> tryparse(Int, byr),
            get(fields, "iyr", "") |> iyr -> tryparse(Int, iyr),
            get(fields, "eyr", "") |> eyr -> tryparse(Int, eyr),
            get(fields, "hgt", nothing) |> hgt -> isnothing(hgt) ? nothing : Height(hgt),
            get(fields, "hcl", nothing),
            get(fields, "ecl", nothing),
            get(fields, "pid", nothing),
        ]
    )
end

# Check that all required fields are present in the passport
function required_fields(passport)
    passport |> values .|> isnothing |> !any
end

# Check that the value of each field is valid
function valid_fields(passport)
    @pipe passport |> pairs |> collect |> map(v -> validate(v...), _) |> all
end

# Dispatch on each Passport key
function validate(key, value)
    isnothing(value) ? false : validate(Val(key), value)
end

# Birth Year: four digits; at least 1920 and at most 2002.
function validate(::Val{:byr}, value)
    1920 <= value <= 2002
end

# Issue Year: four digits; at least 2010 and at most 2020.
function validate(::Val{:iyr}, value)
    2010 <= value <= 2020
end

# Expiration Year: four digits; at least 2020 and at most 2030.
function validate(::Val{:eyr}, value)
    2020 <= value <= 2030
end

# Height: a number followed by either cm or in:
#   - If cm, the number must be at least 150 and at most 193.
#   - If in, the number must be at least 59 and at most 76.
function validate(::Val{:hgt}, value)
    if value.unit == "cm"
        150 <= value.value <= 193
    elseif value.unit == "in"
        59 <= value.value <= 76
    else
        false
    end
end

# Hair Color: a # followed by exactly six characters 0-9 or a-f.
function validate(::Val{:hcl}, value)
    occursin(r"^#[0-9a-f]{6}$", value)
end

# Eye Color: exactly one of: amb blu brn gry grn hzl oth.
function validate(::Val{:ecl}, value)
    value in Set(["amb", "blu", "brn", "gry", "grn", "hzl", "oth"])
end

# Passport ID: a nine-digit number, including leading zeroes.
function validate(::Val{:pid}, value)
    occursin(r"^[0-9]{9}$", value)
end

# Solve the problem for one file
function solve(filename)
    println("\n$(filename)")

    # Read from file
    input = open(filename) do fid
        @pipe fid |> readlines |> join(_, "\n") |> split(_, "\n\n")
    end

    # Part 1
    input .|> parse_passport .|> required_fields |> sum |> println

    # Part 2
    input .|> parse_passport .|> valid_fields |> sum |> println
end


# Run solve on each file
ARGS .|> solve
