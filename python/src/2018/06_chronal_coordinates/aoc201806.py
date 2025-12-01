"""AoC 6, 2018: Chronal Coordinates."""

# Standard library imports
import collections
import itertools
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    return [tuple(map(int, line.split(", "))) for line in puzzle_input.split("\n")]


def part1(coords):
    """Solve part 1."""
    return max(len(area) for area in walk_areas(coords).values())


def part2(coords, threshold=10_000):
    """Solve part 2."""
    return len(find_distances(coords, threshold))


def find_boundaries(coords):
    """Find the smallest and largest values of each coordinate."""
    return (
        min(x for x, _ in coords),
        min(y for _, y in coords),
        max(x for x, _ in coords),
        max(y for _, y in coords),
    )


def walk_areas(coords):
    """Use BFSs to find locations closest to each coordinate"""
    min_x, min_y, max_x, max_y = find_boundaries(coords)
    layer = {coord: coord for coord in coords}
    areas = {coord: {coord} for coord in coords}
    seen = set()
    while layer:
        new_layer = collections.defaultdict(set)
        for (x, y), coord in layer.items():
            for nx, ny in [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]:
                if (nx, ny) in seen:
                    continue
                if min_x <= nx <= max_x and min_y <= ny <= max_y:
                    new_layer[nx, ny].add(coord)
        layer = {
            pos: next(iter(coords))
            for pos, coords in new_layer.items()
            if len(coords) == 1
        }
        for pos, coord in layer.items():
            areas[coord].add(pos)
        seen |= set(new_layer)

    # Filter out infinite areas (hitting the boundaries)
    return {
        coord: area
        for coord, area in areas.items()
        if not any(ax in (min_x, max_x) or ay in (min_y, max_y) for ax, ay in area)
    }


def find_distances(coords, threshold):
    """Find the locations with a total distance to all coords less than threshold"""
    min_x, min_y, max_x, max_y = find_boundaries(coords)
    return [
        (x, y)
        for x, y in itertools.product(range(min_x, max_x + 1), range(min_y, max_y + 1))
        if sum(abs(x - cx) + abs(y - cy) for cx, cy in coords) < threshold
    ]


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
