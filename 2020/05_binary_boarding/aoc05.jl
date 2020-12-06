# Binary Boarding
#
# Advent of Code 2020, day 5
# Solution by Geir Arne Hjelle, 2020-12-05

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
function main(filename)
    println("\n$(filename)")

    # Read from file
    seat_ids = open(filename) do fid
        @pipe fid |> readlines .|> parse_boarding_pass
    end

    # Part 1
    seat_ids |> maximum |> println

    # Part 2
    @pipe seat_ids |> find_missing |> join(_, ", ") |> println
end


# Run main on each file
ARGS .|> main
