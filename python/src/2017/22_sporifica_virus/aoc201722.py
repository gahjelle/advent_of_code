"""AoC 22, 2017: Sporifica Virus."""

# Standard library imports
import collections
import enum
import pathlib
import sys


class Status(enum.IntEnum):
    CLEAN = 0
    WEAKENED = 1
    INFECTED = 2
    FLAGGED = 3


TURN = {
    (-1, 0): {
        Status.CLEAN: (0, -1),
        Status.WEAKENED: (-1, 0),
        Status.INFECTED: (0, 1),
        Status.FLAGGED: (1, 0),
    },
    (0, 1): {
        Status.CLEAN: (-1, 0),
        Status.WEAKENED: (0, 1),
        Status.INFECTED: (1, 0),
        Status.FLAGGED: (0, -1),
    },
    (1, 0): {
        Status.CLEAN: (0, 1),
        Status.WEAKENED: (1, 0),
        Status.INFECTED: (0, -1),
        Status.FLAGGED: (-1, 0),
    },
    (0, -1): {
        Status.CLEAN: (1, 0),
        Status.WEAKENED: (0, -1),
        Status.INFECTED: (-1, 0),
        Status.FLAGGED: (0, 1),
    },
}


def parse_data(puzzle_input):
    """Parse input."""
    grid = {
        (row, col)
        for row, line in enumerate(puzzle_input.split("\n"))
        for col, char in enumerate(line)
        if char == "#"
    }
    rows = len(puzzle_input.split("\n"))
    cols = max(len(line) for line in puzzle_input.split("\n"))
    return ((rows // 2, cols // 2), grid)


def part1(data, num_bursts=10_000):
    """Solve part 1."""
    return evolve_grid(*data, step=2, num_bursts=num_bursts)


def part2(data, num_bursts=10_000_000):
    """Solve part 2."""
    return evolve_grid(*data, step=1, num_bursts=num_bursts)


def evolve_grid(start_pos, infected, step, num_bursts):
    """Evolve the grid the given number of bursts. Count the number of new infections.

    ## Examples:

    >>> evolve_grid((1, 1), {(0, 2), (1, 0)}, step=2, num_bursts=7)
    5
    >>> evolve_grid((1, 1), {(0, 2), (1, 0)}, step=1, num_bursts=7)
    1
    """
    px, py = start_pos
    dx, dy = -1, 0
    grid = collections.defaultdict(int) | {pos: Status.INFECTED for pos in infected}

    num_infections = 0
    for _ in range(num_bursts):
        status = grid[px, py]
        if status + step == Status.INFECTED:
            num_infections += 1
        dx, dy = TURN[dx, dy][status]
        grid[px, py] = (status + step) % 4
        px, py = px + dx, py + dy

    return num_infections


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
