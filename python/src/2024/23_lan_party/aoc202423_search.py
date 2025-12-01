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
    biggest = max(find_all_cliques(graph), key=len)
    return ",".join(sorted(biggest))


def find_threecliques(graph):
    """Find interconnected three-cliques"""
    cliques = set()
    for node, neighbors in graph.items():
        for first, second in itertools.combinations(neighbors, r=2):
            if first in graph[second]:
                cliques.add(frozenset([node, first, second]))
    return cliques


def find_all_cliques(graph):
    """Find all fully interconnected cliques in the graph"""
    cliques = set()
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            clique = [node, neighbor]
            seen = {node, neighbor}
            for new_node in neighbors:
                if new_node in seen:
                    continue
                seen.add(new_node)

                for check in clique:
                    if check not in graph[new_node]:
                        break
                else:
                    clique.append(new_node)
            if len(clique) > 2:
                cliques.add(tuple(sorted(clique)))
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
