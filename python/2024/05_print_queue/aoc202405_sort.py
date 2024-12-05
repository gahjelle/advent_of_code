"""AoC 5, 2024: Print Queue."""

# Standard library imports
import functools
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    rules_str, updates_str = puzzle_input.split("\n\n")
    rules = {
        tuple(int(number) for number in line.split("|"))
        for line in rules_str.split("\n")
    }

    def cmp(first, second):
        return -1 if (first, second) in rules else 1

    return functools.cmp_to_key(cmp), [
        [int(number) for number in line.split(",")] for line in updates_str.split("\n")
    ]


def part1(data):
    """Solve part 1."""
    rules, updates = data
    return sum(
        update[len(update) // 2] for update in updates if is_sorted(update, rules)
    )


def part2(data):
    """Solve part 2."""
    rules, updates = data
    return sum(
        sorted(update, key=rules)[len(update) // 2]
        for update in updates
        if not is_sorted(update, rules)
    )


def is_sorted(update, rules):
    """Check if an update is already sorted according to the rules"""
    return update == sorted(update, key=rules)


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
