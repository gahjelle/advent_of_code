"""Care Package

Advent of Code 2019, day 13
Solution by Geir Arne Hjelle, 2019-12-13
"""
import enum
import pathlib
import sys

import colorama
import numpy as np

from aoc2019.intcode_computer import IntcodeComputer

debug = print if "--debug" in sys.argv else lambda *_: None
colorama.init()


class Tile(enum.IntEnum):
    EMPTY = 0
    WALL = 1
    BLOCK = 2
    PADDLE = 3
    BALL = 4


TILE2STR = {
    Tile.EMPTY: " ",
    Tile.WALL: "█",
    Tile.BLOCK: "◈",
    Tile.PADDLE: "▭",
    Tile.BALL: "●",
}


class Joystick:
    def __init__(self, screen):
        self.screen = screen

    def __next__(self):
        ball_x = np.where(np.any(self.screen == Tile.BALL, axis=0))[0][0]
        paddle_x = np.where(np.any(self.screen == Tile.PADDLE, axis=0))[0][0]
        return np.sign(ball_x - paddle_x)


def build_screen(program):
    """Build dictionary first since we don't know the size"""
    computer = IntcodeComputer(program, input=None)
    screen = {}

    for x, y, tile_id in computer.iter(n=3):
        screen[(x, y)] = Tile(tile_id)

    return _to_array(screen)


def _to_array(screen):
    coords_x, coords_y = zip(*screen.keys())
    max_x, max_y = max(coords_x), max(coords_y)
    array = np.full((max_y + 1, max_x + 1), np.nan)

    for (x, y), tile in screen.items():
        array[y, x] = tile

    return array


def draw_screen(screen, score=0):
    print(
        f"{colorama.Cursor.POS(1, 5)}Score: {score:>08d}\n"
        + "\n".join("".join(TILE2STR[t] for t in row) for row in screen)
    )


def run_game(program, screen, num_quarters=2):
    program[0] = num_quarters
    computer = IntcodeComputer(program, input=Joystick(screen))

    score = 0
    for x, y, tile_id in computer.iter(n=3):
        if x == -1 and y == 0:
            score = tile_id
            continue

        screen[y, x] = tile_id
        if "--draw" in sys.argv:
            draw_screen(screen, score)

    return score


def main(args):
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        print(f"\n{file_path}:")
        program = [int(s) for s in file_path.read_text().split(",")]

        # Part 1
        screen = build_screen(program)
        num_blocks = np.sum(screen == Tile.BLOCK)
        print(f"There are {num_blocks} blocks on the screen")

        # Part 2
        score = run_game(program, screen)
        print(f"The score is {score} after the game is beaten")


if __name__ == "__main__":
    main(sys.argv[1:])
