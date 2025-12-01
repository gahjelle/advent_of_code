"""AoC 1, 2023: Trebuchet?!."""

# Standard library imports
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    return puzzle_input.split("\n")


def part1(data):
    """Solve part 1."""
    return sum(find_calibration_value(line) for line in data)


def part2(data):
    """Solve part 2."""
    for word, digit in {
        "one": "o1e",  # Keep leading and trailing characters to handle overlaps
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e",
    }.items():
        data = [line.replace(word, digit) for line in data]
    return sum(find_calibration_value(line) for line in data)


def find_calibration_value(line):
    """Find the calibration value of a line of text, only care about numeric characters.

    ## Examples:

    >>> find_calibration_value("123")
    13
    >>> find_calibration_value("4")
    44
    >>> find_calibration_value("t2e8o1j")
    21
    >>> find_calibration_value("five6seven")
    66
    """
    digits = [char for char in line if char.isdigit()]
    return int(digits[0] + digits[-1])


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
