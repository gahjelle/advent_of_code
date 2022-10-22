"""AoC 17, 2020: Conway Cubes"""

# Standard library imports
import collections
import itertools
import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    return {
        (row, col, 0, 0)
        for row, line in enumerate(puzzle_input.split("\n"))
        for col, state in enumerate(line)
        if state == "#"
    }


def part1(data):
    """Solve part 1"""
    neighbors = list_neighbors((-1, 0, 1), (-1, 0, 1), (-1, 0, 1), (0,))
    return len(evolve_several(data, neighbors, num_generations=6))


def part2(data):
    """Solve part 2"""
    neighbors = list_neighbors((-1, 0, 1), (-1, 0, 1), (-1, 0, 1), (-1, 0, 1))
    return len(evolve_several(data, neighbors, num_generations=6))


def list_neighbors(*diffs):
    """Enumerate all neighbors

    ## Example:

    >>> sorted(list_neighbors((0, 1), (0,), (-1, 0, 1)))
    [(0, 0, -1), (0, 0, 1), (1, 0, -1), (1, 0, 0), (1, 0, 1)]
    """
    return {coords for coords in itertools.product(*diffs) if any(coords)}


def evolve(cubes, neighbors):
    """Evolve the cubes one generation

    ## Example:

       ..... | 11100    .....
       .#... | 10321 -> ..#..
       ..##. | 24421 -> ...#.
       .##.. | 12331 -> .###.
       ..... | 12210    .....

    >>> cubes = evolve(
    ...     {(0, 0), (1, 1), (1, 2), (2, 0), (2, 1)},
    ...     {(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)},
    ... )
    >>> sorted(cubes)
    [(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    """
    num_neighbors = collections.defaultdict(int)
    for cube, dcube in itertools.product(cubes, neighbors):
        coords = tuple(c + dc for c, dc in zip(cube, dcube))
        num_neighbors[coords] += 1

    stay_alive = {cube for cube, num in num_neighbors.items() if num in {2, 3}} & cubes
    come_alive = {cube for cube, num in num_neighbors.items() if num == 3} - cubes
    return stay_alive | come_alive


def evolve_several(cubes, neighbors, num_generations):
    """Evolve the cubes several generations

    ## Example

       ..... | 11100    ..... | 01110    .....
       .#... | 10321 -> ..#.. | 01121 -> .....
       ..##. | 24421 -> ...#. | 13532 -> .#.#.
       .##.. | 12331 -> .###. | 11322 -> ..##.
       ..... | 12210    ..... | 12321    ..#..

    >>> cubes = evolve_several(
    ...     {(0, 0), (1, 1), (1, 2), (2, 0), (2, 1)},
    ...     {(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)},
    ...     2,
    ... )
    >>> sorted(cubes)
    [(1, 0), (1, 2), (2, 1), (2, 2), (3, 1)]
    """
    for _ in range(num_generations):
        cubes = evolve(cubes, neighbors)

    return cubes


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
