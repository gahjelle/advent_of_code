# Toboggan Trajectory
#
# Advent of Code 2020, day 3
# Solution by Geir Arne Hjelle, 2020-12-03

using Pipe


# Count the number of trees following the given direction through the slope
function count_trees(slope; right=3, down=1)
    max_y, max_x = size(slope)
    idx_y, idx_x = 1, 1
    num_trees = 0

    while idx_y <= max_y
        num_trees += slope[idx_y, idx_x]
        idx_y += down
        idx_x = ((idx_x + right - 1) % max_x) + 1  # +/- 1 since index starts at 1
    end
    num_trees
end


# Solve the problem for one file
function solve(filename)
    println("\n$(filename)")

    # Read from file
    input = open(filename) do fid
        @pipe (
            fid
            |> readlines
            .|> map(c -> c == '#', collect(_))
            |> reduce(hcat, _)
            |> transpose
        )
    end

    # Part 1
    input |> count_trees |> println

    # Part 2
    [
        count_trees(input, right=1, down=1),
        count_trees(input, right=3, down=1),
        count_trees(input, right=5, down=1),
        count_trees(input, right=7, down=1),
        count_trees(input, right=1, down=2),
    ] |> prod |> println
end


# Run solve on each file
ARGS .|> solve
