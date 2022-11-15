"""AoC 9, 2015: All in a Single Night"""

# Standard library imports
import itertools
import pathlib
import sys

import parse

DISTANCE_PATTERN = parse.compile("{first} to {second} = {distance:d}")


def parse(puzzle_input):
    """Parse input"""
    distances = {}
    for line in puzzle_input.split("\n"):
        match = DISTANCE_PATTERN.parse(line)
        first, second, distance = match["first"], match["second"], match["distance"]
        distances.setdefault(first, {})[second] = distance
        distances.setdefault(second, {})[first] = distance
    return distances


def part1(data):
    """Solve part 1"""
    return min(calculate_trips(data).values())


def part2(data):
    """Solve part 2"""
    return max(calculate_trips(data).values())


def calculate_trips(distances):
    """Calculate total distance of all trips.

    ## Example:

    >>> dists = {"a": {"b": 3, "c": 7}, "b": {"a": 3, "c": 4}, "c": {"a": 7, "b": 4}}
    >>> calculate_trips(dists)
    {'a-b-c': 7, 'a-c-b': 11, 'b-a-c': 10, 'b-c-a': 11, 'c-a-b': 10, 'c-b-a': 7}
    """
    return {
        "-".join(cities): sum(
            distances[first][second] for first, second in zip(cities, cities[1:])
        )
        for cities in itertools.permutations(distances.keys())
    }


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
