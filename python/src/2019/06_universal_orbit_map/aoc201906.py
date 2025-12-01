"""AoC 6, 2019: Universal Orbit Map."""

# Standard library imports
import collections
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    return construct_orbit_map(
        {
            orbit: center
            for line in puzzle_input.split("\n")
            for center, orbit in [line.split(")")]
        }
    )


def part1(orbit_map):
    """Solve part 1."""
    return sum(len(orbit) for orbit in orbit_map.values())


def part2(orbit_map):
    """Solve part 2."""
    # Symmetric difference removes common ancestor, which corresponds to
    # conversion from objects to jumps. Remove YOU and SAN explicitly.
    return len(set(orbit_map["YOU"]) ^ set(orbit_map["SAN"])) - 2


def construct_orbit_map(orbits, start="COM"):
    """Construct the full map of orbits.

    ## Example:

    >>> orbits = {"B": "A", "C": "B", "D": "C", "E": "B"}
    >>> construct_orbit_map(orbits, start="A")
    {'A': [], 'B': ['B'], 'C': ['B', 'C'], 'E': ['B', 'E'], 'D': ['B', 'C', 'D']}
    """
    queue = collections.deque([(start, [])])
    orbit_map = {}
    while queue:
        location, path = queue.popleft()
        orbit_map[location] = path

        for orbit, center in orbits.items():
            if center == location:
                queue.append((orbit, path + [orbit]))

    return orbit_map


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
