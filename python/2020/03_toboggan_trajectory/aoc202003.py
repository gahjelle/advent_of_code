"""AoC 3, 2020: Toboggan Trajectory"""

# Standard library imports
import math
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input"""
    return [[c == "#" for c in line] for line in puzzle_input.split("\n")]


def part1(data):
    """Solve part 1"""
    return sum(trees(data))


def part2(data):
    """Solve part 2"""
    return math.prod(
        [
            sum(trees(data, right=1, down=1)),
            sum(trees(data, right=3, down=1)),
            sum(trees(data, right=5, down=1)),
            sum(trees(data, right=7, down=1)),
            sum(trees(data, right=1, down=2)),
        ]
    )


def trees(slope, right=3, down=1):
    """Yield trees along the slope in the given direction

    ## Examples:

        #.#.
        #..#
        .#..
        ..#.
        ##..

    >>> slope = [[1, 0, 1, 0], [1, 0, 0, 1], [0, 1, 0, 0], [0, 0, 1, 0], [1, 1, 0, 0]]
    >>> list(trees(slope, right=2, down=1))
    [1, 0, 0, 1, 1]
    """
    max_y, max_x = len(slope), len(slope[0])

    idx_x = 0
    for idx_y in range(0, max_y, down):
        yield slope[idx_y][idx_x]
        idx_x = (idx_x + right) % max_x


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
