"""AoC 3, 2022: Rucksack Reorganization."""

# Standard library imports
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    return puzzle_input.split("\n")


def part1(rucksacks):
    """Solve part 1."""
    return sum(priority(find_common(split(rucksack))) for rucksack in rucksacks)


def part2(rucksacks):
    """Solve part 2."""
    return sum(
        priority(find_common(triple))
        for triple in zip(rucksacks[::3], rucksacks[1::3], rucksacks[2::3])
    )


def split(rucksack):
    """Split one rucksack into two compartments.

    ## Example:

    >>> split("GeirArne")
    ['Geir', 'Arne']
    """
    per_compartment = len(rucksack) // 2
    return [rucksack[:per_compartment], rucksack[per_compartment:]]


def find_common(items):
    """Find common items in all rucksacks or compartments.

    ## Examples:

    >>> find_common(["geiRarnE", "advent", "wastl"])
    'a'
    >>> find_common(["ABCXyz", "abcXYZ"])
    'X'
    """
    return set.intersection(*[set(item) for item in items]).pop()


def priority(item):
    """Calculate priority of item.

    - Lowercase item types a through z have priorities 1 through 26.
    - Uppercase item types A through Z have priorities 27 through 52.

    ## Examples:

    >>> priority("E")
    31
    >>> priority("l")
    12
    """
    return (ord(item) - 38) % 58


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
