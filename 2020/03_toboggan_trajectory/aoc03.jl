# Toboggan Trajectory
#
# Advent of Code 2020, day 3
# Solution by Geir Arne Hjelle, 2020-12-03

module AOC03

using Pipe


# Count the number of trees following the given direction through the slope
function count_trees(slope; right=3, down=1)
    max_y, max_x = size(slope)
    idx_ys = range(1, step=down, stop=max_y)
    idx_xs = @pipe range(1, step=right, length=length(idx_ys)) .|> mod1(_, max_x)

    count(zip(idx_ys, idx_xs)) do (idx_y, idx_x)
        slope[idx_y, idx_x]
    end
end


# Solve the problem for one file
function solve(input)
    # Parse input
    slope = @pipe (
        input
        |> split
        .|> map(==('#'), collect(_))
        |> hcat(_...)
        |> permutedims
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
