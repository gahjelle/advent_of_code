"""AoC 6, 2024: Guard Gallivant."""

# Standard library imports
import pathlib
import sys

TURN_RIGHT = {(-1, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0)}


def parse_data(puzzle_input):
    """Parse input."""
    return {
        (row, col): char
        for row, line in enumerate(puzzle_input.split("\n"))
        for col, char in enumerate(line)
    }


def part1(grid):
    """Solve part 1."""
    start = next(pos for pos, char in grid.items() if char == "^")
    return len({pos for pos, _ in walk(grid, start)})


def part2(grid):
    """Solve part 2.

    Put an obstacle at each point in the path from part 1. Start the walk right
    in front of the obstacle.
    """
    start = next(pos for pos, char in grid.items() if char == "^")

    # Find all the locations that can be reached, and how they are entered
    original_path = walk(grid, start)
    first_entries = {
        pos: (prev_pos, prev_dir)
        for (prev_pos, prev_dir), (pos, _) in zip(
            original_path[-2::-1], original_path[-1::-1]
        )
        if pos != start
    }

    # Add obstacles at all feasible positions
    obstacles = {
        obstacle
        for obstacle, (pos, dir) in first_entries.items()
        if not walk(grid | {obstacle: "#"}, pos, dir)
    }
    return len(obstacles)


def walk(grid, pos, dir=(-1, 0)):
    """Walk the grid until you walk off the map or get caught in a loop"""
    path = []
    seen = set()
    while pos in grid:
        if (pos, dir) in seen:  # Stuck in a loop
            return []
        path.append((pos, dir))
        seen.add((pos, dir))
        while grid.get(new_pos := (pos[0] + dir[0], pos[1] + dir[1])) == "#":
            dir = TURN_RIGHT[dir]
        pos = new_pos
    return path


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