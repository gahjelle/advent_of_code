"""AoC 18, 2022: Boiling Boulders."""

# Standard library imports
import collections
import itertools
import pathlib
import sys

NEIGHBORS = {
    (x, y, z): {
        (x - 1, y, z),
        (x + 1, y, z),
        (x, y - 1, z),
        (x, y + 1, z),
        (x, y, z - 1),
        (x, y, z + 1),
    }
    for x, y, z in itertools.product(range(20), range(20), range(20))
}


def parse_data(puzzle_input):
    """Parse input."""
    return {
        tuple(int(xyz) for xyz in line.split(",")) for line in puzzle_input.split("\n")
    }


def part1(lava):
    """Solve part 1."""
    return count_sides(lava)


def part2(lava):
    """Solve part 2."""
    filled_lava_ball = fill_holes(lava)
    return count_sides(filled_lava_ball)


def count_sides(lava):
    """Count the number of open sides in the lava ball.

    ## Example:

    >>> count_sides({(2, 2, 2)})
    6
    >>> count_sides({(2, 2, 2), (2, 3, 2)})
    10
    >>> count_sides({(2, 2, 2), (2, 3, 3)})
    12
    """
    return sum(side not in lava for cube in lava for side in NEIGHBORS[cube])


def fill_holes(lava):
    """Fill holes in lava ball by shrinking a bounding box to the lava boundary.

    Do a "reverse flood fill" starting from a cube containing all droplets of
    the lava ball. Remove all droplets that can be reached from the outside and
    that are not part of the lava ball.

    ## Example:

    >>> lava = {(0, 1, 1), (1, 0, 1), (1, 1, 0), (1, 1, 2), (1, 2, 1), (2, 1, 1)}
    >>> sorted(fill_holes(lava))
    [(0, 1, 1), (1, 0, 1), (1, 1, 0), (1, 1, 1), (1, 1, 2), (1, 2, 1), (2, 1, 1)]
    >>> fill_holes(lava) - lava
    {(1, 1, 1)}
    """
    all_cubes = set(NEIGHBORS.keys())
    queue = collections.deque([min(all_cubes)])
    seen = set(lava)

    while queue:
        cube = queue.popleft()
        if cube in seen:
            continue

        seen.add(cube)
        if cube in all_cubes and cube not in lava:
            all_cubes.remove(cube)
        queue.extend((NEIGHBORS[cube] & all_cubes) - seen)

    return all_cubes


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
