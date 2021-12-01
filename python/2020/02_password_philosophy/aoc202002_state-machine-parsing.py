"""AoC 2, 2020: Password Philosophy"""

# Standard library imports
import pathlib
import string
import sys


def parse(puzzle_input):
    """Parse input"""
    return [parse_policy(line) for line in puzzle_input.split("\n")]


def parse_policy(line):
    """Parse one line into a password policy

    Use a hand-coded state machine for parsing:
        https://dev.to/meseta/advent-of-code-day-02-a-59m0

    >>> parse_policy("4-6 e: adventofcode")
    {'first': 4, 'second': 6, 'char': 'e', 'password': 'adventofcode'}
    """
    state = "first"
    accumulator = ""
    policy = {}
    for char in line:
        if state == "first":
            if char.isdigit():
                accumulator += char
            else:
                policy["first"] = int(accumulator)
                accumulator = ""
                state = "second"
                continue

        if state == "second":
            if char.isdigit():
                accumulator += char
            else:
                policy["second"] = int(accumulator)
                accumulator = ""
                state = "char"
                continue

        if state == "char":
            policy["char"] = char
            state = "password"
            continue

        if state == "password":
            if char in string.ascii_lowercase:
                accumulator += char

    policy["password"] = accumulator

    return policy


def part1(data):
    """Solve part 1"""
    return sum(is_valid_count(**policy) for policy in data)


def part2(data):
    """Solve part 2"""
    return sum(is_valid_position(**policy) for policy in data)


def is_valid_count(first, second, char, password):
    """Check if the password follows the count requirements

    ## Examples:

    >>> is_valid_count(first=4, second=6, char="e", password="adventofcode")
    False

    >>> is_valid_count(first=1, second=3, char="o", password="passwordphilosophy")
    True
    """
    return first <= password.count(char) <= second


def is_valid_position(first, second, char, password):
    """Check if the password follows the position requirements

    ## Examples:

    >>> is_valid_position(first=4, second=6, char="e", password="adventofcode")
    True

    >>> is_valid_position(first=1, second=3, char="o", password="passwordphilosophy")
    False
    """
    return (password[first - 1] == char) != (password[second - 1] == char)


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
