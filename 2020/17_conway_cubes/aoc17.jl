# Conway Cubes
#
# Advent of Code 2020, day 17
# Solution by Geir Arne Hjelle, 2021-01-01

module AOC17

using Pipe

function setup_cubes(initial_state, offset; num_dims)
    cubes = falses(fill(2 * offset + size(initial_state, 1), num_dims)...)
    for idx ∈ findall(initial_state)
        row, col = idx.I
        cubes[row + offset, col + offset, fill(offset + 2, num_dims - 2)...] = true
    end
    cubes
end

function evolve!(num_steps)
    function _evolve!(cubes)
        for _ in 1:num_steps
            next_gen = cubes |> copy
            for idx in CartesianIndices(cubes)[((2:s - 1) for s in size(cubes))...]
                num_active = cubes[([-1, 0, 1] .+ i for i ∈ idx.I)...] |> count  # Includes the cell itself
                next_gen[idx] = cubes[idx] ? num_active ∈ [3, 4] : num_active == 3
            end
            cubes = next_gen
        end
        cubes
    end
end

# Solve the problem for one file
function solve(input)
    # Parse input
    initial_state = @pipe (
        input
        |> split
        .|> map(==('#'), collect(_))
        |> hcat(_...)
        |> permutedims
    )
    num_steps = 6

    # Part 1
    part_1 = setup_cubes(initial_state, num_steps, num_dims=3) |> evolve!(num_steps) |> count

    # Part 2
    part_2 = setup_cubes(initial_state, num_steps, num_dims=4) |> evolve!(num_steps) |> count

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
