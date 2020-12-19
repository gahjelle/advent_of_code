"""Amplification Circuit

Advent of Code 2019, day 7
Solution by Geir Arne Hjelle, 2019-12-07
"""
# Standard library imports
import collections
import itertools
import pathlib
import sys

# Advent of Code imports
from aoc2019.intcode_computer import IntcodeComputer

debug = print if "--debug" in sys.argv else lambda *_: None


class InputStream:
    def __init__(self, initial_stream):
        self.stream = collections.deque(initial_stream)

    def append(self, value):
        self.stream.append(value)

    def __next__(self):
        return self.stream.popleft()

    def __iter__(self):
        return self


def run_amplifiers(program, settings):
    debug(f"\nAmplifier settings: {settings}")
    input_stream = InputStream([0])

    amplifiers = []
    for amplifier, amplifier_setting in enumerate(settings):
        amplifiers.append(
            IntcodeComputer(program, itertools.chain([amplifier_setting], input_stream))
        )

    for amplifier in itertools.cycle(amplifiers):
        output = next(amplifier)
        debug(f"Amplifier: {input_stream.stream} -> {output}\n")
        if output is None:
            break

        input_stream.append(output)

    return next(input_stream)


def main(argv):
    for file_path in [pathlib.Path(p) for p in argv if not p.startswith("-")]:
        print(f"\n{file_path}:")
        program = [int(c) for c in file_path.read_text().strip().split(",")]

        # Part 1
        part_1 = max(
            run_amplifiers(program, settings=s)
            for s in itertools.permutations(range(5), 5)
        )
        print(f"Highest signal from amplifiers is {part_1}")

        # Part 2
        part_2 = max(
            run_amplifiers(program, settings=s)
            for s in itertools.permutations(range(5, 10), 5)
        )
        print(f"Highest signal from feedback loop is {part_2}")


if __name__ == "__main__":
    main(sys.argv[1:])
