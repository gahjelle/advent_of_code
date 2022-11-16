# Lobby Layout
#
# Advent of Code 2020, day 24
# Solution by Geir Arne Hjelle, 2020-12-24

module AOC24

using Pipe
using StatsBase: countmap

# Using 3D cube coordinates: https://math.stackexchange.com/a/2643016
DIRECTIONS = Dict(
    "ne" => [1, 0, -1],
    "e" => [1, -1, 0],
    "se" => [0, -1, 1],
    "sw" => [-1, 0, 1],
    "w" => [-1, 1, 0],
    "nw" => [0, 1, -1]
)


function parse_tile(line)
    @pipe line |> findall(r"(e|w|se|sw|ne|nw)", _) |> map(s -> line[s], _) |> map(s -> DIRECTIONS[s], _) |> sum
end


function neighbors(tile)
    @pipe map(d -> tile + d, DIRECTIONS |> values)
end


function step(black, _)
    black_nbs = black .|> neighbors |> n -> hcat(n...) |> countmap

    # All tiles with 2 neighbors and black tiles with 1 neighbor are black the
    # next day
    union(
        filter(n -> n.second == 2, black_nbs) |> keys,
        intersect(black, filter(n -> n.second == 1, black_nbs) |> keys)
    )
end


# Solve the problem for one file
function solve(input)
    # Parse input
    tiles = split(input, "\n") .|> parse_tile

    # Part 1
    black = tiles |> countmap |> t -> filter(p -> isodd(p.second), t) |> keys
    part_1 = black |> length

    # Part 2
    part_2 = reduce(step, 1:100, init=black) |> length

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
