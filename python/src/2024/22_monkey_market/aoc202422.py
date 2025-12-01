"""AoC 22, 2024: Monkey Market."""

# Standard library imports
import collections
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    return [int(line) for line in puzzle_input.split("\n")]


def part1(numbers, num_steps=2000):
    """Solve part 1."""
    return sum(next_random(number, num_steps=num_steps) for number in numbers)


def part2(numbers, num_steps=2000):
    """Solve part 2."""
    differences = collections.defaultdict(int)
    for number in numbers:
        sequence = random_sequence(number, num_steps=num_steps)
        for pattern, value in first_differences(sequence).items():
            differences[pattern] += value
    return max(differences.values())


def next_random(number, num_steps):
    """Calculate the next pseudorandom numbers."""
    prune = (2 << 23) - 1
    for _ in range(num_steps):
        number = number ^ (number << 6) & prune
        number = number ^ (number >> 5) & prune
        number = number ^ (number << 11) & prune
    return number


def random_sequence(number, num_steps):
    """Calculate the sequence of pseudorandom numbers (modulo 10)."""
    prune = (2 << 23) - 1
    sequence = [number % 10]
    for _ in range(num_steps):
        number = number ^ (number << 6) & prune
        number = number ^ (number >> 5) & prune
        number = number ^ (number << 11) & prune
        sequence.append(number % 10)
    return sequence


def first_differences(sequence):
    differences = {}
    diffs = [second - first for first, second in zip(sequence, sequence[1:])]
    for a, b, c, d, value in zip(diffs, diffs[1:], diffs[2:], diffs[3:], sequence[4:]):
        differences.setdefault((a, b, c, d), value)
    return differences


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
