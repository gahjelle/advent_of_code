"""AoC 12, 2024: Garden Groups."""

# Standard library imports
import pathlib
import sys
from collections import defaultdict


def parse_data(puzzle_input):
    """Parse input."""
    return {
        (row, col): char
        for row, line in enumerate(puzzle_input.split("\n"))
        for col, char in enumerate(line)
    }


def part1(grid):
    """Solve part 1."""
    areas, perimeters = find_perimeters(grid)
    return sum(
        area * perimeter
        for plot in areas
        for area, perimeter in zip(areas[plot], perimeters[plot])
    )


def part2(grid):
    """Solve part 2."""
    areas, corners = find_corners(grid)
    return sum(
        area * num_corners
        for plot in areas
        for area, num_corners in zip(areas[plot], corners[plot])
    )


def find_perimeters(grid):
    seen = set()
    areas, perimeters = defaultdict(list), defaultdict(list)
    for pos, plot in grid.items():
        if pos in seen:
            continue
        queue = [pos]
        area, perimeter = 0, 0
        while queue:
            r, c = queue.pop()
            if (r, c) in seen:
                continue
            seen.add((r, c))
            area += 1
            for new_pos in [(r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)]:
                if grid.get(new_pos) == plot:
                    if new_pos not in seen:
                        queue.append(new_pos)
                else:
                    perimeter += 1
        areas[plot].append(area)
        perimeters[plot].append(perimeter)
    return areas, perimeters


def find_corners(grid):
    seen = set()
    areas, corners = defaultdict(list), defaultdict(list)
    for pos, plot in grid.items():
        if pos in seen:
            continue
        queue = [pos]
        area, locations = 0, set()
        while queue:
            r, c = queue.pop()
            if (r, c) in seen:
                continue
            seen.add((r, c))
            area += 1
            locations.add((2 * r, 2 * c))
            for new_pos in [(r + 1, c), (r, c + 1), (r - 1, c), (r, c - 1)]:
                if grid.get(new_pos) == plot and new_pos not in seen:
                    queue.append(new_pos)
        areas[plot].append(area)
        corners[plot].append(count_corners(locations))
    return areas, corners


def count_corners(plot):
    """Count the corners of a plot"""
    diagonals = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
    candidates = {
        (row + drow, col + dcol) for row, col in plot for drow, dcol in diagonals
    }
    num_corners = 0
    for row, col in candidates:
        neighbors = [(row + drow, col + dcol) in plot for drow, dcol in diagonals]
        num_neighbors = sum(neighbors)
        if num_neighbors in [1, 3]:
            num_corners += 1
        elif num_neighbors == 2 and neighbors in [
            [False, True, False, True],
            [True, False, True, False],
        ]:
            num_corners += 2
    return num_corners


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
