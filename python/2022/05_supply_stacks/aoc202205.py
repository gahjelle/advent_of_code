"""AoC 5, 2022: Supply Stacks."""

# Standard library imports
import collections
import pathlib
import string
import sys

# Third party imports
import parse

PATTERN = parse.compile("move {num:d} from {start:d} to {end:d}")


def parse_data(puzzle_input):
    """Parse input."""
    stacks, moves = puzzle_input.split("\n\n")
    return parse_stacks(stacks), parse_moves(moves)


def parse_stacks(stack_str):
    """Parse crate information into a dictionary of stacks.

    ## Example:

    >>> parse_stacks("    [G]    \\n[A] [H]    \\n[A] [O] [C]\\n 1   2   3 ")
    defaultdict(<class 'list'>, {2: ['O', 'H', 'G'], 1: ['A', 'A'], 3: ['C']})
    """
    stacks = collections.defaultdict(list)
    for line in stack_str.split("\n"):
        for idx, crate in enumerate(line[1::4], start=1):
            if crate in string.ascii_uppercase:
                stacks[idx].insert(0, crate)
    return stacks


def parse_moves(move_str):
    """Parse moves into a list of tuples.

    ## Example:

    >>> parse_moves("move 1 from 1 to 2\\nmove 42 from 6 to 3")
    [(1, 1, 2), (42, 6, 3)]
    """
    return [
        (m["num"], m["start"], m["end"])
        for line in move_str.split("\n")
        if (m := PATTERN.parse(line))
    ]


def part1(data):
    """Solve part 1."""
    return do_moves(*data, lifo=True)


def part2(data):
    """Solve part 2."""
    return do_moves(*data, lifo=False)


def do_moves(stacks, moves, lifo=True):
    """Move crates around the stacks

    ## Examples:

    >>> stacks = {1: ["H", "A", "G"], 2: ["A"], 3: ["C", "O"]}
    >>> moves = [(2, 1, 3), (4, 3, 2), (1, 2, 1), (1, 2, 3)]
    >>> do_moves(stacks, moves[:1], lifo=True)
    'HAA'
    >>> do_moves(stacks, moves, lifo=True)
    'CGO'
    >>> do_moves(stacks, moves[:1], lifo=False)
    'HAG'
    >>> do_moves(stacks, moves, lifo=False)
    'GOA'
    """
    for num, start, end in moves:
        crates = stacks[start][-num:]
        stacks = stacks | {
            start: stacks[start][:-num],
            end: stacks[end] + (crates[::-1] if lifo else crates),
        }
    return "".join(stack[-1] for _, stack in sorted(stacks.items()))


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
