"""AoC 12, 2023: Hot Springs."""

# Standard library imports
import functools
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    data = []
    for line in puzzle_input.split("\n"):
        springs, groups = line.split()
        data.append((springs, tuple(int(number) for number in groups.split(","))))

    return data


def part1(data):
    """Solve part 1."""
    return sum(count_arrangements(*hot_spring) for hot_spring in data)


def part2(data):
    """Solve part 2."""
    return sum(count_arrangements(*unfold_map(*hot_spring)) for hot_spring in data)


@functools.cache
def count_arrangements(springs, groups):
    """Find the number of arrangements that satisfy the group contraints.

    Based on https://github.com/hyper-neutrino/. Recursively count the number of
    valid arrangements.

    ## Example:

    >>> count_arrangements("?????", (1, 2))
    3
    >>> count_arrangements("????###??.????#.#", (5, 1, 2, 1))
    7
    """
    if springs == "":
        return 1 if groups == () else 0
    if groups == ():
        return 0 if "#" in springs else 1

    total = 0
    group = groups[0]

    # Operational spring
    if springs[0] in ".?":
        total += count_arrangements(springs[1:], groups)

    # Group of damaged springs
    if springs[0] in "#?" and (
        group <= len(springs)  # Enough springs left to fill group
        and "." not in springs[:group]  # No operational spring inside group
        and (group == len(springs) or springs[group] != "#")  # Spring after group works
    ):
        total += count_arrangements(springs[group + 1 :], groups[1:])

    return total


def unfold_map(springs, groups):
    """Unfold the map to show all springs."""
    return "?".join([springs] * 5), groups * 5


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
