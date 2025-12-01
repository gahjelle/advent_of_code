"""AoC 14, 2023: Parabolic Reflector Dish."""

# Standard library imports
import itertools
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    return (
        {
            (row, col)
            for row, line in enumerate(puzzle_input.split("\n"))
            for col, char in enumerate(line)
            if char == "O"
        },
        {
            (row, col)
            for row, line in enumerate(puzzle_input.split("\n"))
            for col, char in enumerate(line)
            if char == "#"
        },
    )


def part1(data):
    """Solve part 1."""
    rolling, obstacles = data
    max_row = max(row for row, _ in rolling | obstacles) + 1

    rolled = roll_north(rolling, obstacles)
    return sum(max_row - row for row, _ in rolled)


def roll_north(rolling, obstacles):
    """Roll all rolling stones north."""

    rolled = set()
    for row, col in sorted(rolling, key=lambda pos: pos[0]):
        while (
            row > 0 and (row - 1, col) not in obstacles and (row - 1, col) not in rolled
        ):
            row -= 1

        rolled.add((row, col))
    return rolled


def roll_west(rolling, obstacles):
    """Roll all rolling stones west."""

    rolled = set()
    for row, col in sorted(rolling, key=lambda pos: pos[1]):
        while (
            col > 0 and (row, col - 1) not in obstacles and (row, col - 1) not in rolled
        ):
            col -= 1

        rolled.add((row, col))
    return rolled


def roll_south(rolling, obstacles):
    """Roll all rolling stones south."""
    max_row = max(row for row, _ in rolling | obstacles) + 1

    rolled = set()
    for row, col in sorted(rolling, key=lambda pos: -pos[0]):
        while (
            row < max_row - 1
            and (row + 1, col) not in obstacles
            and (row + 1, col) not in rolled
        ):
            row += 1

        rolled.add((row, col))
    return rolled


def roll_east(rolling, obstacles):
    """Roll all rolling stones east."""
    max_col = max(col for _, col in rolling | obstacles) + 1

    rolled = set()
    for row, col in sorted(rolling, key=lambda pos: -pos[1]):
        while (
            col < max_col - 1
            and (row, col + 1) not in obstacles
            and (row, col + 1) not in rolled
        ):
            col += 1

        rolled.add((row, col))
    return rolled


def part2(data, num_iters=1_000_000_000):
    """Solve part 2."""
    rolling, obstacles = data
    max_row = max(row for row, _ in rolling | obstacles) + 1

    seen = {"".join(str(pos) for pos in sorted(rolling)): 0}
    loads = [0]
    for iter in itertools.count(start=1):
        rolling = roll_north(rolling, obstacles)
        rolling = roll_west(rolling, obstacles)
        rolling = roll_south(rolling, obstacles)
        rolling = roll_east(rolling, obstacles)
        finger_print = "".join(str(pos) for pos in sorted(rolling))
        if finger_print in seen:
            break
        seen[finger_print] = iter
        loads.append(sum(max_row - row for row, _ in rolling))

    first = seen[finger_print]
    cycle_length = iter - first
    return loads[(num_iters - first) % cycle_length + first]


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
