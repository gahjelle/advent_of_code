"""Oxygen System

Advent of Code 2019, day 15
Solution by Geir Arne Hjelle, 2019-12-15
"""
# Standard library imports
import enum
import pathlib
import sys
import time
from collections import UserDict
from dataclasses import dataclass, field
from typing import List

# Third party imports
import colorama

# Advent of Code imports
from aoc2019.intcode_computer import IntcodeComputer

colorama.init(autoreset=True)
debug = print if "--debug" in sys.argv else lambda *_: None

MOVEMENTS = {1: (0, -1), 3: (-1, 0), 2: (0, 1), 4: (1, 0)}
BACKTRACK = {1: 2, 2: 1, 3: 4, 4: 3}
SLEEP = 0.01


class Block(enum.IntEnum):
    WALL = 0
    VISITED = 100
    SPACE = 1
    VISITED_SPACE = 101
    OXYGEN_SYSTEM = 2
    VISITED_OXYGEN_SYSTEM = 102


BLOCK2MAP = {
    Block.WALL: f"{colorama.Fore.YELLOW}█",
    Block.SPACE: f"{colorama.Fore.WHITE}▪",
    Block.VISITED_SPACE: f"{colorama.Fore.BLUE}▣",
    Block.OXYGEN_SYSTEM: f"{colorama.Fore.BLUE}◎",
    Block.VISITED_OXYGEN_SYSTEM: f"{colorama.Fore.BLUE}◎",
}


class Map(UserDict):
    def search(self, start_pos, found_goal):
        """Breadth-first search"""
        time_step = 0
        front = [start_pos]
        while not found_goal(self):
            new_front = []
            for x, y in front:
                for move, (dx, dy) in MOVEMENTS.items():
                    pos = (x + dx, y + dy)
                    if Block.WALL < self.data[pos] < Block.VISITED:
                        self.data[pos] = Block(self.data[pos] + Block.VISITED)
                        new_front.append(pos)
            time_step += 1
            front = new_front

            if "--draw" in sys.argv:
                draw_map(self, f"Step: {time_step:>8d}")

        return time_step

    def __str__(self, origin_x=22, origin_y=25, max_y=44):
        return "".join(
            colorama.Cursor.POS(origin_x + x, origin_y + y) + BLOCK2MAP[b]
            for (x, y), b in self.data.items()
        ) + colorama.Cursor.POS(1, max_y + 1)


@dataclass
class RepairDroid:
    program: List[int] = field(repr=False)
    x: int = 0
    y: int = 0
    map: Map = field(default_factory=Map, repr=False)
    moves: List[int] = field(default_factory=list)

    def explore(self, goal=None):
        computer = IntcodeComputer(self.program, input=self)
        while True:
            block = next(computer)
            if block is None:
                break
            self.map[self.pos] = block = Block(block)
            if block == Block.WALL:
                self.do_move(BACKTRACK[self.moves.pop()])
            elif block == goal:
                break
            if "--draw" in sys.argv:
                draw_map(self.map, "Exploring ship")

    @property
    def pos(self):
        return (self.x, self.y)

    def next_pos(self, move):
        dx, dy = MOVEMENTS[move]
        return (self.x + dx, self.y + dy)

    def do_move(self, move):
        self.x, self.y = self.next_pos(move)

    def __next__(self):
        """Depth first exploration"""
        for move in MOVEMENTS:
            if not self.next_pos(move) in self.map:
                self.do_move(move)
                self.moves.append(move)
                return move

        # Backtrack
        while self.moves:
            self.map[self.pos] += Block.VISITED
            move = BACKTRACK[self.moves.pop()]
            self.do_move(move)
            if self.map[self.pos] < Block.VISITED:
                return move


def draw_map(map, text=""):
    print(str(map) + f"{colorama.Fore.GREEN}{text}")
    time.sleep(SLEEP)


def generate_map(program):
    droid = RepairDroid(program)
    droid.explore()
    return Map({k: Block(v % Block.VISITED) for k, v in droid.map.items()})


def find_oxygen_system(map):
    start_pos = (0, 0)

    def found_goal(map):
        return any(b == Block.VISITED_OXYGEN_SYSTEM for b in map.values())

    return map.search(start_pos, found_goal)


def fill_oxygen(map):
    start_pos = [p for p, b in map.items() if b == Block.OXYGEN_SYSTEM].pop()

    def found_goal(map):
        return all(b != Block.SPACE for b in map.values())

    return map.search(start_pos, found_goal)


def main(args):
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        print(f"\n{file_path}:")
        program = [int(s) for s in file_path.read_text().split(",")]
        map = generate_map(program)

        # Part 1
        part_1 = find_oxygen_system(map.copy())
        print(f"Found oxygen system at step {part_1}")

        # Part 2
        part_2 = fill_oxygen(map.copy())
        print(f"It takes {part_2} minutes to fill the ship with oxygen")


if __name__ == "__main__":
    main(sys.argv[1:])
