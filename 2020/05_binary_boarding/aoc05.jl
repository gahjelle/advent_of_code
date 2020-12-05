# Binary Boarding
#
# Advent of Code 2020, day 5
# Solution by Geir Arne Hjelle, 2020-12-05

PASS2SEATID = Dict('F' => 0, 'B' => 1', 'L' => 0, 'R' => 1)

"""
    parse_boarding_pass(boarding_pass)

Parse a boarding pass into a binary seat ID
"""
function parse_boarding_pass(boarding_pass)
    return parse(
        Int16,
        join([PASS2SEATID[c] for c in boarding_pass], ""),
        base=2
    )
end


"""
    find_missing(seat_ids)

Find missing seat IDs in a list of IDs
"""
function find_missing(seat_ids)
    all_ids = Set(minimum(seat_ids):maximum(seat_ids))
    return setdiff(all_ids, Set(seat_ids))
end


"""
    main(filename)

Solve the problem for one file
"""
function main(filename)
    println("\n$(filename)")

    # Read from file
    seat_ids = open(filename) do fid
        parse_boarding_pass.(readlines(fid))
    end

    # Part 1
    println(maximum(seat_ids))

    # Part 2
    println(join(find_missing(seat_ids), ", "))
end


# Run main on each file
main.(ARGS)
