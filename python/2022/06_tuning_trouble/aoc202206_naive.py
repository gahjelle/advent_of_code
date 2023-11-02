"""AoC 6, 2022: Tuning Trouble."""

# Standard library imports
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    return puzzle_input


def part1(sequence):
    """Solve part 1."""
    return find_packet_marker(sequence)


def part2(sequence):
    """Solve part 2."""
    return find_message_marker(sequence)


def find_packet_marker(sequence):
    """Find the first start-of-packet marker of length four.

    A marker of length N is a sequence of N characters that are all different.

    ## Examples:

    >>> find_packet_marker("geirarne")
    4
    >>> find_packet_marker("aaaaaaaaaabcdddddd")
    13
    >>> find_packet_marker("aaaabcd")
    7
    """
    first, second, third, fourth, *rest = sequence
    marker = 4
    while any(
        [
            first == second,
            first == third,
            first == fourth,
            second == third,
            second == fourth,
            third == fourth,
        ]
    ):
        marker += 1
        first = second
        second = third
        third = fourth
        fourth, *rest = rest

    return marker


def find_message_marker(sequence):
    """Find the first start-of-message marker of length fourteen.

    A marker of length N is a sequence of N characters that are all different.

    ## Examples:

    >>> find_message_marker("aabcdefghijklmnnnn")
    15
    """
    head, rest = sequence[:14], sequence[14:]
    marker = 14
    while len(set(head)) < 14:
        marker += 1
        head = head[1:] + rest[:1]
        rest = rest[1:]
    return marker


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
