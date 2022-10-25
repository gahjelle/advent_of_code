"""AoC 3, 2019: Crossed Wires"""

# Standard library imports
import pathlib
import sys

DIRECTIONS = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}


def parse(puzzle_input):
    """Parse input"""
    first, second = puzzle_input.split("\n")
    return parse_wire(first), parse_wire(second)


def parse_wire(wire):
    """Parse the description of one wire

    ## Example:

    >>> parse_wire("U2,R1,D3,L2")
    [(0, 1), (0, 2), (1, 2), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    """
    return coordinates((step[0], int(step[1:])) for step in wire.split(","))


def coordinates(wire):
    """Convert wire steps to coordinates

    ## Example:

    >>> coordinates([("U", 2), ("R", 1), ("D", 3), ("L", 2)])
    [(0, 1), (0, 2), (1, 2), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
    """
    pos_x, pos_y = 0, 0
    coords = []
    for direction, steps in wire:
        dx, dy = DIRECTIONS[direction]
        for _ in range(steps):
            pos_x += dx
            pos_y += dy
            coords.append((pos_x, pos_y))
    return coords


def part1(data):
    """Solve part 1"""
    first, second = data
    crossings = set(first) & set(second)
    return min(manhattan(crossing) for crossing in crossings)


def part2(data):
    """Solve part 2"""
    first, second = [enumerate_steps(coordinates) for coordinates in data]
    crossings = set(first) & set(second)
    return min(first[crossing] + second[crossing] for crossing in crossings)


def manhattan(pos):
    """Manhattan distance from origin to position

    ## Examples:

    >>> manhattan((4, 2))
    6
    >>> manhattan((-2, 19))
    21
    """
    pos_x, pos_y = pos
    return abs(pos_x) + abs(pos_y)


def enumerate_steps(coordinates):
    """Enumerate the steps for each coordinate

    ## Example:

    >>> enumerate_steps([(0, 1), (0, 2), (1, 2), (1, 1), (0, 1), (-1, 1)])
    {(0, 1): 1, (0, 2): 2, (1, 2): 3, (1, 1): 4, (-1, 1): 6}
    """
    steps = {}
    for idx, pos in enumerate(coordinates, start=1):
        steps.setdefault(pos, idx)
    return steps


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
