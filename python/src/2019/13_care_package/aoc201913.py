"""AoC 13, 2019: Care Package."""

# Standard library imports
import pathlib
import sys
import time

# Advent of Code imports
from aoc import intcode


class Joystick:
    def __init__(self, screen):
        self.screen = screen

    def __iter__(self):
        return self

    def __next__(self):
        """Move the joystick, depending on the position of the ball and paddle.

        If the joystick is in the neutral position, provide 0.
        If the joystick is tilted to the left, provide -1.
        If the joystick is tilted to the right, provide 1.
        """
        paddle_col = next(col for (_, col), tile in self.screen.items() if tile == 3)
        ball_col = next(col for (_, col), tile in self.screen.items() if tile == 4)
        return 0 if paddle_col == ball_col else 1 if paddle_col < ball_col else -1


def parse_data(puzzle_input):
    """Parse input."""
    return [int(number) for number in puzzle_input.split(",")]


def part1(program):
    """Solve part 1."""
    computer = intcode.IntcodeComputer(program)

    screen = {}
    for col, row, tile in computer.iter_n(n=3):
        screen[row, col] = tile

    return sum(tile == 2 for tile in screen.values())


def part2(program):
    """Solve part 2."""
    modified_program = [2 if idx == 0 else value for idx, value in enumerate(program)]
    screen = {}

    computer = intcode.IntcodeComputer(modified_program, input=Joystick(screen))

    score = 0
    for col, row, tile in computer.iter_n(n=3):
        if col == -1 and row == 0:
            score = tile
            continue

        screen[row, col] = tile
        if tile == 4 and "--draw" in sys.argv:
            plot_screen(screen, score)
            time.sleep(0.01)

    return score


def plot_screen(screen, score=0):
    """Plot the screen.

    0 is an empty tile. No game object appears in this tile.
    1 is a wall tile. Walls are indestructible barriers.
    2 is a block tile. Blocks can be broken by the ball.
    3 is a horizontal paddle tile. The paddle is indestructible.
    4 is a ball tile. The ball moves diagonally and bounces off objects.
    """
    tiles = {0: " ", 1: "█", 2: "◇", 3: "═", 4: "●"}

    max_row = max(row for row, _ in screen.keys()) + 1
    max_col = max(col for _, col in screen.keys()) + 1

    print("\033[0;0H", end="")
    for row in range(max_row):
        for col in range(max_col):
            print(tiles[screen.get((row, col), 0)], end="")
        print()

    print(score)


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        if path.startswith("-"):
            continue
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().rstrip())
        print("\n".join(str(solution) for solution in solutions))
