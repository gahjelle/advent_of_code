# Jurassic Jigsaw
#
# Advent of Code 2020, day 20
# Solution by Geir Arne Hjelle, 2020-12-20

using Pipe
using StatsBase: countmap

global TILE_SIZE = 8

struct Tile
    id::Int16
    pixels::Array{Bool,2}

    function Tile(lines)
        tile = match(r"Tile (?<id>\d+):", lines[1])
        new(
            parse(Int, tile[:id]),
            (
                lines[2:11]
                |> lns -> [[c == '#' for c in ln] for ln in lns]
                |> a -> hcat(a...)
            )
        )
    end
end

function sea_monster()
    [b == 1 for b in
        [
            0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0;
            1 0 0 0 0 1 1 0 0 0 0 1 1 0 0 0 0 1 1 1;
            0 1 0 0 1 0 0 1 0 0 1 0 0 1 0 0 1 0 0 0;
        ]
    ]
end

function parse_tiles(lines)
    [Tile(lines[i:i + TILE_SIZE + 2]) for i in 1:TILE_SIZE + 4:length(lines)]
end

function fingerprint_line(line::Array{Bool,1})
    @pipe line |> (px ? "1" : "0" for px in _) |> join(_, "") |> parse(Int16, _, base=2)
end

function fingerprint_tile(tile::Tile)
    [
        fingerprint_line(tile.pixels[1, :]),
        fingerprint_line(tile.pixels[:, end]),
        fingerprint_line(tile.pixels[end, :]),
        fingerprint_line(tile.pixels[:, 1]),
        fingerprint_line(tile.pixels[1, :] |> reverse),
        fingerprint_line(tile.pixels[:, end] |> reverse),
        fingerprint_line(tile.pixels[end, :] |> reverse),
        fingerprint_line(tile.pixels[:, 1] |> reverse),
    ]
end

function fingerprint_tiles(tiles::Array{Tile,1})
    Dict(t.id => fingerprint_tile(t) for t in tiles)
end

function find_neighbors(tiles)
    fingerprints = tiles |> fingerprint_tiles
    Dict(
        tile.first => [
            other.first
            for other in fingerprints
            if other.first != tile.first && !isempty(intersect(tile.second, other.second))
        ]
        for tile in fingerprints
    )
end

function count_neighbors(tiles)
    @pipe tiles |> find_neighbors |> Dict(t.first => length(t.second) for t in _)
end

function find_corners(tiles)
    @pipe tiles |> count_neighbors |> filter(n -> n.second == 2, _) |> keys
end

function place_tile(image, row, col, candidates, available)
    tile = intersect(candidates, available |> keys) |> first
    image[row, col] = tile
    pop!(available, tile)
end

function place_tiles(tiles)
    neighbors = tiles |> find_neighbors
    corners = @pipe neighbors |> filter(n -> length(n.second) == 2, _)
    edges = @pipe neighbors |> filter(n -> length(n.second) == 3, _)
    centers = @pipe neighbors |> filter(n -> length(n.second) == 4, _)

    image_size = tiles |> length |> isqrt
    image = zeros(Int, (image_size, image_size))

    for row in 1:image_size
        for col in 1:image_size
            if row == 1 && col == 1
                place_tile(image, row, col, corners |> keys, corners)
            elseif row == 1
                candidates = neighbors[image[row, col - 1]]
                if col == image_size
                    place_tile(image, row, col, candidates, corners)
                else
                    place_tile(image, row, col, candidates, edges)
                end
            elseif col == 1
                candidates = neighbors[image[row - 1, col]]
                if row == image_size
                    place_tile(image, row, col, candidates, corners)
                else
                    place_tile(image, row, col, candidates, edges)
                end
            else
                candidates = intersect(neighbors[image[row, col - 1]], neighbors[image[row - 1, col]])
                if row == image_size && col == image_size
                    place_tile(image, row, col, candidates, corners)
                elseif row == image_size || col == image_size
                    place_tile(image, row, col, candidates, edges)
                else
                    place_tile(image, row, col, candidates, centers)
                end
            end
        end
    end
    image
end

function find_edges(tiles, image, row, col)
    top, right, bottom, left = nothing, nothing, nothing, nothing
    rows, cols = size(image)

    fingerprints = tiles |> fingerprint_tiles
    edges = fingerprints[image[row, col]]

    if row > 1
        top = findfirst(n -> n ∈ intersect(edges, fingerprints[image[row - 1, col]]), edges)
    end

    if col < cols
        right = findfirst(n -> n ∈ intersect(edges, fingerprints[image[row, col + 1]]), edges)
    end

    if row < rows
        bottom = findfirst(n -> n ∈ intersect(edges, fingerprints[image[row + 1, col]]), edges)
    end

    if col > 1
        left = findfirst(n -> n ∈ intersect(edges, fingerprints[image[row, col - 1]]), edges)
    end

    top, right, bottom, left
