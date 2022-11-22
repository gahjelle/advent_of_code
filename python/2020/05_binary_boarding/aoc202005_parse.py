"""AoC 5, 2020: Binary Boarding"""

# Standard library imports
import pathlib
import sys


def decode(string):
    """Decode a boarding pass string into a number"""
    start, end = 0, 2 ** len(string)
    for char in string:
        if char in {"F", "L"}:
            end -= (end - start) // 2
        elif char in {"B", "R"}:
            start += (end - start) // 2

    return start


def get_seat_id(row, col):
    """Calculate seat ID based on row and column"""
    return row * 8 + col


def parse(puzzle_input):
    """Parse input"""
    return [
        get_seat_id(decode(bp[:7]), decode(bp[7:])) for bp in puzzle_input.split("\n")
    ]


def part1(data):
    """Solve part 1"""
    return max(data)


def part2(data):
    """Solve part 2"""
    all_ids = set(range(min(data), max(data) + 1))
    return (all_ids - set(data)).pop()


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
