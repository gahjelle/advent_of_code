"""AoC 17, 2017: Spinlock."""

# Standard library imports
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    return int(puzzle_input)


def part1(step):
    """Solve part 1."""
    buffer = [0]
    idx = 0
    for num in range(1, 2018):
        idx = (idx + step) % len(buffer) + 1
        buffer.insert(idx, num)

    return buffer[idx + 1]


def part2(step):
    """Solve part 2.

    The 0 element always stays at index 0 in the buffer.
    """
    idx, num = 1, 1
    while num < 50_000_000:
        if idx == 1:
            last = num
        num_steps = (num - idx) // step + 1
        num += num_steps
        idx = (idx + (step + 1) * num_steps - 1) % num + 1
    return last


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
