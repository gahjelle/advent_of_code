# Toboggan Trajectory
#
# Advent of Code 2020, day 3
# Solution by Geir Arne Hjelle, 2020-12-03

module AOC03

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
function solve(input)
    # Parse input
    slope = @pipe (
        input
        |> split
        .|> map(c -> c == '#', collect(_))
        |> hcat(_...)
        |> transpose
    )

    # Part 1
    part_1 = slope |> count_trees

    # Part 2
    part_2 = [
        count_trees(slope, right=1, down=1),
        count_trees(slope, right=3, down=1),
        count_trees(slope, right=5, down=1),
        count_trees(slope, right=7, down=1),
        count_trees(slope, right=1, down=2),
    ] |> prod

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
