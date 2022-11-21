"""AoC 14, 2015: Reindeer Olympics"""

# Standard library imports
import itertools
import pathlib
import sys
from typing import NamedTuple

import parse

PARSER = parse.compile(
    "{name} can fly {speed:d} km/s for {stamina:d} seconds, "
    "but then must rest for {rest:d} seconds."
)


class Reindeer(NamedTuple):
    speed: int
    stamina: int
    rest: int
    cycle: int


def parse(puzzle_input):
    """Parse input"""
    return {
        (rd := PARSER.parse(line))["name"]: Reindeer(
            rd["speed"], rd["stamina"], rd["rest"], rd["stamina"] + rd["rest"]
        )
        for line in puzzle_input.split("\n")
    }


def part1(reindeers, time=2503):
    """Solve part 1"""
    return max(distance(reindeer, time) for reindeer in reindeers.values())


def part2(reindeers, time=2503):
    """Solve part 2"""
    positions = [position(rd, time) for rd in reindeers.values()]
    leader = [max(pos) for pos in zip(*positions)]
    scores = [sum(pos == best for pos, best in zip(rd, leader)) for rd in positions]
    return max(scores)


def distance(rd, time):
    """Find the distance that the reindeer flies in the given time.

    ## Examples:

    >>> distance(Reindeer(5, 6, 12, 18), time=1)
    5
    >>> distance(Reindeer(5, 6, 12, 18), time=6)
    30
    >>> distance(Reindeer(5, 6, 12, 18), time=7)
    30
    >>> distance(Reindeer(5, 6, 12, 18), time=18)
    30
    >>> distance(Reindeer(5, 6, 12, 18), time=37)
    65
    """
    cycles, left_time = divmod(time, rd.cycle)
    return rd.speed * (cycles * rd.stamina + min(left_time, rd.stamina))


def position(rd, time):
    """Find the position of the reindeer at each second.

    ## Example:

    >>> position(Reindeer(9, 3, 4, 7), time=15)
    [9, 18, 27, 27, 27, 27, 27, 36, 45, 54, 54, 54, 54, 54, 63]
    """
    cycle = [rd.speed] * rd.stamina + [0] * rd.rest
    cycles = cycle * (time // rd.cycle + 1)
    return list(itertools.accumulate(cycles[:time]))


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
