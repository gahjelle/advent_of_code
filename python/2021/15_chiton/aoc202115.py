"""AoC 15, 2021: Chiton"""

# Standard library imports
import heapq
import itertools
import pathlib
import sys

# Third party imports
import colorama
import numpy as np
from colorama import Cursor, Fore

colorama.init()


def parse(puzzle_input):
    """Parse input"""
    return np.array(
        [[int(energy) for energy in line] for line in puzzle_input.split("\n")]
    )


def part1(data):
    """Solve part 1"""
    return find_cheapest(data)


def part2(data):
    """Solve part 2"""
    return find_cheapest(expand(data, 5, 5))


def expand(risks, num_tile_rows, num_tile_cols):
    """Expand risk map by tiling risks

    >>> expand(np.array([[1, 4], [8, 9]]), 2, 2)
    array([[1, 4, 2, 5],
           [8, 9, 9, 1],
           [2, 5, 3, 6],
           [9, 1, 1, 2]])
    """
    num_rows, num_cols = risks.shape
    tiled = np.tile(risks, (num_tile_rows, num_tile_cols))
    for row, col in itertools.product(range(num_tile_rows), range(num_tile_cols)):
        tiled[
            num_rows * row : num_rows * (row + 1), num_cols * col : num_cols * (col + 1)
        ] += (row + col)

    tiled[tiled > 9] -= 9
    return tiled


def find_cheapest(risks):
    """Find the cost of the cheapest path through the risk levels

    Use a heap to keep track of the cheapest next step.

    [1]:2: 9          --[2]:9:         |  X :9:         |  X :9:
               2,3             3,9,11  |        8,9,11  |
    :3: 7  1   -->   :3::7: 1   -->   [3]:7: 1   -->    | :7: 1
                                                        |
     5  8  3          5  8  3         :5: 8  3         [5]:8: 3


              ---+ :9:          ---+ :9:          -----[9]         ---+  X
     9,11,16     |     10,11,16    |     11,13,16           13,16     |
       -->    X [7]:1:   -->    X  +-[1]   -->    X  X  X    -->   X  +--+   -->   13
                                                                         |
              X :8: 3           X :8::3:          X :8::3:         X :8:[3]

    >>> find_cheapest(np.array([[1, 2, 9], [3, 7, 1], [5, 8, 3]]))
    13
    """
    num_rows, num_cols = risks.shape
    target = (num_rows - 1, num_cols - 1)
    locations = [(0, (0, 0))]
    seen = set()

    while True:
        cost, current = heapq.heappop(locations)
        if "-v" in sys.argv:
            visualize(risks, seen, current)

        if current == target:
            return cost

        for neighbor in neighbors(current, *risks.shape):
            if neighbor not in seen:
                seen.add(neighbor)
                heapq.heappush(locations, (cost + risks[neighbor], neighbor))


def neighbors(current, num_rows, num_cols):
    """Find neighbors to the current position

    >>> list(neighbors((2, 2), 5, 5))
    [(1, 2), (2, 1), (2, 3), (3, 2)]

    >>> list(neighbors((0, 4), 5, 5))
    [(0, 3), (1, 4)]
    """
    row, col = current

    if row - 1 >= 0:
        yield (row - 1, col)
    if col - 1 >= 0:
        yield (row, col - 1)
    if col + 1 < num_cols:
        yield (row, col + 1)
    if row + 1 < num_rows:
        yield (row + 1, col)


def visualize(risks, seen, current):
    """Draw risks to terminal"""
    for row, line in enumerate(risks):
        for col, risk in enumerate(line):
            symbol = (
                Fore.RED + "#"
                if (row, col) == current
                else Fore.YELLOW + str(risks[row, col])
                if (row, col) in seen
                else Fore.GREEN + str(risks[row, col])
            )
            print(Cursor.POS(col + 1, row + 1) + symbol)


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        if path.startswith("-"):
            continue

        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
