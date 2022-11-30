"""AoC 13, 2020: Shuttle Search"""

# Standard library imports
import itertools
import math
import pathlib
import sys
from typing import NamedTuple


class Bus(NamedTuple):
    id: int
    dt: int


def parse_data(puzzle_input):
    """Parse input"""
    time, bus_ids = puzzle_input.split("\n")
    return {
        "time": int(time),
        "bus_ids": [
            Bus(int(id), idx) for idx, id in enumerate(bus_ids.split(",")) if id != "x"
        ],
    }


def part1(data):
    """Solve part 1"""
    return math.prod(find_next_departure(data["bus_ids"], data["time"]))


def part2(data):
    """Solve part 2"""
    return find_first_timestamp(data["bus_ids"])[0]


def find_next_departure(busses, current_time):
    """Find the next departure of some bus

    Return time to wait before departure and bus ID.

    ## Example:

    >>> find_next_departure([Bus(5, 0)], 7)
    (3, 5)
    >>> find_next_departure([Bus(5, 0), Bus(4, 2)], 7)
    (1, 4)
    """
    return min((-current_time % bus.id, bus.id) for bus in busses)


def find_first_timestamp(busses):
    """Find the first timestamp when all busses leave according to schedule

    ## Examples:

    >>> find_first_timestamp([Bus(17, 0), Bus(13, 2), Bus(19, 3)])[0]
    3417
    >>> find_first_timestamp([Bus(67, 0), Bus(7, 1), Bus(59, 2), Bus(61, 3)])[0]
    754018
    >>> find_first_timestamp([Bus(67, 0), Bus(7, 2), Bus(59, 3), Bus(61, 4)])[0]
    779210
    >>> find_first_timestamp([Bus(67, 0), Bus(7, 1), Bus(59, 3), Bus(61, 4)])[0]
    1261476
    >>> find_first_timestamp([Bus(1789, 0), Bus(37, 1), Bus(47, 2), Bus(1889, 3)])[0]
    1202161486
    """
    *other_busses, bus = busses
    if not other_busses:
        return (bus.id - bus.dt) % bus.id, bus.id

    first, step = find_first_timestamp(other_busses)
    for timestamp in itertools.count(first, step=step):
        if (timestamp + bus.dt) % bus.id == 0:
            return timestamp, math.lcm(step, bus.id)


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
