"""AoC 1, 2022: Calorie Counting."""

# Standard library imports
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    return [
        sum(int(calories) for calories in elf.split("\n"))
        for elf in puzzle_input.split("\n\n")
    ]


def part1(calories):
    """Solve part 1."""
    return max(calories)


def part2(calories):
    """Solve part 2."""
    return sum(sorted(calories)[-3:])


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