end

function rotate_cw(pixels)
    @pipe pixels |> _[end:-1:1, 1:end] |> transpose
end

function rotate_ccw(pixels)
    @pipe pixels |> _[1:end, end:-1:1] |> transpose
end

function flip_horizontal(pixels)
    @pipe pixels |> _[1:end, end:-1:1]
end

function flip_vertical(pixels)
    @pipe pixels |> _[end:-1:1, 1:end]
end

function rotate(pixels, top, right, bottom, left)
    rotated = nothing

    if top ∈ [4, nothing] && right ∈ [3, nothing] && bottom ∈ [2, nothing] && left ∈ [1, nothing]
        rotated = pixels |> rotate_cw |> flip_horizontal
    end

    if top ∈ [3, nothing] && right ∈ [2, nothing] && bottom ∈ [1, nothing] && left ∈ [4, nothing]
        rotated = pixels |> flip_vertical
    end

    if top ∈ [2, nothing] && right ∈ [1, nothing] && bottom ∈ [4, nothing] && left ∈ [3, nothing]
        rotated = pixels |> rotate_cw |> flip_vertical
    end

    if top ∈ [1, nothing] && right ∈ [4, nothing] && bottom ∈ [3, nothing] && left ∈ [2, nothing]
        rotated = pixels |> flip_horizontal
    end

    if top ∈ [1, nothing] && right ∈ [2, nothing] && bottom ∈ [3, nothing] && left ∈ [4, nothing]
        rotated = pixels
    end

    if top ∈ [2, nothing] && right ∈ [3, nothing] && bottom ∈ [4, nothing] && left ∈ [1, nothing]
        rotated = pixels |> rotate_ccw
    end

    if top ∈ [3, nothing] && right ∈ [4, nothing] && bottom ∈ [1, nothing] && left ∈ [2, nothing]
        rotated = pixels |> rotate_cw |> rotate_cw
    end

    if top ∈ [4, nothing] && right ∈ [1, nothing] && bottom ∈ [2, nothing] && left ∈ [3, nothing]
        rotated = pixels |> rotate_cw 
    end

    rotated
end

function get_pixels(tiles, image, row, col)
    pixels = @pipe (
        tiles
        |> filter(t -> t.id == image[row, col], _)
        |> first
        |> getfield(_, :pixels)
        |> _[2:end - 1, 2:end - 1]
    )

    rotate(pixels, find_edges(tiles, image, row, col)...)
end

function px_idx(idx)
    (1:TILE_SIZE) .+ (idx - 1) * TILE_SIZE
end

function construct_image(tiles)
    image_tiles = tiles |> place_tiles
    rows, cols = size(image_tiles)
    image = zeros(Bool, (rows * TILE_SIZE, cols * TILE_SIZE))

    for row in 1:rows
        for col in 1:cols
            image[px_idx(row), px_idx(col)] = get_pixels(tiles, image_tiles, row, col)
        end
    end
    image
end

function monsters_exist(image)
    monster = sea_monster()
    m_rows, m_cols = size(monster[2:end, 2:end])
    rows, cols = size(image)

    for row in 1:(rows - m_rows)
        for col in 1:(cols - m_cols)
            if image[row:row + m_rows, col:col + m_cols] .& monster == monster
                return true
            end
        end
    end
    false
end

function rotate_image_to_see_monsters(image)
    rotations = [
        image -> image,
        image -> image |> rotate_cw,
        image -> image |> rotate_cw |> rotate_cw,
        image -> image |> rotate_ccw,
        image -> image |> rotate_cw |> flip_horizontal,
        image -> image |> rotate_cw |> flip_vertical,
        image -> image |> flip_horizontal,
        image -> image |> flip_vertical,
    ]

    for rotation in rotations
        if image |> rotation |> monsters_exist
            return image |> rotation
        end
    end
end

function remove_monsters(image)
    monster = sea_monster()
    m_rows, m_cols = size(monster[2:end, 2:end])
    rows, cols = size(image)

    for row in 1:(rows - m_rows)
        for col in 1:(cols - m_cols)
            if image[row:row + m_rows, col:col + m_cols] .& monster == monster
                image[row:row + m_rows, col:col + m_cols] .-= monster
            end
        end
    end

    image
end

# Solve the problem for one file
function solve(filename)
    println("\n$(filename)")

    # Read from file
    tiles = open(filename) do fid
        fid |> readlines |> parse_tiles
    end

    # Part 1
    tiles |> find_corners |> prod |> println

    # Part 2
    (
        tiles
        |> construct_image
        |> rotate_image_to_see_monsters
        |> remove_monsters
        |> sum
        |> println
    )

    tiles
end


# Solve the problem for each file
ARGS .|> solve
