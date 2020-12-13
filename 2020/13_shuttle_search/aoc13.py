"""Shuttle Search

Advent of Code 2020, day 13
Solution by Geir Arne Hjelle, 2020-12-13
"""
import itertools
import pathlib
import sys
from typing import NamedTuple

debug = print if "--debug" in sys.argv else lambda *_: None


class Bus(NamedTuple):
    id: int
    dt: int


def find_next_departure(busses, current_time):
    """Find next departure"""
    return min((bus.id - current_time % bus.id, bus.id) for bus in busses)


def find_first_timestamp(busses):
    """Find first timestamp when all busses are leaving according to schedule"""
    *other_busses, bus = busses
    if not other_busses:
        return bus.id, itertools.count(bus.id + bus.dt, step=bus.id)

    step, timestamps = find_first_timestamp(other_busses)
    for timestamp in timestamps:
        if (timestamp + bus.dt) % bus.id == 0:
            return step * bus.id, itertools.count(timestamp, step=step * bus.id)


def main(args):
    """Solve the problem for all file paths"""
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        solve(file_path)


def solve(file_path):
    """Solve the problem for one file path"""
    print(f"\n{file_path}:")
    lines = file_path.read_text().strip().split("\n")
    current_time = int(lines[0])
    busses = [Bus(int(id), t) for t, id in enumerate(lines[1].split(",")) if id != "x"]

    # Part 1
    wait, next_bus = find_next_departure(busses, current_time)
    print(f"Bus {next_bus} leaves in {wait} minutes: {next_bus * wait}")

    # Part 2
    _, candidate_generator = find_first_timestamp(busses)
    print(f"The bus schedules line up at {next(candidate_generator)}")


if __name__ == "__main__":
    main(sys.argv[1:])
