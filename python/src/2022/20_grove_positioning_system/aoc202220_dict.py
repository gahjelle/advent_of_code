"""AoC 20, 2022: Grove Positioning System."""


# Standard library imports
import itertools
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    return dict(enumerate(int(number) for number in puzzle_input.split("\n")))


def part1(numbers):
    """Solve part 1."""
    positions = {idx: idx for idx in numbers}

    for index, steps in numbers.items():
        positions = move_number(positions, index, steps)

    return grove_coordinates([numbers[positions[pos]] for pos in numbers])


def part2(numbers):
    """Solve part 2."""
    numbers = {idx: number * 811_589_153 for idx, number in numbers.items()}
    positions = {idx: idx for idx in numbers}

    for _, (index, steps) in itertools.product(range(10), numbers.items()):
        positions = move_number(positions, index, steps)

    return grove_coordinates([numbers[positions[pos]] for pos in numbers])


def move_number(positions, index, steps):
    """Move one number."""
    from_pos = next(pos for pos, idx in positions.items() if idx == index)
    to_pos = (from_pos + steps) % (len(positions) - 1)

    if from_pos == to_pos:
        return positions
    elif from_pos < to_pos:
        return (
            positions
            | {to_pos: positions[from_pos]}
            | {pos: positions[pos + 1] for pos in range(from_pos, to_pos)}
        )
    else:
        return (
            positions
            | {to_pos: positions[from_pos]}
            | {pos: positions[pos - 1] for pos in range(to_pos + 1, from_pos + 1)}
        )


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
