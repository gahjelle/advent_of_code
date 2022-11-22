"""AoC 10, 2015: Elves Look, Elves Say"""

# Standard library imports
import itertools
import pathlib
import sys
from dataclasses import dataclass


def parse(puzzle_input):
    """Parse input"""
    return LookSayNumber(puzzle_input)
    return iter(LookSayNumber(puzzle_input))


def part1(data, num_steps=40):
    """Solve part 1"""
    for _ in range(num_steps):
        next(data)
    return data.num_digits


def part2(data, num_additional_steps=10):
    """Solve part 2"""
    for _ in range(num_additional_steps):
        next(data)
    return data.num_digits


@dataclass
class LookSayNumber:
    number: str

    @property
    def num_digits(self):
        """Number of digits in number.

        ## Example:

        >>> LookSayNumber("123456").num_digits
        6
        """
        return len(self.number)

    def __next__(self):
        """Calculate the next LookSayNumber.

        ## Examples:

        >>> next(LookSayNumber("1"))
        LookSayNumber(number='11')
        >>> next(LookSayNumber("11"))
        LookSayNumber(number='21')
        >>> next(LookSayNumber("21"))
        LookSayNumber(number='1211')
        """
        self.number = "".join(
            f"{len(list(elems))}{elem}"
            for elem, elems in itertools.groupby(self.number)
        )
        return self


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
