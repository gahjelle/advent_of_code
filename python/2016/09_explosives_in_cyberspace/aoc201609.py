"""AoC 9, 2016: Explosives in Cyberspace."""

# Standard library imports
import itertools
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    return puzzle_input


def part1(string):
    """Solve part 1."""
    return sum(find_length(string))


def part2(string):
    """Solve part 2."""
    return sum(find_length(string, recurse=True))


def find_length(string, recurse=False):
    """Find the decompressed length of a string.

    The format compresses a sequence of characters. Whitespace is ignored. To
    indicate that some sequence should be repeated, a marker is added to the
    file, like (10x2). To decompress this marker, take the subsequent 10
    characters and repeat them 2 times.

    ## Examples:

    >>> sum(find_length("(6x1)(1x3)A", recurse=False))
    6
    >>> sum(find_length("(6x1)(1x3)A", recurse=True))
    3
    """
    str_iter = iter(string)
    for char in str_iter:
        if char != "(":
            yield 1
            continue

        counter, repeats = [
            int(n)
            for n in "".join(
                itertools.takewhile(lambda char: char != ")", str_iter)
            ).split("x")
        ]
        data = itertools.islice(str_iter, counter)
        yield repeats * (sum(find_length(data, True)) if recurse else len(list(data)))


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
