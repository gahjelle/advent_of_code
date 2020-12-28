# Combo Breaker
#
# Advent of Code 2020, day 25
# Solution by Geir Arne Hjelle, 2020-12-25

module AOC25

using Pipe


function find_first_loopsize(public_keys)
    candidate, value = 1, 1
    while true
        value = (value * 7) % 20201227
        if any(value .== public_keys)
            return candidate, value .!= public_keys 
        end
        candidate += 1
    end
end

function encryption_key(public_key, loop_size)
    value = 1
    for _ in 1:loop_size
        value = (value * public_key) % 20201227
    end
    value
end

# Solve the problem for one file
function solve(input)
    # Parse input
    public_keys = split(input, "\n") .|> keys -> parse(Int, keys)

    # Part 1
    loop_size, idx = find_first_loopsize(public_keys)
    part_1 = encryption_key(public_keys[idx] |> first, loop_size)

    part_1, nothing
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
