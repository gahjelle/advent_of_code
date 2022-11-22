"""AoC 2, 2018: Inventory Management System"""

# Standard library imports
import collections
import itertools
import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    return puzzle_input.split("\n")


def part1(data):
    """Solve part 1"""
    twos, threes = zip(*[has_counts(box_id, 2, 3) for box_id in data])
    return sum(twos) * sum(threes)


def part2(data):
    """Solve part 2"""
    return next(
        match
        for first, second in itertools.product(data, repeat=2)
        if (match := almost_equal(first, second))
    )


def has_counts(box_id, *counts):
    """Check if box ID has the given counts of letters

    ## Examples:

    >>> has_counts("geirarne", 2, 3, 5)
    (True, False, False)
    >>> has_counts("geirarnehjelle", 2, 3)
    (True, False)
    """
    box_id_counts = set(collections.Counter(box_id).values())
    return tuple(count in box_id_counts for count in counts)


def almost_equal(first, second):
    """Check if two strings differ in exactly one position.

    Return all matching characters if almost equal.

    ## Examples

    >>> almost_equal("geir", "arne")
    False
    >>> almost_equal("geirarne", "geirarne")
    False
    >>> almost_equal("arne", "anne")
    'ane'
    >>> almost_equal("oooooAooo", "oooooSooo")
    'oooooooo'
    """
    matches = []
    has_missed = False
    for char1, char2 in zip(first, second):
        if char1 == char2:
            matches.append(char1)
        elif not has_missed:
            has_missed = True
        else:
            return False
    return "".join(matches) if has_missed else False


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
