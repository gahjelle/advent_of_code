"""AoC 8, 2023: Haunted Wasteland."""

# Standard library imports
import itertools
import math
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    path, nodes = puzzle_input.split("\n\n")

    return (
        [0 if ch == "L" else 1 for ch in path],
        dict(parse_node(node) for node in nodes.split("\n")),
    )


def parse_node(node):
    """Parse one node of input.

    ## Example:

    >>> parse_node("AAA = (BBB, CCC)")
    ('AAA', ('BBB', 'CCC'))
    """
    start, targets = node.split(" = ")
    return (start, tuple(targets.replace("(", "").replace(")", "").split(", ")))


def part1(data):
    """Solve part 1."""
    path, nodes = data
    return walk_path(nodes, path)


def part2(data):
    """Solve part 2."""
    path, nodes = data
    return walk_ghost_path(nodes, path)


def walk_path(nodes, path):
    """Walk a single path from AAA to ZZZ.

    ## Example:

    >>> nodes = {"AAA": ("BBB", "BBB"), "BBB": ("AAA", "ZZZ"), "ZZZ": ("ZZZ", "ZZZ")}
    >>> walk_path(nodes, [0, 0, 1])
    6
    """
    current = "AAA"
    for num_steps, turn in enumerate(itertools.cycle(path)):
        if current == "ZZZ":
            return num_steps
        current = nodes[current][turn]


def walk_ghost_path(nodes, path):
    """Walk multiple paths from all __As to all __Zs.

    ## Example:

    >>> nodes = {
    ...     "AAA": ("11B", "XXX"),
    ...     "11B": ("XXX", "ZZZ"),
    ...     "ZZZ": ("11B", "XXX"),
    ...     "22A": ("22B", "XXX"),
    ...     "22B": ("22C", "22C"),
    ...     "22C": ("22Z", "22Z"),
    ...     "22Z": ("22B", "22B"),
    ...     "XXX": ("XXX", "XXX"),
    ... }
    >>> walk_ghost_path(nodes, [0, 1])
    6
    """
    current = [node for node in nodes if node.endswith("A")]
    steps = [0 for _ in current]
    for num_steps, turn in enumerate(itertools.cycle(path)):
        for idx, node in enumerate(current):
            if node.endswith("Z") and not steps[idx]:
                steps[idx] = num_steps
                if all(steps):
                    return math.lcm(*steps)
        current = [nodes[node][turn] for node in current]


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
