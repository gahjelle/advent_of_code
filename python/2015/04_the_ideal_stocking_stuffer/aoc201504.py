"""AoC 4, 2015: The Ideal Stocking Stuffer"""

# Standard library imports
import hashlib
import itertools
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input"""
    return puzzle_input


def part1(data):
    """Solve part 1"""
    return first_md5(secret=data, prefix="0" * 5)


def part2(data):
    """Solve part 2"""
    return first_md5(secret=data, prefix="0" * 6)


def first_md5(secret, prefix):
    """Find the first advent coin with the given prefix

    ## Example:

    >>> first_md5("aoc", "000")
    425
    """
    for num in itertools.count(1):
        md5 = hashlib.md5()
        md5.update(f"{secret}{num}".encode("utf-8"))

        if md5.hexdigest().startswith(prefix):
            return num


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
