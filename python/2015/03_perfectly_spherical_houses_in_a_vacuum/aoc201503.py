"""AoC 3, 2015: Perfectly Spherical Houses in a Vacuum"""

# Standard library imports
import pathlib
import sys

DIRECTIONS = {">": (1, 0), "<": (-1, 0), "^": (0, 1), "v": (0, -1)}


def parse(puzzle_input):
    """Parse input"""
    return [DIRECTIONS[arrow] for arrow in puzzle_input]


def visit(moves):
    """Visit houses based on moves"""
    pos_x, pos_y = 0, 0
    houses = {(pos_x, pos_y)}

    for dx, dy in moves:
        pos_x, pos_y = pos_x + dx, pos_y + dy
        houses.add((pos_x, pos_y))

    return houses


def part1(data):
    """Solve part 1"""
    return len(visit(data))


def part2(data):
    """Solve part 2"""
    santa = visit(data[::2])
    robosanta = visit(data[1::2])

    return len(santa | robosanta)


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
