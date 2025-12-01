"""AoC 10, 2024: Hoof It."""

# Standard library imports
import collections
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    return {
        (row, col): int(char)
        for row, line in enumerate(puzzle_input.split("\n"))
        for col, char in enumerate(line)
    }


def part1(grid):
    """Solve part 1."""
    return sum(
        len(walk(grid, trailhead)) for trailhead, height in grid.items() if height == 0
    )


def part2(grid):
    """Solve part 2."""
    return sum(
        sum(walk(grid, trailhead).values())
        for trailhead, height in grid.items()
        if height == 0
    )


def walk(grid, start, target=9):
    """Walk the grid and count how many paths that can be walked to reach targets."""
    layer = {start: 1}
    for height in range(1, target + 1):
        new_layer = collections.defaultdict(int)
        for pos, num_paths in layer.items():
            for dir in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                new_pos = (pos[0] + dir[0], pos[1] + dir[1])
                if grid.get(new_pos) == height:
                    new_layer[new_pos] += num_paths
        layer, new_layer = new_layer, collections.defaultdict(int)

    return layer


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
