"""AoC 1, 2017: Inverse Captcha"""

# Standard library imports
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input"""
    return [int(digit) for digit in puzzle_input]


def part1(data):
    """Solve part 1"""
    return equal_sum(data, data[1:] + data[:1])


def part2(data):
    """Solve part 2"""
    split_idx = len(data) // 2
    return equal_sum(data, data[split_idx:] + data[:split_idx])


def equal_sum(sequence_1, sequence_2):
    """Find sum of digits that are equal in both sequences

    >>> equal_sum([1, 2, 3], [1, 2, 3])
    6

    >>> equal_sum([1, 2, 3, 4], [4, 3, 2, 1])
    0
    """
    return sum(
        first for first, second in zip(sequence_1, sequence_2) if first == second
    )


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
