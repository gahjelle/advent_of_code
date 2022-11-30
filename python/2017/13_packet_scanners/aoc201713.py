"""AoC 13, 2017: Packet Scanners"""

# Standard library imports
import math
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input"""
    return dict(
        [int(number) for number in line.split(": ")]
        for line in puzzle_input.split("\n")
    )


def part1(data):
    """Solve part 1"""
    caught = [depth for depth, range in data.items() if scanner(range, depth) == 0]
    return sum(depth * data[depth] for depth in caught)


def part2(data):
    """Solve part 2"""
    all_periods = {2 * (rng - 1) for rng in data.values()}
    full_cycle = math.lcm(*all_periods)
    all_delays = set(range(2, full_cycle, 4))
    for depth, rng in data.items():
        period = 2 * (rng - 1)
        start = (period - depth) % period

        if start % 2:
            continue
        caught = range(start, full_cycle, period)
        all_delays -= set(caught)

    return min(all_delays)


def scanner(range, timestamp):
    """Calculate location of scanner at a given timestamp

    >>> scanner(4, 0)
    0

    >>> scanner(4, 1)
    1

    >>> scanner(4, 3)
    3

    >>> scanner(4, 4)
    2

    >>> scanner(4, 6)
    0

    >>> scanner(4, 60001)
    1
    """
    period = 2 * (range - 1)
    position = timestamp % period
    return min(position, period - position)


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
