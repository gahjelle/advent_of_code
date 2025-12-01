"""AoC 4, 2022: Camp Cleanup."""

# Standard library imports
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    return [parse_pair(line) for line in puzzle_input.split("\n")]


def parse_pair(line):
    """Parse one pair of assignments.

    ## Example:

    >>> parse_pair("5-7,6-9")
    ((5, 7), (6, 9))
    """
    return tuple(tuple(int(ids) for ids in elf.split("-")) for elf in line.split(","))


def part1(pairs):
    """Solve part 1."""
    return sum(full_overlap(first, second) for first, second in pairs)


def part2(pairs):
    """Solve part 2."""
    return sum(any_overlap(first, second) for first, second in pairs)


def full_overlap(first, second):
    """Does one assignment fully overlap the other?

    ## Examples:

    >>> full_overlap((5, 7), (6, 9))
    False
    >>> full_overlap((4, 11), (6, 9))
    True
    """
    low_1, high_1 = first
    low_2, high_2 = second
    return (low_1 <= low_2 and high_1 >= high_2) or (
        low_2 <= low_1 and high_2 >= high_1
    )


def any_overlap(first, second):
    """Do the assignments overlap at all?

    ## Examples:

    >>> any_overlap((5, 7), (6, 9))
    True
    >>> any_overlap((1, 3), (4, 7))
    False
    """
    low_1, high_1 = first
    low_2, high_2 = second
    return low_1 <= high_2 and low_2 <= high_1


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
