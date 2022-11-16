# Aunt Sue
#
# Advent of Code 2015, day 16
# Solution by Geir Arne Hjelle, 2020-12-18

module AOC16

using Pipe


struct Sue
    number::Int16
    children::Union{Int8,Nothing}
    cats::Union{Int8,Nothing}
    samoyeds::Union{Int8,Nothing}
    pomeranians::Union{Int8,Nothing}
    akitas::Union{Int8,Nothing}
    vizslas::Union{Int8,Nothing}
    goldfish::Union{Int8,Nothing}
    trees::Union{Int8,Nothing}
    cars::Union{Int8,Nothing}
    perfumes::Union{Int8,Nothing}

    function Sue(number::Int; items::Dict{String,Int})
        new(
            number,
            get(items, "children", nothing),
            get(items, "cats", nothing),
            get(items, "samoyeds", nothing),
            get(items, "pomeranians", nothing),
            get(items, "akitas", nothing),
            get(items, "vizslas", nothing),
            get(items, "goldfish", nothing),
            get(items, "trees", nothing),
            get(items, "cars", nothing),
            get(items, "perfumes", nothing),
        )
    
    end
end

function Sue(line::String)
    m = match(r"Sue (?P<number>\d+): (?P<items>.+)", line)
    items = (
        m[:items]
        |> s -> split(s, [',', ':'])
        .|> strip
        |> s -> Iterators.partition(s, 2)
        |> Dict
    )
    Sue(
        parse(Int, m[:number]),
        items=Dict(String(k) => parse(Int, v) for (k, v) in items),
    )
end

function ==(aunt::Sue, gift::Sue)
    (
        fieldnames(Sue)
        |> Base.tail  # Skip :number
        |> fs -> map(f -> getfield(aunt, f) ∈ [getfield(gift, f), nothing], fs)
        |> all
    )
end

function retroencabulate(gift::Sue)
    function _retroencabulate(aunt::Sue)
        for field in fieldnames(Sue) |> Base.tail  # Skip :number
            aunt_value, gift_value = getfield(aunt, field), getfield(gift, field)
            if aunt_value === nothing
                continue
            elseif field ∈ [:cats, :trees]
                if aunt_value <= gift_value
                    return false
                end
            elseif field ∈ [:pomeranians, :goldfish]
                if aunt_value >= gift_value
                    return false
                end
            else
                if aunt_value != gift_value
                    return false
                end
            end
        end
        true
    end
end

# Solve the problem for one file
function solve(input)
    # Parse input
    aunts = split(input, "\n") .|> string .|> Sue

    gift = Sue(
        2015,
        items=Dict(
            "children" => 3,
            "cats" => 7,
            "samoyeds" => 2,
            "pomeranians" => 3,
            "akitas" => 0,
            "vizslas" => 0,
            "goldfish" => 5,
            "trees" => 3,
            "cars" => 2,
            "perfumes" => 1,
        )
    )

    # Part 1
    part_1 = @pipe aunts |> filter(aunt -> aunt == gift, _) |> first |> getfield(_, :number)

    # Part 2
    part_2 = @pipe aunts |> filter(retroencabulate(gift), _) |> first |> getfield(_, :number)

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
