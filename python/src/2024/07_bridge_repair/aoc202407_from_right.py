"""AoC 7, 2024: Bridge Repair."""

# Standard library imports
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    return [
        [int(number) for number in line.split()]
        for line in puzzle_input.replace(":", "").split("\n")
    ]


def part1(data):
    """Solve part 1."""
    return sum(
        equation[0] for equation in data if is_equation(equation[0], equation[1:])
    )


def part2(data):
    """Solve part 2."""
    return sum(
        equation[0]
        for equation in data
        if is_equation(equation[0], equation[1:], include_concat=True)
    )


def is_equation(target, numbers, include_concat=False):
    """Check that the equation can be satisfied

    Check numbers from the right of the list and abandon as early as possible.

    ## Examples

    >>> is_equation(3267, [81, 40, 27])
    True
    >>> is_equation(1977, [28, 1, 77])
    False
    >>> is_equation(7290, [6, 8, 6, 15], include_concat=True)
    True
    """
    if len(numbers) == 1:
        return target == numbers[0]
    *rest, last = numbers
    if target > last and is_equation(target - last, rest, include_concat):
        return True
    if target % last == 0 and is_equation(target // last, rest, include_concat):
        return True
    if include_concat:
        target_s, last_s = str(target), str(last)
        if (
            len(target_s) > len(last_s)
            and target_s.endswith(last_s)
            and is_equation(int(target_s.removesuffix(last_s)), rest, include_concat)
        ):
            return True

    return False


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
