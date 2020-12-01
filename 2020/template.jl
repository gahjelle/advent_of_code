#
#
# Advent of Code 2020, day
# Solution by Geir Arne Hjelle, 2020-12-


"""
    main(filename)

Solve the problem for one file
"""
function main(filename)
    println("\n$(filename)")

    # Read from file
    input = open(filename) do fid
        parse.(Int64, readlines(fid))
    end

    # Part 1
end


# Run main on each file
main.(ARGS)