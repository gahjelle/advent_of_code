"""AoC 11, 2015: Corporate Policy"""


# Standard library imports
import functools
import pathlib
import sys

LETTERS = "abcdefghjkmnpqrstuvwxyz"
INC = dict(zip(LETTERS[:-1], LETTERS[1:])) | {"i": "j", "l": "m", "o": "p", "z": ""}


def parse_data(puzzle_input):
    """Parse input"""
    return puzzle_input


def part1(data):
    """Solve part 1"""
    return next_password(data)


def part2(data):
    """Solve part 2"""
    return next_password(increase_password(next_password(data)))


@functools.cache
def next_password(password):
    """Find the next valid password.

    ## Example:

    >>> next_password("aabba")
    'aabcc'
    """
    while not is_valid(password):
        password = increase_password(password)
    return password


def increase_password(current):
    """Increase the current password.

    ## Examples:

    >>> increase_password("abc")
    'abd'
    >>> increase_password("fgh")
    'fgj'
    >>> increase_password("ghi")
    'ghj'
    >>> increase_password("vwxyz")
    'vwxza'
    >>> increase_password("mnzzz")
    'mpaaa'
    """
    head, tail = current[:-1], current[-1]
    return f"{increase_password(head)}a" if tail == "z" else f"{head}{INC[tail]}"


def is_valid(password):
    """Check if password is valid.

    - At least three continuously increasing letters, e.g. "abc"
    - No "i", "l", or "o"
    - At least two different, non-overlapping pairs of letters, e.g "aa" and "bb"

    ## Examples:

    >>> is_valid("hijklmmn")
    False
    >>> is_valid("abbceffg")
    False
    >>> is_valid("abbcegjk")
    False
    >>> is_valid("abcdffaa")
    True
    """
    if not any(
        INC[first] == second and INC[second] == third
        for first, second, third in zip(password, password[1:], password[2:])
    ):
        return False

    pair_idx = [
        idx
        for idx, (first, second) in enumerate(zip(password, password[1:]))
        if first == second
    ]

    return pair_idx and max(pair_idx) - min(pair_idx) >= 2


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
