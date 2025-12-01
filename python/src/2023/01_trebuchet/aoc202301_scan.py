"""AoC 1, 2023: Trebuchet?!."""

# Standard library imports
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    return puzzle_input.split("\n")


def part1(data):
    """Solve part 1."""
    return sum(find_digit(line) * 10 + find_digit(line[::-1]) for line in data)


def part2(data):
    """Solve part 2."""
    digits = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    tigids = {word[::-1]: digit for word, digit in digits.items()}
    return sum(
        find_digit(line, words=digits) * 10 + find_digit(line[::-1], words=tigids)
        for line in data
    )


def find_digit(text, words={}):
    """Find the first digit in a text, include possible digit words.

    ## Examples:

    >>> find_digit("one2three")
    2
    >>> find_digit("one2three", words={"one": 1, "three": 3})
    1
    >>> find_digit("abc7eightwo", words={"two": 2, "eight": 8})
    7
    >>> find_digit("heightwo", words={"two": 2, "eight": 8})
    8
    """
    if text[0].isdigit():
        return int(text[0])
    for word, digit in words.items():
        if text.startswith(word):
            return digit
    return find_digit(text[1:], words=words)


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
