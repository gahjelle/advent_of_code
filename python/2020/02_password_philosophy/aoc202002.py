"""AoC 2, 2020: Password Philosophy."""

# Standard library imports
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    return [parse_policy(line) for line in puzzle_input.split("\n")]


def parse_policy(line):
    """Parse one line of input.

    ## Example:

    >>> parse_policy("3-10 o: adventofcode")
    (3, 10, 'o', 'adventofcode')
    """
    numbers, char, password = line.split()
    first, second = numbers.split("-")
    return (int(first), int(second), char[0], password)


def part1(policies):
    """Solve part 1."""
    return sum(is_valid_count(*policy) for policy in policies)


def part2(policies):
    """Solve part 2."""
    return sum(is_valid_position(*policy) for policy in policies)


def is_valid_count(first, second, char, password):
    """Check if the password follows the count requirements.

    ## Examples:

    >>> is_valid_count(4, 6, "e", "adventofcode")
    False

    >>> is_valid_count(1, 3, "o", "passwordphilosophy")
    True
    """
    return first <= password.count(char) <= second


def is_valid_position(first, second, char, password):
    """Check if the password follows the position requirements.

    ## Examples:

    >>> is_valid_position(4, 6, "e", "adventofcode")
    True

    >>> is_valid_position(1, 3, "o", "passwordphilosophy")
    False
    """
    return (password[first - 1] == char) != (password[second - 1] == char)


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
