# Advent of Code 2020, day 3: Toboggan Trajectory

module AOC202003

using Pipe

# Parse input
function parse_data(puzzle_input)
    @pipe (
        puzzle_input
        |> split
        .|> map(==('#'), collect(_))
        |> hcat(_...)
        |> permutedims
    )
end


# Solve part 1
function part1(slope)
    slope |> count_trees
end


# Solve part 2
function part2(slope)
    [
        count_trees(slope, right=1, down=1),
        count_trees(slope, right=3, down=1),
        count_trees(slope, right=5, down=1),
        count_trees(slope, right=7, down=1),
        count_trees(slope, right=1, down=2),
    ] |> prod
end


# Count the number of trees following the given direction through the slope
function count_trees(slope; right=3, down=1)
    max_y, max_x = size(slope)
    idx_ys = range(1, step=down, stop=max_y)
    idx_xs = @pipe range(1, step=right, length=length(idx_ys)) .|> mod1(_, max_x)

    count(zip(idx_ys, idx_xs)) do (idx_y, idx_x)
        slope[idx_y, idx_x]
    end
end


# Solve the puzzle for the given input
function solve(puzzle_input)
    data = puzzle_input |> parse_data
    part1(data), part2(data)
end


# Solve the problem for one file
function solve_file(file_path)
    "\n$(file_path)" |> println
    open(file_path) do fid
        read(fid, String) |> strip .|> solve
    end
end

# Solve the problem for each file
[a for a in ARGS if a[1] != '-'] .|> solve_file .|> s -> join(s, "\n") |> println

end  # module
