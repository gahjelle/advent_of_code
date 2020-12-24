# Lobby Layout
#
# Advent of Code 2020, day 24
# Solution by Geir Arne Hjelle, 2020-12-24

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
function solve(filename)
    println("\n$(filename)")

    # Read from file
    tiles = open(filename) do fid
        fid |> readlines .|> parse_tile
    end

    # Part 1
    black = tiles |> countmap |> t -> filter(p -> isodd(p.second), t) |> keys
    black |> length |> println

    # Part 2
    reduce(step, 1:100, init=black) |> length |> println
end


# Solve the problem for each file
ARGS .|> solve
