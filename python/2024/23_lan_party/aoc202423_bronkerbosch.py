"""AoC 23, 2024: LAN Party."""

# Standard library imports
import collections
import itertools
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    connections = collections.defaultdict(set)
    for line in puzzle_input.split("\n"):
        first, second = line.split("-")
        connections[first].add(second)
        connections[second].add(first)
    return connections


def part1(graph):
    """Solve part 1."""
    return len(
        [
            clique
            for clique in find_threecliques(graph)
            if any(node.startswith("t") for node in clique)
        ]
    )


def part2(graph):
    """Solve part 2."""
    biggest = max(find_cliques(graph), key=len)
    return ",".join(sorted(biggest))


def find_threecliques(graph):
    """Find interconnected three-cliques"""
    cliques = set()
    for node, neighbors in graph.items():
        for first, second in itertools.combinations(neighbors, r=2):
            if first in graph[second]:
                cliques.add(frozenset([node, first, second]))
    return cliques


def find_cliques(graph):
    """Find all cliques using Bron-Kerbosch"""
    return bron_kerbosch(graph, set(), set(graph), set(), [])


def bron_kerbosch(graph, clique, to_do, done, cliques):
    r"""Use Bron-Kerbosch to find cliques.

    algorithm BronKerbosch1(R, P, X) is
    if P and X are both empty then
        report R as a maximal clique
    for each vertex v in P do
        BronKerbosch1(R ⋃ {v}, P ⋂ N(v), X ⋂ N(v))
        P := P \ {v}
        X := X ⋃ {v}
    """
    if not to_do and not done:
        cliques.append(clique)
    for node in to_do.copy():
        bron_kerbosch(
            graph, clique | {node}, to_do & graph[node], done & graph[node], cliques
        )
        to_do -= {node}
        done |= {node}
    return cliques


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().rstrip())
        print("\n".join(str(solution) for solution in solutions))
