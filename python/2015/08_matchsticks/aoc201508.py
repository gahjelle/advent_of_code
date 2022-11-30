"""AoC 8, 2015: Matchsticks"""

# Standard library imports
import pathlib
import re
import sys


def parse_data(puzzle_input):
    """Parse input"""
    return puzzle_input.split("\n")


def part1(words):
    """Solve part 1"""
    return sum(len(word) - len(memory(word)) for word in words)


def part2(words):
    """Solve part 2"""
    return sum(len(encode(word)) - len(word) for word in words)


def memory(word):
    r"""Convert literal string to in-memory string.

    ## Examples:

    >>> memory(r'""')
    ''
    >>> memory(r'"aaa\"aaa"')
    'aaa"aaa'
    >>> memory(r'"\x27"')
    '_'
    """
    stripped = word.strip('"').replace(r"\\", "\\").replace(r"\"", '"')
    return re.sub(r"\\x[0-9a-fA-F]{2}", "_", stripped)


def encode(word):
    r"""Encode a literal string.

    ## Examples:

    >>> encode(r'""')
    '"\\"\\""'
    >>> encode(r'"aaa\"aaa"')
    '"\\"aaa\\\\\\"aaa\\""'
    >>> encode(r'"\x27"')
    '"\\"\\\\x27\\""'
    """
    encoded = word.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{encoded}"'


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
