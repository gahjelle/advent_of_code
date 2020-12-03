# Toboggan Trajectory
#
# Advent of Code 2020, day 3
# Solution by Geir Arne Hjelle, 2020-12-03


"""
    count_trees(slope; right=3, down=1)

Count the number of trees following the given direction through the slope
"""
function count_trees(slope; right=3, down=1)
    max_y, max_x = size(slope)
    idx_y, idx_x = 1, 1
    num_trees = 0

    while idx_y <= max_y
        num_trees += slope[idx_y, idx_x]
        idx_y += down
        idx_x += right
        if idx_x > max_x
            idx_x -= max_x
        end
    end
    return num_trees
end


"""
    main(filename)

Solve the problem for one file
"""
function main(filename)
    println("\n$(filename)")

    # Read from file
    input = open(filename) do fid
        transpose(reduce(hcat, [[c == '#' for c in ln] for ln in readlines(fid)]))
    end

    # Part 1
    println(count_trees(input, right=3, down=1))

    # Part 2
    println(
        prod(
            [
                count_trees(input, right=1, down=1),
                count_trees(input, right=3, down=1),
                count_trees(input, right=5, down=1),
                count_trees(input, right=7, down=1),
                count_trees(input, right=1, down=2),
            ]
        )
    )
end


# Run main on each file
main.(ARGS)
