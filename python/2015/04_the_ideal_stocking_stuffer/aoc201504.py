"""AoC 4, 2015: The Ideal Stocking Stuffer"""

# Standard library imports
import hashlib
import itertools
import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    return puzzle_input


def first_md5(secret, prefix):
    """Find the first adventcoint with the given prefix"""
    for num in itertools.count(1):
        md5 = hashlib.md5()
        md5.update(f"{secret}{num}".encode("utf-8"))

        if md5.hexdigest().startswith(prefix):
            return num


def part1(data):
    """Solve part 1"""
    return first_md5(secret=data, prefix="0" * 5)


def part2(data):
    """Solve part 2"""
    return first_md5(secret=data, prefix="0" * 6)


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
