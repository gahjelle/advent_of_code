"""AoC 25, 2017: The Halting Problem."""

# Standard library imports
import collections
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    lines = puzzle_input.split("\n")
    start = lines[0][-2]
    steps = int(lines[1].split()[5])

    states = collections.defaultdict(dict)
    for state_line in range(3, len(lines), 10):
        state = lines[state_line][-2]
        for line_num in range(state_line + 1, state_line + 8, 4):
            value = int(lines[line_num][-2])
            next_value = int(lines[line_num + 1][-2])
            move = 1 if lines[line_num + 2].split()[-1] == "right." else -1
            next_state = lines[line_num + 3][-2]
            states[state][bool(value)] = bool(next_value), move, next_state

    return start, steps, states


def part1(data):
    """Solve part 1."""
    state, num_steps, states = data
    cursor, tape = 0, set()

    for _ in range(num_steps):
        value, move, state = states[state][cursor in tape]
        if value:
            tape.add(cursor)
        else:
            tape.discard(cursor)
        cursor += move

    return len(tape)


def part2(data):
    """There is no part 2."""


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
