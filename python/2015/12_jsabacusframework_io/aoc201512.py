"""AoC 12, 2015: JSAbacusFramework.io"""

# Standard library imports
import json
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input"""
    return json.loads(puzzle_input)


def part1(data):
    """Solve part 1"""
    return sum_numbers(data)


def part2(data):
    """Solve part 2"""
    return sum_numbers(data, ignore_red=True)


def sum_numbers(document, ignore_red=False):
    """Sum numbers in a document.

    ## Examples:

    >>> sum_numbers(7)
    7
    >>> sum_numbers("twelve")
    0
    >>> sum_numbers([1, "two", 3])
    4
    >>> sum_numbers({"one": 1, 2: "two", "four": 4})
    5
    >>> sum_numbers([1, {"two": 2, "five": 5}, "nine"])
    8
    >>> sum_numbers([1, {"c": "red", "b": 2}, 3], ignore_red=True)
    4
    """
    if isinstance(document, int):
        return document
    if isinstance(document, str):
        return 0
    if isinstance(document, list):
        return sum(sum_numbers(item, ignore_red) for item in document)
    if isinstance(document, dict):
        if ignore_red and "red" in document.values():
            return 0
        else:
            return sum(sum_numbers(item, ignore_red) for item in document.values())


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
