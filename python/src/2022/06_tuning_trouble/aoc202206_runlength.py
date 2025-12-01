"""AoC 6, 2022: Tuning Trouble."""

# Standard library imports
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    return puzzle_input


def part1(sequence):
    """Solve part 1."""
    return find_marker(sequence, 4)


def part2(sequence):
    """Solve part 2."""
    return find_marker(sequence, 14)


def find_marker(sequence, length):
    """Find the first marker of the given length.

    A marker of length N is a sequence of N characters that are all different.

    ## Examples:

    >>> find_marker("geirarne", 3)
    3
    >>> find_marker("abcdefghijklmnopqrstuvwxyz", 20)
    20
    >>> find_marker("aaaaaaaaaabccccccc", 3)
    12
    """
    last_seen = {}
    run_length = 0
    for n, char in enumerate(sequence, start=1):
        if n - last_seen.get(char, -length) > length:
            run_length += 1
            if run_length == length:
                return n
        else:
            run_length = min(run_length + 1, n - last_seen.get(char, 0))
        last_seen[char] = n


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
