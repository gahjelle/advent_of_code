"""AoC 8, 2019: Space Image Format."""

# Standard library imports
import collections
import pathlib
import sys

# Third party imports
from advent_of_code_ocr import convert_6


def parse_data(puzzle_input):
    """Parse input."""
    return [int(number) for number in puzzle_input]


def part1(numbers, width=25, height=6):
    """Solve part 1."""
    numbers_per_layer = width * height
    return min(
        (c[0], c[1] * c[2])
        for i in range(0, len(numbers), numbers_per_layer)
        if (c := collections.Counter(numbers[i : i + numbers_per_layer]))
    )[1]


def part2(numbers, width=25, height=6):
    """Solve part 2."""
    numbers_per_layer = width * height
    grid = [[None for _ in range(width)] for _ in range(height)]

    for number_idx in range(0, len(numbers), numbers_per_layer):
        layer = numbers[number_idx : number_idx + numbers_per_layer]
        for idx, number in enumerate(layer):
            row, col = divmod(idx, width)
            if number != 2 and grid[row][col] is None:
                grid[row][col] = "#" if number == 1 else "."

    return convert_6("\n".join("".join(line) for line in grid))


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
