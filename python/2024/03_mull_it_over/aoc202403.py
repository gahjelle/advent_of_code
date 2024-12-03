"""AoC 3, 2024: Mull It Over."""

# Standard library imports
import pathlib
import sys

# Third party imports
import parse

MUL = parse.compile("mul({first:3d},{second:3d})")


def parse_data(puzzle_input):
    """Parse input. Break lines on occurences of do()"""
    return puzzle_input.replace("\n", "").split("do()")


def part1(data):
    """Solve part 1."""
    return sum(multiplies("".join(data)))


def part2(data):
    """Solve part 2."""
    return sum(multiplies("".join(line.split("don't")[0] for line in data)))


def multiplies(text):
    """Find multiply instructions in text and do the multiplication"""
    return (mul["first"] * mul["second"] for mul in MUL.findall(text))


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().rstrip())
        print("\n".join(str(solution) for solution in solutions))
