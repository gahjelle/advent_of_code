"""Cryostasis

Advent of Code 2019, day 25
Solution by Geir Arne Hjelle, 2019-12-25
"""
# Standard library imports
import collections
import pathlib
import sys
from dataclasses import dataclass, field

# Advent of Code imports
from aoc2019.intcode_computer import IntcodeComputer

debug = print if "--debug" in sys.argv else lambda *_: None


@dataclass
class Keyboard:
    buffer: collections.deque = field(default_factory=collections.deque)

    def __next__(self):
        if not self.buffer:
            command = input("")
            for char in command + "\n":
                self.buffer.append(ord(char))

        return self.buffer.popleft()


def run_interactive(intcode):
    droid = IntcodeComputer(intcode, input=Keyboard())
    while True:
        output = next(droid)
        if output is None:
            break
        print(chr(output), end="", flush=True)


def main(args):
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        print(f"\n{file_path}:")
        intcode = [int(s) for s in file_path.read_text().split(",")]

        print(run_interactive(intcode))


if __name__ == "__main__":
    main(sys.argv[1:])
