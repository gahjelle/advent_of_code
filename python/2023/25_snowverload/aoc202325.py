"""AoC 25, 2023: Snowverload."""

# Standard library imports
import collections
import pathlib
import sys

# Third party imports
import networkx as nx


def parse_data(puzzle_input):
    """Parse input."""
    connections = collections.defaultdict(set)
    for line in puzzle_input.split("\n"):
        start, targets = line.split(":")
        for target in targets.split():
            connections[start].add(target)
            connections[target].add(start)
    print(connections)
    return nx.Graph(connections)


def part1(graph):
    """Solve part 1."""
    graph.remove_edges_from(nx.minimum_edge_cut(graph))
    first, second = nx.connected_components(graph)
    return len(first) * len(second)


def part2(_):
    """There is no part 2."""


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
