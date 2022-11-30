"""AoC 7, 2017: Recursive Circus."""

# Standard library imports
import collections
import pathlib
import statistics
import sys

# Third party imports
import parse

PATTERN_TOP = parse.compile("{name} ({weight:d})")
PATTERN_SUPPORT = parse.compile("{name} ({weight:d}) -> {supported}")


def parse_data(puzzle_input):
    """Parse input."""
    tree, weights = {}, {}
    for line in puzzle_input.split("\n"):
        if match := PATTERN_TOP.parse(line):
            tree[match["name"]] = set()
        elif match := PATTERN_SUPPORT.parse(line):
            tree[match["name"]] = set(match["supported"].split(", "))
        weights[match["name"]] = match["weight"]

    return tree, weights


def part1(data):
    """Solve part 1."""
    tree, _ = data
    return find_root(tree)


def part2(data):
    """Solve part 2."""
    tree, weights = data
    return balance_nodes(tree, weights)


def find_root(tree):
    """Find the root of the tree as the only node that is not a child.

    >>> find_root({"a": {"b", "c"}, "b": set(), "c": set()})
    'a'
    """
    return (set(tree) - set.union(*tree.values())).pop()


def node_weight(node, tree, weights):
    """Calculate the total weight of a node, including its children.

    >>> node_weight("a", {"a": {"b", "c"}, "b": set(), "c": set()}, {"a": 1, "b": 2, "c": 4})
    7

    >>> node_weight("b", {"a": {"b", "c"}, "b": set(), "c": set()}, {"a": 1, "b": 2, "c": 4})
    2
    """
    return weights[node] + sum(
        node_weight(child, tree, weights) for child in tree[node]
    )


def balance_nodes(tree, weights):
    """Balance the nodes so that all siblings have the same total weight.

    Assumes one node has the wrong weigth and returns the corrected weight.

    >>> balance_nodes({"a": {"b", "c", "d"}, "b": {"e", "f", "g"}, "c": set(),
    ...                "d": set(), "e": set(), "f": set(), "g": set()},
    ...               {"a": 1, "b": 1, "c": 5, "d": 5, "e": 1, "f": 1, "g": 1})
    2
    """
    full_weights = {node: node_weight(node, tree, weights) for node in tree}
    root = max(full_weights, key=lambda node: full_weights[node])
    queue = collections.deque([root])

    while queue:
        root = queue.popleft()
        child_weights = {node: full_weights[node] for node in tree[root]}
        if min(child_weights.values()) < max(child_weights.values()):
            correct_weight = statistics.mode(child_weights.values())
            wrong_child, weight_diff = next(
                (child, weight - correct_weight)
                for child, weight in child_weights.items()
                if weight != correct_weight
            )
            queue.append(wrong_child)
            continue
        return weights[root] - weight_diff


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
