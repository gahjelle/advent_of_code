"""AoC 4, 2023: Scratchcards."""

# Standard library imports
import pathlib
import sys

# Third party imports
import parse

TICKET_PATTERN = parse.compile("Card {id:3d}: {winning} | {tickets}")


def parse_data(puzzle_input):
    """Parse input."""
    return [
        len(set(match["winning"].split()) & set(match["tickets"].split()))
        for line in puzzle_input.split("\n")
        if (match := TICKET_PATTERN.parse(line))
    ]


def part1(num_winning):
    """Solve part 1."""
    return sum(2 ** (wins - 1) for wins in num_winning if wins > 0)


def part2(num_winning):
    """Solve part 2."""
    counts = [1 for _ in num_winning]
    for index, num in enumerate(num_winning):
        for idx in range(index + 1, index + num + 1):
            counts[idx] += counts[index]
    return sum(counts)


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
