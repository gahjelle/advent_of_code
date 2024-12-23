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
            cluster
            for cluster in find_threeclusters(graph)
            if any(node.startswith("t") for node in cluster)
        ]
    )


def part2(graph):
    """Solve part 2."""
    biggest = max(find_all_clusters(graph), key=len)
    return ",".join(sorted(biggest))


def find_threeclusters(graph):
    """Find interconnected three-clusters"""
    clusters = set()
    for node, neighbors in graph.items():
        for first, second in itertools.combinations(neighbors, r=2):
            if first in graph[second]:
                clusters.add(frozenset([node, first, second]))
    return clusters


def find_all_clusters(graph):
    """Find all fully interconnected clusters in the graph"""
    clusters = set()
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            cluster = [node, neighbor]
            seen = {node, neighbor}
            for new_node in neighbors:
                if new_node in seen:
                    continue
                seen.add(new_node)

                for check in cluster:
                    if check not in graph[new_node]:
                        break
                else:
                    cluster.append(new_node)
            if len(cluster) > 2:
                clusters.add(tuple(sorted(cluster)))
    return clusters


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
