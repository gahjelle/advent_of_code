# Test outputs of Advent of Code puzzle solutions"""

module AOC2015

using BenchmarkTools
using Pipe

PUZZLE_DIR = @__DIR__
PUZZLES = [
    relpath(dir, PUZZLE_DIR)
    for (dir, _, files) in walkdir(PUZZLE_DIR)
    if "output.jl.txt" ∈ files
]
TIMINGS_LOG = joinpath(PUZZLE_DIR, "timings.jl.md")


function get_puzzle_name(puzzle)
    m = match(r"^(?<day>\d\d)_(?<name>.+)$", puzzle)
    m[:name] |> n -> split(n, "_") .|> uppercasefirst |> n -> join(n, " ")
end


function test_puzzle(puzzle)
    global puzzle_name = get_puzzle_name(puzzle)
    global day = puzzle[1:2]
    global code = joinpath(puzzle, "aoc$(day).jl")
    global mod = Symbol("AOC$(day)")
    global input = open(joinpath(PUZZLE_DIR, puzzle, "input.txt")) do fin
        read(fin, String) |> strip
    end
    global output = open(joinpath(PUZZLE_DIR, puzzle, "output.jl.txt")) do fout
        read(fout, String) |> strip
    end

    include(code)
    @eval begin
        results = AOC2015.$mod.solve(input)
       
        # Test that results are as expected
        expected = @pipe output |> split(_, "\n") |> _[2:end]
        test_pass = (
            length(results) == length(expected)
            && all(results .|> string .== expected)
        ) ? "✔" : "✕"

        # Report time and memory usage
        if "-r" ∈ ARGS || "--report" ∈ ARGS
            bench = @benchmark(AOC2015.$mod.solve(input))
            link = "[$(basename(code))]($(code))"
            runtime = BenchmarkTools.prettytime(time(bench))
            mem = BenchmarkTools.prettymemory(memory(bench))
            open(TIMINGS_LOG, "a") do fid
                write(
                    fid,
                    "| $(parse(Int, day)) | $(puzzle_name) | $(link) | $(runtime) | $(mem) |\n",
                )
            end
        end

        println("$(test_pass) $(parse(Int, day)). $(puzzle_name)")
    end
end


if "-r" ∈ ARGS || "--report" ∈ ARGS
    open(TIMINGS_LOG, "w") do fid
        write(
            fid,
            "| Day | Puzzle | Julia | Time | Memory |\n|:---|:---|:---|---:|---:|\n",
        )
    end
end
for puzzle in PUZZLES
    test_puzzle(puzzle)
end

end
