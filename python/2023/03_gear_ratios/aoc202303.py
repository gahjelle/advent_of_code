"""AoC 3, 2023: Gear Ratios."""


# Standard library imports
import collections
import itertools
import math
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    numbers, symbols = [], {}
    parsing_number = False
    for row, line in enumerate(puzzle_input.split("\n")):
        for col, char in enumerate(line):
            if char == ".":
                parsing_number = False
                continue
            if not char.isdigit():
                parsing_number = False
                symbols[(col, row)] = char
            if char.isdigit() and not parsing_number:
                number = ""
                parsing_number = True
                for digit in line[col:]:
                    if digit.isdigit():
                        number += digit
                    else:
                        break
                numbers.append((int(number), neighbors(len(number), col, row)))
    return numbers, symbols


def neighbors(num_digits, col, row):
    """Find neighbor positions of a number.

    ## Example:

    >>> sorted(neighbors(2, 4, 3))
    [(3, 2), (3, 3), (3, 4), (4, 2), (4, 4), (5, 2), (5, 4), (6, 2), (6, 3), (6, 4)]
    """
    return set(
        itertools.product((col - 1, col + num_digits), range(row - 1, row + 2))
    ) | set(itertools.product(range(col, col + num_digits), (row - 1, row + 1)))


def part1(data):
    """Solve part 1."""
    numbers, symbols = data
    return sum(
        number
        for number, neighbors in numbers
        if any(pos in symbols for pos in neighbors)
    )


def part2(data):
    """Solve part 2."""
    numbers, symbols = data
    gears = {pos for pos, symbol in symbols.items() if symbol == "*"}

    ratios = collections.defaultdict(list)
    for number, neighbors in numbers:
        if any((gpos := pos) in gears for pos in neighbors):
            ratios[gpos].append(number)
    return sum(math.prod(parts) for parts in ratios.values() if len(parts) == 2)


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
