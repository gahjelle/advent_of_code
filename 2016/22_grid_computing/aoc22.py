"""Grid Computing

Advent of Code 2016, day 22
Solution by Geir Arne Hjelle, 2021-01-02
"""

# Standard library imports
import itertools
import pathlib
import sys
from collections import deque
from typing import NamedTuple

# Third party imports
import numpy as np
import parse

debug = print if "--debug" in sys.argv else lambda *_: None

NODE_PATTERN = parse.compile(
    "/dev/grid/node-x{x:d}-y{y:d} {size:>d}T {used:>d}T {avail:>d}T {use:>d}%"
)


class Node(NamedTuple):
    x: int
    y: int
    size: int
    used: int
    avail: int
    use: int


def parse_nodes(lines):
    """Parse each line into a Node"""
    nodes = []
    for line in lines:
        node = Node(**NODE_PATTERN.parse(line).named)
        nodes.append(node)

    return nodes


def viable_pairs(nodes):
    """Find viable pairs"""
    viable = []
    for node_a, node_b in itertools.product(nodes, repeat=2):
        if node_a == node_b:
            continue

        if 0 < node_a.used < node_b.avail:
            viable.append((node_a, node_b))

    return viable


def to_grid(nodes):
    """Set up grid representing nodes"""
    last_node = max(nodes, key=lambda n: n.x + n.y)
    smallest_node = min(nodes, key=lambda n: n.size)

    grid = np.ones((last_node.y + 1, last_node.x + 1), dtype=bool)
    for node in nodes:
        # Treat big nodes like walls
        if node.used > smallest_node.size:
            grid[node.y, node.x] = False

    return grid


def move_data(nodes):
    """Move data between two nodes"""
    grid = to_grid(nodes)

    # The empty node is used for transferring data
    empty_nodes = [n for n in nodes if n.used == 0]
    assert len(empty_nodes) == 1, "Assuming there is only 1 empty node"
    empty_idx = (empty_nodes[0].y, empty_nodes[0].x)

    # Move empty node next to data node (0, max_x)
    data_idx = (0, max(nodes, key=lambda n: n.x).x)
    num_steps = find_distance(
        grid, from_idx=empty_idx, to_idx=(data_idx[0], data_idx[1] - 1)
    )

    # Move data node next to goal node (0, 0)
    #
    # It takes 5 moves to move data one step towards the goal:
    #
    # ._D  >  .D_  >  .D.  >  .D.  >  .D.  >  _D.
    # ...  >  ...  >  .._  >  ._.  >  _..  >  ...
    #
    assert np.all(grid[:2]), "Assuming no walls in top two rows"
    num_steps += 5 * (data_idx[1] - 1)

    # Move data node onto goal node
    return num_steps + 1


def find_distance(grid, from_idx, to_idx):
    """Breadth-first search on grid"""
    max_y, max_x = grid.shape
    inf = 150  # Some number big enough to represent distance to undiscovered nodes
    distances = np.full(grid.shape, inf)
    queue = deque([(from_idx, 0)])

    while queue:
        idx, distance = queue.popleft()
        if distance < distances[idx]:
            if idx == to_idx:
                return distance

            distances[idx] = distance
            y, x = idx
            for dy, dx in ((-1, 0), (0, -1), (1, 0), (0, 1)):
                if 0 <= y + dy < max_y and 0 <= x + dx < max_x and grid[y + dy, x + dx]:
                    queue.append(((y + dy, x + dx), distance + 1))


def main(args):
    """Solve the problem for all file paths"""
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        solve(file_path)


def solve(file_path):
    """Solve the problem for one file path"""
    print(f"\n{file_path}:")
    nodes = parse_nodes(file_path.read_text().strip().split("\n")[2:])

    # Part 1
    viable = viable_pairs(nodes)
    print(f"There are {len(viable)} viable pairs")

    # Part 2
    num_steps = move_data(nodes)
    print(f"It takes {num_steps} steps to move the goal data to (0, 0)")


if __name__ == "__main__":
    main(sys.argv[1:])
