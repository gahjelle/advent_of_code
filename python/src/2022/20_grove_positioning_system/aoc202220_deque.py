"""AoC 20, 2022: Grove Positioning System."""


# Standard library imports
import collections
import itertools
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    return collections.deque(
        enumerate(int(number) for number in puzzle_input.split("\n"))
    )


def part1(numbers):
    """Solve part 1."""
    for index in range(len(numbers)):
        move_number(numbers, index)

    return grove_coordinates([number for _, number in numbers])


def part2(numbers):
    """Solve part 2."""
    numbers = collections.deque(
        [(idx, 811_589_153 * number) for idx, number in sorted(numbers)]
    )
    for _, index in itertools.product(range(10), range(len(numbers))):
        move_number(numbers, index)

    return grove_coordinates([number for _, number in numbers])


def move_number(numbers, number):
    """Move one number."""
    from_idx, total_steps = next(
        (idx, steps)
        for idx, (number_idx, steps) in enumerate(numbers)
        if number_idx == number
    )
    steps = total_steps % (len(numbers) - 1)
    # print(from_idx, total_steps, steps)

    # print(numbers)
    for _ in range(from_idx):
        numbers.append(numbers.popleft())
    value = numbers.popleft()
    for _ in range(steps):
        numbers.append(numbers.popleft())
    numbers.append(value)


def grove_coordinates(numbers):
    """Calculate grove coordinates.

    The grove coordinates can be found by looking at the 1000th, 2000th, and
    3000th numbers after the value 0, wrapping around the list as necessary. Add
    these together.

    ## Examples:

    >>> grove_coordinates([0, 1, 2])
    3
    >>> grove_coordinates([47, 7, 6, 1, 4, 1, 8, 0, 6])
    60
    >>> grove_coordinates([1, 2, -3, 4, 0, 3, -2])
    3
    """
    num_numbers = len(numbers)
    idx_of_zero = numbers.index(0)

    return sum(
        numbers[(idx_of_zero + offset) % num_numbers] for offset in (1000, 2000, 3000)
    )


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
