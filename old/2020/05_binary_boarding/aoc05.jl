# Binary Boarding
#
# Advent of Code 2020, day 5
# Solution by Geir Arne Hjelle, 2020-12-05

module AOC05

using Pipe

PASS2SEATID = Dict('F' => '0', 'B' => '1', 'L' => '0', 'R' => '1')


# Parse a boarding pass into a binary seat ID
function parse_boarding_pass(boarding_pass)
    @pipe boarding_pass |> map(c -> PASS2SEATID[c], _) |> parse(Int16, _, base=2)
end


# Find missing seat IDs in a list of IDs
function find_missing(seat_ids)
    @pipe Set(minimum(seat_ids):maximum(seat_ids)) |> setdiff(_, Set(seat_ids))
end


# Solve the problem for one file
function solve(input)
    # Parse input
    seat_ids = @pipe input |> split .|> parse_boarding_pass

    # Part 1
    part_1 = seat_ids |> maximum

    # Part 2
    part_2 = @pipe seat_ids |> find_missing |> join(_, ", ")

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
