"""AoC 14, 2022: Regolith Reservoir."""

# Standard library imports
import pathlib
import sys
from itertools import product

ROCK, SAND, FLOOR = range(3)


def parse_data(puzzle_input):
    """Parse input."""
    return {
        pos: ROCK for line in puzzle_input.split("\n") for pos in parse_structure(line)
    }


def parse_structure(line):
    """Parse one rock structure."""
    corners = line.split(" -> ")
    return [
        pos
        for first, last in zip(corners, corners[1:])
        for pos in parse_line(first, last)
    ]


def parse_line(first, last):
    """Parse one line of rocks."""
    first_col, first_row = [int(coord) for coord in first.split(",")]
    last_col, last_row = [int(coord) for coord in last.split(",")]

    if last_col > first_col or last_row > first_row:
        return product(range(first_col, last_col + 1), range(first_row, last_row + 1))
    elif last_col < first_col:
        return product(range(last_col, first_col + 1), range(first_row, last_row + 1))
    elif last_row < first_row:
        return product(range(first_col, last_col + 1), range(last_row, first_row + 1))


def part1(rocks):
    """Solve part 1."""
    abyss = max(row for _, row in rocks.keys())
    cave = simulate_sand(rocks, source=(500, 0), abyss=abyss)
    return sum(kind == SAND for kind in cave.values())


def part2(rocks):
    """Solve part 2."""
    floor = max(row for _, row in rocks.keys()) + 2
    cave = simulate_sand(
        rocks | {(col, floor): FLOOR for col in range(1000)},
        source=(500, 0),
        abyss=floor,
    )
    return sum(kind == SAND for kind in cave.values())


def simulate_sand(cave, source, abyss):
    """Simulate sand falling from the source."""
    while True:
        sand_pos = pour_sand_unit(cave, source, abyss)
        if sand_pos is None:
            return cave
        cave = cave | {sand_pos: SAND}
        if sand_pos == source:
            return cave


def pour_sand_unit(cave, source, abyss):
    """Pour one unit of sand until it hits something or falls into the abyss."""
    col, source_row = source
    for row in range(source_row, abyss + 1):
        if (col, row + 1) not in cave:
            continue
        elif (col - 1, row + 1) not in cave:
            col -= 1
            continue
        elif (col + 1, row + 1) not in cave:
            col += 1
            continue
        else:
            return (col, row)


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
