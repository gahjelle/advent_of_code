"""Clock Signal

Advent of Code 2016, day 25
Solution by Geir Arne Hjelle, 2021-01-06
"""

# Standard library imports
import itertools
import pathlib
import sys

# Advent of Code imports
from aoc2016.assembunny import AssembunnyComputer

debug = print if "--debug" in sys.argv else lambda *_: None


def generate_clock_signal(instructions):
    # Remove the infinite loop at the end of the code
    unlooped = "\n".join(instructions.strip().split("\n")[:-1])

    # Check different values of a
    a = 0
    while True:
        outputs = AssembunnyComputer(unlooped, a=a).run()["outputs"]

        # Number of digits at beginning of output correctly being 0, 1, 0, 1, ...
        num_correct = len(
            list(itertools.takewhile(lambda o: o[1] == o[0] % 2, enumerate(outputs)))
        )
        if num_correct == len(outputs):
            return a, "".join(str(o) for o in outputs)

        a += 2 ** num_correct  # Binary jumps keep correct digits


def main(args):
    """Solve the problem for all file paths"""
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        solve(file_path)


def solve(file_path):
    """Solve the problem for one file path"""
    print(f"\n{file_path}:")
    instructions = file_path.read_text()

    # Part 1
    initial_a, output = generate_clock_signal(instructions)
    print(f"{initial_a} generates output {output}...")


if __name__ == "__main__":
    main(sys.argv[1:])
