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
    areas, perimeters, _ = find_plots(grid)
    return sum(
        area * perimeter
        for plot in areas
        for area, perimeter in zip(areas[plot], perimeters[plot])
    )


def part2(grid):
    """Solve part 2."""
    areas, _, sides = find_plots(grid)
    return sum(
        area * side for plot in areas for area, side in zip(areas[plot], sides[plot])
    )


def find_plots(grid):
    """Find the plots in the grid, including their area, perimeter, and number of sides"""
    seen = set()
    areas, perimeters, sides = defaultdict(list), defaultdict(list), defaultdict(list)
    for pos, plot in grid.items():
        if pos in seen:
            continue
        queue = [pos]
        area, perimeter = 0, 0
        fence = set()
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
                    fence.add((3 * r + new_pos[0], 3 * c + new_pos[1]))
        areas[plot].append(area)
        perimeters[plot].append(perimeter)
        sides[plot].append(walk_fence(fence))

    return areas, perimeters, sides


def walk_fence(fence):
    """Walk the fence to count sides"""
    num_sides = 0
    corners = defaultdict(int)
    while fence:
        row, col = sorted(fence)[0]
        fence.remove((row, col))
        queue = [(row, col)]
        while queue:
            r, c = queue.pop()
            turns = [
                (r + 1, c + 1),
                (r + 1, c - 1),
                (r - 1, c + 1),
                (r - 1, c - 1),
                (r + 3, c + 1),
                (r + 3, c - 1),
                (r - 3, c + 1),
                (r - 3, c - 1),
                (r + 1, c + 3),
                (r + 1, c - 3),
                (r - 1, c + 3),
                (r - 1, c - 3),
                (r + 3, c + 3),
                (r + 3, c - 3),
                (r - 3, c + 3),
                (r - 3, c - 3),
            ]
            straights = (
                [(r, c + 4), (r, c - 4)] if c % 2 == 0 else [(r + 4, c), (r - 4, c)]
            )
            for new_pos in straights + turns:
                if new_pos in fence:
                    queue.append(new_pos)
                    fence.remove(new_pos)
                    corners[(new_pos[0] + r, new_pos[1] + c)] += 1
                    if new_pos[0] != r and new_pos[1] != c:
                        num_sides += 1
                    break
        if r != row and c != col:
            num_sides += 1
    return num_sides


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
