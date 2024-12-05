"""AoC 5, 2024: Print Queue."""

# Standard library imports
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    rules_str, updates_str = puzzle_input.split("\n\n")
    rules = [
        tuple(int(number) for number in line.split("|"))
        for line in rules_str.split("\n")
    ]

    return {
        number: {before for before, after in rules if after == number}
        for number in {number for rule in rules for number in rule}
    }, [[int(number) for number in line.split(",")] for line in updates_str.split("\n")]


def part1(data):
    """Solve part 1."""
    rules, updates = data
    return sum(middle(update) for update in updates if check_update(update, rules))


def part2(data):
    """Solve part 2."""
    rules, updates = data
    return sum(
        middle(order_correctly(update, rules))
        for update in updates
        if not check_update(update, rules)
    )


def check_update(update, before):
    """Recursively check whether the pages in an update are ordered correctly.

    ## Example

    >>> before = {77: {1, 28}, 1: {28}, 28: set()}
    >>> check_update([28, 1, 77], before)
    True
    >>> check_update([77, 28, 1], before)
    False
    """
    if len(update) < 2:
        return True
    first, *rest = update
    return False if before[first] & set(rest) else check_update(rest, before)


def order_correctly(update, before):
    """Order the pages of an update correctly

    ## Example

    >>> before = {77: {1, 19, 28}, 19: {1, 28}, 1: {28}, 28: set()}
    >>> order_correctly([77, 28, 19, 1], before)
    [28, 1, 19, 77]
    """
    not_placed = set(update)
    new_update = []
    while not_placed:
        new_update.extend(page for page in not_placed if not before[page] & not_placed)
        not_placed -= set(new_update)
    return new_update


def middle(update):
    """Find the middle page in an update.

    ## Examples

    >>> middle([1, 2, 3, 4, 5])
    3
    >>> middle([75, 47, 61, 53, 29])
    61
    """
    return update[len(update) // 2]


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
