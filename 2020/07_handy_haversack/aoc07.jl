# Handy Haversack
#
# Advent of Code 2020, day 7
# Solution by Geir Arne Hjelle, 2020-12-29

module AOC07

using Compose: SVG, cm
using GraphPlot: gplot
using LightGraphs: add_edge!, bfs_tree, ne, neighbors
using Pipe
using SimpleWeightedGraphs: SimpleWeightedDiGraph
using SparseArrays: nonzeros

function parse_graph(lines)
    # Read and parse each line
    bags, colors = [], Set()
    for line ∈ lines
        m = match(r"^(?P<outer>[\w ]+) bags contain (?P<inner>[\w ,]+)[.]$", line)
        outer, inner_bags = m[:outer], @pipe m[:inner] |> split(_, ", ")
        push!(colors, outer)
        for inner ∈ inner_bags
            m = match(r"^(?P<number>\d+) (?P<color>[\w ]+) bags?$", inner)
            if m !== nothing
                push!(bags, (outer, m[:color], parse(Int, m[:number])))
                push!(colors, m[:color])
            end
        end
    end

    # Construct a graph with one node per color
    nodes = colors |> enumerate .|> reverse |> Dict
    graph = SimpleWeightedDiGraph(length(nodes))
    for (outer, inner, number) ∈ bags
        add_edge!(graph, nodes[outer], nodes[inner], number)
    end

    # Return the graph and the mapping from node number to color
    graph, Dict(nodes |> values .=> nodes |> keys)
end

function _valid_color(color)
    COLORMAP = Dict(
        "bronze" => "brown",
    )
    @pipe color |> split |> last |> get(COLORMAP, _, _)
end

function draw(graph; colors)
    path = "aoc07_graph.svg"
    size = (length(colors) |> isqrt) * 4cm
    (
        gplot(
            graph,
            nodelabel=(@pipe 1:length(colors) .|> colors[_]),
            nodefillc=(@pipe 1:length(colors) .|> colors[_] .|> _valid_color),
            edgelabel=graph.weights |> nonzeros .|> Int,
        )
        |> SVG(path, size, size)
    )
    "Graph stored in $(path)" |> println
end

function count_bags(graph; bag)
    neighbor_bags = neighbors(graph, bag)
    if isempty(neighbor_bags)
        1
    else
        1 + sum(neighbor_bags) do nb
            count_bags(graph, bag=nb) * Int(graph.weights[nb, bag])
        end
    end
end

# Solve the problem for one file
function solve(input)
    # Parse input
    graph, colors = split(input, "\n") |> parse_graph
    shiny_gold = filter(c -> c.second == "shiny gold", colors) |> keys |> only

    # Draw graph to a file
    if "--draw" ∈ ARGS
        draw(graph, colors=colors)
    end

    # Part 1
    part_1 = bfs_tree(graph, shiny_gold, dir=:in) |> ne

    # Part 2
    part_2 = count_bags(graph, bag=shiny_gold) - 1

    part_1, part_2
end


# Solve the problem for one file
function solve_file(file_path)
    println("\n$(file_path)")
    input = open(file_path) do fid
        read(fid, String) |> strip
    end
    input |> solve
end

# Solve the problem for each file
[a for a in ARGS if a[1] != '-'] .|> solve_file .|> s -> join(s, "\n") |> println

end  # module
