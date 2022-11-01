"""AoC 3, 2016: Squares With Three Sides"""

# Standard library imports
import itertools
import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    return [
        [int(side) for side in triangle.split()]
        for triangle in puzzle_input.split("\n")
    ]


def part1(data):
    """Solve part 1"""
    return sum(is_triangle(side_lengths) for side_lengths in data)


def part2(data):
    """Solve part 2"""
    return sum(is_triangle(side_lengths) for side_lengths in transpose(data))


def is_triangle(side_lengths):
    """Check that the given side lengths represent a valid triangle

    ## Examples:

    >>> is_triangle([3, 4, 5])
    True
    >>> is_triangle([5, 10, 25])
    False
    >>> is_triangle([25, 10, 5])
    False
    >>> is_triangle([1, 2, 3])
    False
    """
    return sum(side_lengths) > 2 * max(side_lengths)


def transpose(triangles):
    """Transpose list of triangles

    ## Example:

    >>> transpose([[1, 2, 3], [4, 5, 6], [7, 8, 9], [0, 1, 2], [3, 4, 5], [6, 7, 8]])
    [[1, 4, 7], [0, 3, 6], [2, 5, 8], [1, 4, 7], [3, 6, 9], [2, 5, 8]]
    """
    side_lengths = itertools.chain(*zip(*triangles))
    return [list(itertools.islice(side_lengths, 3)) for _ in triangles]


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
