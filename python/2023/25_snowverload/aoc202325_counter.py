"""AoC 25, 2023: Snowverload."""

# Standard library imports
import collections
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    connections = collections.defaultdict(set)
    for line in puzzle_input.split("\n"):
        start, targets = line.split(":")
        for target in targets.split():
            connections[start].add(target)
            connections[target].add(start)

    return connections


def part1(connections):
    """Solve part 1."""
    connections, node1, node2 = cut_wires(connections)

    first = build_graph(connections, node1)
    second = build_graph(connections, node2)
    return len(first) * len(second)


def part2(connections):
    """There is no part 2."""


def cut_wires(connections):
    """Find wires to cut. It should be the three most used connections."""
    graph = {node: build_graph(connections, node) for node in connections}

    c = collections.Counter()
    for paths in graph.values():
        for path in paths.values():
            c.update(path)

    to_cut = c.most_common(3)
    for wire, _ in to_cut:
        first, second = wire.split("-")
        connections[first] -= {second}
        connections[second] -= {first}

    return connections, first, second


def build_graph(connections, start):
    """Build a graph of the connections."""
    graph = {}
    queue = collections.deque([(start, [])])
    while queue:
        node, path = queue.popleft()
        if node in graph:
            continue

        graph[node] = path
        for target in connections[node]:
            queue.append((target, path + ["-".join(sorted([node, target]))]))
    return graph


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
