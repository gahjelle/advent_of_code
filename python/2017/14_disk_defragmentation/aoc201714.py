"""AoC 14, 2017: Disk Defragmentation."""

# Standard library imports
import functools
import itertools
import pathlib
import sys

# Advent of Code imports
from aoc import knothash

BITS = (
    {"0": [], "1": [3], "2": [2], "3": [2, 3], "4": [1], "5": [1, 3]}
    | {"6": [1, 2], "7": [1, 2, 3], "8": [0], "9": [0, 3], "a": [0, 2], "b": [0, 2, 3]}
    | {"c": [0, 1], "d": [0, 1, 3], "e": [0, 1, 2], "f": [0, 1, 2, 3]}
)
NUM_BITS = {hex: len(bits) for hex, bits in BITS.items()}


def parse_data(puzzle_input):
    """Parse input."""
    return puzzle_input


def part1(key_string):
    """Solve part 1."""
    return sum(sum(NUM_BITS[hex] for hex in hash) for hash in get_hashes(key_string))


def part2(key_string):
    """Solve part 2."""
    return count_regions(create_map(get_hashes(key_string)))


@functools.cache
def get_hashes(key_string):
    """Get the hashes of a key_string."""
    return [knothash.hash_string(f"{key_string}-{idx}") for idx in range(128)]


def create_map(hashes):
    """Create a map based on knot hashes.

    ## Example:

    >>> map = create_map(["00", "00", "a1", "00", "00", "00", "89", "00"])
    >>> sorted(map)
    [(2, 0), (2, 2), (2, 7), (6, 0), (6, 4), (6, 7)]
    """
    return {
        (row, col * 4 + bit)
        for row, hash in enumerate(hashes)
        for col, hex in enumerate(hash)
        for bit in BITS[hex]
    }


def count_regions(coordinates):
    """Count regions of adjacent coordinates.

    ## Example:

    >>> count_regions({(0, 0), (2, 0), (2, 1), (3, 2)})
    3
    """
    for count in itertools.count():
        if not coordinates:
            return count

        remove_adjacent(coordinates, next(iter(coordinates)))


def remove_adjacent(coordinates, start):
    """Remove all coordinates in the same adjacency region as start.

    NOTE: Mutates the original sets of coordinates

    ## Example:

    >>> coordinates = {(0, 0), (2, 0), (2, 1), (3, 2)}
    >>> left = remove_adjacent(coordinates, (2, 1))
    >>> sorted(coordinates)
    [(0, 0), (3, 2)]
    """
    queue = [start]
    while queue:
        row, col = current = queue.pop()
        for drow, dcol in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if (neighbor := (row + drow, col + dcol)) in coordinates:
                queue.append(neighbor)
        coordinates -= {current}


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
