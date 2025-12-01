"""AoC 8, 2018: Memory Maneuver."""

# Standard library imports
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    root = map(int, puzzle_input.split())
    return parse_node(root)


def parse_node(memory):
    """Parse a piece of memory into a node."""
    num_children = next(memory)
    num_metadata = next(memory)
    return (
        {idx + 1: parse_node(memory) for idx in range(num_children)},
        [next(memory) for _ in range(num_metadata)],
    )


def part1(root):
    """Solve part 1."""
    return sum_metadata(root)


def part2(root):
    """Solve part 2."""
    return get_value(root)


def sum_metadata(node):
    """Recursively sum the metadata of the given node."""
    children, metadata = node
    return sum(metadata) + sum(sum_metadata(child) for child in children.values())


def get_value(node):
    """Recursively calculate the value of the given node."""
    children, metadata = node
    if not children:
        return sum(metadata)

    return sum(get_value(children.get(idx, ({}, []))) for idx in metadata)


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
