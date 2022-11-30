"""AoC 6, 2016: Signals and Noise"""

# Standard library imports
import collections
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    return [order_letters(letters) for letters in zip(*puzzle_input.split("\n"))]


def order_letters(letters):
    """Order list of letters by their frequency.

    ## Example:

    >>> order_letters("ccdlcl")
    'cld'
    """
    return "".join(letter for letter, _ in collections.Counter(letters).most_common())


def part1(letters_list):
    """Solve part 1."""
    return "".join(letters[0] for letters in letters_list)


def part2(letters_list):
    """Solve part 2."""
    return "".join(letters[-1] for letters in letters_list)


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
