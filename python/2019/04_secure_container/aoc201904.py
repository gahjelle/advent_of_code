"""AoC 4, 2019: Secure Container"""

# Standard library imports
import pathlib
import sys

RULES = {}


def register_rule(func):
    """Register function that validates a rule"""
    RULES[func.__name__] = func
    return func


def parse(puzzle_input):
    """Parse input"""
    start, _, end = puzzle_input.partition("-")
    return [str(password) for password in range(int(start), int(end) + 1)]


def part1(data):
    """Solve part 1"""
    return len(check(data, "non_decreasing", "adjacent_same"))


def part2(data):
    """Solve part 2"""
    return len(check(data, "non_decreasing", "adjacent_only_two"))


def check(passwords, *rules):
    """Check passwords against rules

    ## Example:

    >>> check(["280177","135579", "040480"], "non_decreasing", "adjacent_same")
    ['135579']
    """
    for rule in rules:
        passwords = RULES[rule](passwords)
    return passwords


@register_rule
def non_decreasing(passwords):
    """Check that password digits never decreases

    ## Example:

    >>> non_decreasing(["123456", "155559", "280177"])
    ['123456', '155559']
    """
    return [
        password
        for password in passwords
        if all(first <= second for first, second in zip(password, password[1:]))
    ]


@register_rule
def adjacent_same(passwords):
    """Check that two adjacent digits are the same

    ## Example:

    >>> adjacent_same(["282828", "280177", "777777"])
    ['280177', '777777']
    """
    return [
        password
        for password in passwords
        if any(first == second for first, second in zip(password, password[1:]))
    ]


@register_rule
def adjacent_only_two(passwords):
    """Check that exactly two adjacent digits are the same

    ## Examples:

    >>> adjacent_only_two(["282828", "280177", "777777", "111233"])
    ['280177', '111233']
    """
    return [
        pw
        for pw in passwords
        if any(
            before != first == second != after
            for before, first, second, after in zip(f"X{pw}", pw, pw[1:], f"{pw}X"[2:])
        )
    ]


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
