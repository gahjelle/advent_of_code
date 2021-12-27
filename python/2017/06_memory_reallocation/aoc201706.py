"""AoC 6, 2017: Memory Reallocation"""

# Standard library imports
import functools
import itertools
import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    return tuple(int(number) for number in puzzle_input.split())


def part1(data):
    """Solve part 1"""
    _, repeat = redistribute(data)
    return repeat


def part2(data):
    """Solve part 2"""
    first, repeat = redistribute(data)
    return repeat - first


@functools.cache
def redistribute(memory_banks):
    """Redistribute blocks among memory banks, report the first repeated configuration

        7 0 1 2 -->  1 2 3 4  -->  2 3 4 1  -->  3 4 1 2  -->  4 1 2 3  -->  1 2 3 4

    >>> redistribute((7, 0, 1, 2))
    (1, 5)
    """
    num_banks = len(memory_banks)
    seen = {memory_banks: 0}

    for step in itertools.count(start=1):
        max_blocks = max(memory_banks)
        max_idx = next(
            idx for idx, blocks in enumerate(memory_banks) if blocks == max_blocks
        )
        for_all, remaining = divmod(max_blocks, num_banks)
        memory_banks = tuple(
            for_all
            + b * (i != max_idx)
            + (
                i > max_idx
                and i <= max_idx + remaining
                or i <= max_idx - num_banks + remaining
            )
            for i, b in enumerate(memory_banks)
        )
        if memory_banks in seen:
            return seen[memory_banks], step
        else:
            seen[memory_banks] = step


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
