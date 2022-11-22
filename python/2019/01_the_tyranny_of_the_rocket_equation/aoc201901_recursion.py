"""AoC 1, 2019: The Tyranny of the Rocket Equation"""

# Standard library imports
import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    return [int(mass) for mass in puzzle_input.split()]


def part1(data):
    """Solve part 1"""
    return sum(mass // 3 - 2 for mass in data)


def recursive_fuel(mass):
    """Calculate fuel while recursively taking the mass of the fuel into account"""
    return 0 if (fuel := mass // 3 - 2) <= 0 else fuel + recursive_fuel(fuel)


def part2(data):
    """Solve part 2"""
    return sum(recursive_fuel(mass) for mass in data)


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
