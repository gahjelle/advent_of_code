"""AoC 2, 2021: Dive!"""

# Standard library imports
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    return [parse_command(command) for command in puzzle_input.split("\n")]


def parse_command(command):
    """Parse one command.

    >>> parse_command("forward 12")
    (12, 0)

    >>> parse_command("up 3")
    (0, -3)

    >>> parse_command("down 7")
    (0, 7)
    """
    match command.split():
        case ["forward", steps]:
            return (int(steps), 0)
        case ["up", steps]:
            return (0, -int(steps))
        case ["down", steps]:
            return (0, int(steps))


def part1(data):
    """Solve part 1."""
    return sum(dhpos for dhpos, _ in data) * sum(ddepth for _, ddepth in data)


def part2(data):
    """Solve part 2."""
    horizontal_pos, depth, aim = 0, 0, 0
    for command in data:
        match command:
            case (0, daim):
                aim += daim
            case (dpos, 0):
                horizontal_pos += dpos
                depth += dpos * aim

    return horizontal_pos * depth


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
