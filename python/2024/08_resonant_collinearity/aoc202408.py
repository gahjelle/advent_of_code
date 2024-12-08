"""AoC 8, 2024: Resonant Collinearity."""

# Standard library imports
import collections
import itertools
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
    return len(set.union(*[find_antinodes(grid, pos) for pos in antennas.values()]))


def part2(data):
    """Solve part 2."""
    grid, antennas = data
    return len(set.union(*[find_all_antinodes(grid, pos) for pos in antennas.values()]))


def find_antinodes(grid, antennas):
    """Find the first resonant antinodes to the given antennas"""
    return grid & {
        (2 * row - row_other, 2 * col - col_other)
        for (row, col), (row_other, col_other) in itertools.permutations(antennas, r=2)
    }


def find_all_antinodes(grid, antennas):
    """Find all resonant antinodes to the given antennas"""
    antinodes = set()
    for (row, col), (row_other, col_other) in itertools.permutations(antennas, r=2):
        dr, dc = row_other - row, col_other - col
        # dr, dc = dr // math.gcd(dr, dc), dc // math.gcd(dr, dc)  # Not necessary
        for n in itertools.count(1):
            if (antinode := (row + n * dr, col + n * dc)) not in grid:
                break
            antinodes.add(antinode)
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
