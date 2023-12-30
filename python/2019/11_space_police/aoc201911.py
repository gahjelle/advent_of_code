"""AoC 11, 2019: Space Police."""

# Standard library imports
import pathlib
import sys
from dataclasses import dataclass

# Third party imports
from advent_of_code_ocr import convert_6

# Advent of Code imports
from aoc import intcode

TURN_RIGHT = {(1, 0): (0, -1), (0, 1): (1, 0), (-1, 0): (0, 1), (0, -1): (-1, 0)}
TURN_LEFT = {(1, 0): (0, 1), (0, 1): (-1, 0), (-1, 0): (0, -1), (0, -1): (1, 0)}


@dataclass
class Robot:
    panels: dict[tuple[int, int], int]
    row: int = 0
    col: int = 0
    drow: int = -1
    dcol: int = 0

    def paint(self, program):
        computer = intcode.IntcodeComputer(program, input=self)
        while True:
            try:
                color = next(computer)
            except StopIteration:
                return self.panels
            self.panels[self.row, self.col] = color
            turn = TURN_RIGHT if next(computer) else TURN_LEFT
            self.drow, self.dcol = turn[self.drow, self.dcol]
            self.row, self.col = self.row + self.drow, self.col + self.dcol

    def __iter__(self):
        return self

    def __next__(self):
        return self.panels.get((self.row, self.col), 0)


def parse_data(puzzle_input):
    """Parse input."""
    return [int(number) for number in puzzle_input.split(",")]


def part1(program):
    """Solve part 1."""
    robot = Robot({(0, 0): 0})
    panels = robot.paint(program)
    return len(panels)


def part2(program):
    """Solve part 2."""
    robot = Robot({(0, 0): 1})
    panels = robot.paint(program)

    min_row = min(row for row, col in panels if panels.get((row, col)))
    min_col = min(col for row, col in panels if panels.get((row, col)))
    max_row = max(row for row, col in panels if panels.get((row, col))) + 1
    max_col = max(col for row, col in panels if panels.get((row, col))) + 1

    text = "\n".join(
        "".join("#" if panels.get((r, c)) else "." for c in range(min_col, max_col))
        for r in range(min_row, max_row)
    )
    return convert_6(text)


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
