"""AoC 7, 2019: Amplification Circuit."""

# Standard library imports
import collections
import itertools
import pathlib
import sys

# Advent of Code imports
from aoc import intcode


class NumberStream:
    """A stream of numbers that can be popped and appended to."""

    def __init__(self, initial_stream):
        self.stream = collections.deque(initial_stream)

    def append(self, value):
        self.stream.append(value)

    def __next__(self):
        return self.stream.popleft()

    def __iter__(self):
        return self

    def __repr__(self):
        return f"{type(self).__name__}({self.stream})"


def parse_data(puzzle_input):
    """Parse input."""
    return [int(number) for number in puzzle_input.split(",")]


def part1(program):
    """Solve part 1."""
    return max(
        run_amplifiers(program, settings)
        for settings in itertools.permutations(range(5))
    )


def part2(program):
    """Solve part 2."""
    return max(
        run_amplifiers(program, settings)
        for settings in itertools.permutations(range(5, 10))
    )


def run_amplifiers(program, settings):
    """Run amplifiers with the given settings."""
    stream = NumberStream(initial_stream=[0])
    amplifiers = [
        intcode.IntcodeComputer(program, input=itertools.chain([setting], stream))
        for setting in settings
    ]

    for amplifier in itertools.cycle(amplifiers):
        try:
            output = next(amplifier)
        except StopIteration:
            break
        stream.append(output)
    return next(stream)


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
