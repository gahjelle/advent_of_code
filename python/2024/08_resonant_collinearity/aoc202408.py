"""AoC 8, 2024: Resonant Collinearity."""

# Standard library imports
import collections
import itertools
import math
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    grid = {
        (row, col): char
        for row, line in enumerate(puzzle_input.split("\n"))
        for col, char in enumerate(line)
    }
    antennas = collections.defaultdict(list)
    for pos, char in grid.items():
        if char != ".":
            antennas[char].append(pos)
    return set(grid), antennas


def part1(data):
    """Solve part 1."""
    grid, antennas = data
    return len(
        grid
        & set.union(*[find_antinodes(positions) for positions in antennas.values()])
    )


def part2(data):
    """Solve part 2."""
    grid, antennas = data
    return len(
        set.union(
            *[find_all_antinodes(grid, positions) for positions in antennas.values()]
        )
    )


def find_antinodes(antennas):
    """Find the first resonant antinodes to the given antennas"""
    return set.union(
        *[
            {
                (2 * row_1 - row_2, 2 * col_1 - col_2),
                (2 * row_2 - row_1, 2 * col_2 - col_1),
            }
            for (row_1, col_1), (row_2, col_2) in itertools.combinations(antennas, r=2)
        ]
    )


def find_all_antinodes(grid, antennas):
    """Find all resonant antinodes to the given antennas

    Sort antennas to guarantee that row <= row_2. The input data are constructed
    such that row1 != row2, so it's possible to loop over rows.
    """
    max_row, _ = max(grid)
    antinodes = set()
    for (row, col), (row_2, col_2) in itertools.combinations(sorted(antennas), r=2):
        dr, dc = row_2 - row, col_2 - col
        # dr, dc = dr // math.gcd(dr, dc), dc // math.gcd(dr, dc)  # Not necessary
        antinodes |= grid & {
            (row + n * dr, col + n * dc)
            for n in range(-row // dr, (max_row - row) // dr + 1)
        }
    return antinodes


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
