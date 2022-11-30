"""AoC 5, 2017: A Maze of Twisty Trampolines, All Alike."""

# Standard library imports
import itertools
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    return [int(line) for line in puzzle_input.split("\n")]


def part1(data):
    """Solve part 1."""
    return jump_outside(data.copy())


def part2(data):
    """Solve part 2."""
    return conditional_jump_outside(data.copy(), threshold=3)


def jump_outside(offsets):
    """Count steps to jump outside of offsets.

        (0)  1
        (1)  1
         1  (1)

    >>> jump_outside([0, 1])
    3
    """
    pointer = 0
    num_offsets = len(offsets)
    for step in itertools.count(start=1):
        jump = offsets[pointer]
        offsets[pointer] += 1
        pointer += jump

        if pointer >= num_offsets:
            return step


def conditional_jump_outside(offsets, threshold):
    """Count steps to jump outside of offsets, decrease offsets if they are
    above threshold.

        (0)  3   0   0   -1
        (1)  3   0   0   -1
         2  (3)  0   0   -1
         2   4   0   0  (-1)
         2   4   0  (0)   0
         2   4   0  (1)   0
         2   4   0   2   (0)
         2   4   0   2   (1)

    >>> jump_outside([0, 3, 0, 0, -1])
    8
    """
    pointer = 0
    num_offsets = len(offsets)
    for step in itertools.count(start=1):
        jump = offsets[pointer]
        offsets[pointer] += 1 if jump < threshold else -1
        pointer += jump

        if pointer >= num_offsets:
            return step


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
