"""Donut Map

Advent of Code 2019, day 20
Solution by Geir Arne Hjelle, 2019-12-20
"""
# Standard library imports
import collections
import enum
import pathlib
import sys
import time
from dataclasses import dataclass

# Third party imports
import colorama
import numpy as np

colorama.init(autoreset=True)
debug = print if "--debug" in sys.argv else lambda *_: None

SLEEP = 0.04


class Block(enum.IntEnum):
    NULL = 0
    WALL = 1
    SPACE = 2
    PORTAL = 10000


@dataclass
class Direction:
    name: str
    dy: int
    dx: int


DIRECTIONS = [
    Direction("north", -1, 0),
    Direction("east", 0, 1),
    Direction("south", 1, 0),
    Direction("west", 0, -1),
]
STR2BLOCK = {" ": Block.NULL, "#": Block.WALL, ".": Block.SPACE}
BLOCK2DRAW = {
    Block.NULL: f" ",
    Block.WALL: f"{colorama.Fore.LIGHTBLACK_EX}█{colorama.Fore.RESET}",
    Block.SPACE: f"▪",
    Block.PORTAL: f"{colorama.Fore.BLUE}◎{colorama.Fore.RESET}",
}


class Map:
    def __init__(self, map):
        self._map = map
        self._paths = None

    @classmethod
    def from_text(cls, text):
        blocks = np.array(
            [
                [STR2BLOCK.get(c, ord(c)) for c in row]
                for row in text.strip("\n").split("\n")
            ],
            dtype=int,
        )

        return cls(_convert_portals(blocks))

    def fill_dead_ends(self, start="AA"):
        size_y, size_x = self._map.shape

        seen = set()
        stack = [(pos, (pos,)) for pos in zip(*np.where(self._map >= Block.PORTAL))]
        while stack:
            (y, x), path = stack.pop()
            available_moves = 0
            for direction in DIRECTIONS:
                dy, dx = direction.dy, direction.dx
                if 0 <= y + dy < size_y and 0 <= x + dx < size_x:
                    new_pos = (y + dy, x + dx)
                    if len(path) >= 2 and new_pos == path[-2]:
                        continue
                    if self._map[new_pos] in {Block.WALL, Block.NULL}:
                        continue
                    available_moves += 1
                    if new_pos in seen:
                        continue
                    stack.append((new_pos, path + (new_pos,)))
            seen.add((y, x))
            if available_moves == 0:
                if self._map[y, x] == Block.SPACE:
                    stack.append((path[-2], path[:-1]))
                    self._map[y, x] = Block.WALL

            if "--debug_draw" in sys.argv:
                self._map[y, x] *= -1
                self.draw()
                time.sleep(SLEEP)
                self._map[y, x] *= -1

    def get_paths(self):
        if self._paths is not None:
            return self._paths

        size_y, size_x = self._map.shape
        paths = collections.defaultdict(dict)

        portals = sorted(np.unique(self._map[self._map >= Block.PORTAL]))
        for portal in portals:
            seen = {}
            stack = collections.deque(
                [
                    (pos, [], self._is_border(pos))
                    for pos in zip(*np.where(self._map == portal))
                ]
            )
            while stack:
                pos, path, is_border = stack.pop()
                if pos in seen:
                    continue
                seen[pos] = len(path)

                if self._map[pos] >= Block.PORTAL and self._map[pos] != portal:
                    paths[portal][self._map[pos]] = (
                        path + [pos],
                        is_border - self._is_border(pos),
                    )

                y, x = pos
                for direction in DIRECTIONS:
                    dy, dx = direction.dy, direction.dx
                    if 0 <= y + dy < size_y and 0 <= x + dx < size_x:
                        if self._map[y + dy, x + dx] not in {Block.NULL, Block.WALL}:
                            stack.appendleft(
                                ((y + dy, x + dx), path + [pos], is_border)
                            )
        self._paths = paths
        return paths

    def _is_border(self, pos):
        size_y, size_x = self._map.shape
        y, x = pos
        dist_border = min(y, x, size_y - y - 1, size_x - x - 1)
        return int(dist_border == 0)

    def search_shortest(self, start="AA", goal="ZZ", level_diff=0):
        paths = self.get_paths()
        start_id = _get_portal_id(*[ord(c) for c in start])
        goal_id = _get_portal_id(*[ord(c) for c in goal])

        shortest = {}
        stack = collections.deque([(0, start_id, [])])
        while stack:
            level, portal, path = stack.pop()
            if (portal, level) in shortest:
                if len(path) >= len(shortest[(portal, level)]):
                    continue

            shortest[(portal, level)] = path[1:]
            for other, (to_other, dl) in paths[portal].items():
                new_level = level + dl * level_diff
                if new_level < 0 or new_level > len(paths):
                    continue
                stack.appendleft(
                    (new_level, other, path + [p + (level,) for p in to_other])
                )

        try:
            return shortest[(goal_id, 0)]
        except KeyError:
            return []

    def draw(self):
        def draw_block(block):
            if block < 0:
                return f"{colorama.Fore.RED}{draw_block(-block)}{colorama.Fore.RESET}"

            if block >= Block.PORTAL:
                return BLOCK2DRAW[Block.PORTAL]
            else:
                return BLOCK2DRAW[block]

        print(
            colorama.Cursor.POS(1, 5)
            + "\n".join("".join(draw_block(b) for b in row) for row in self._map)
        )

    def draw_path(self, path):
        spacer = " " * (self._map.shape[1] - 20)
        for step, (y, x, level) in enumerate(path, start=1):
            self._map[y, x] *= -1
            self.draw()
            print(f"Step: {step:05d}{spacer}Level: {level:02d}")
            time.sleep(SLEEP)
            if abs(self._map[y, x]) >= Block.PORTAL:
                self._map[self._map < 0] *= -1


def _convert_portals(blocks):
    size_y, size_x = blocks.shape
    all_y, all_x = np.where(blocks > 64)

    for y, x in zip(all_y, all_x):
        if blocks[y, x] <= 64:
            continue

        for direction in DIRECTIONS:
            dy, dx = direction.dy, direction.dx
            if 0 <= y + 2 * dy < size_y and 0 <= x + 2 * dx < size_x:
                if (
                    blocks[y + dy, x + dx] > 64
                    and blocks[y + 2 * dy, x + 2 * dx] == Block.SPACE
                ):
                    portal_id = _get_portal_id(
                        *sorted([blocks[y, x], blocks[y + dy, x + dx]])
                    )
                    blocks[y, x] = Block.NULL
                    blocks[y + dy, x + dx] = Block.NULL
                    blocks[y + 2 * dy, x + 2 * dx] = portal_id
                    break

    return blocks[2:-2, 2:-2]


def _get_portal_id(num_1, num_2):
    return Block.PORTAL + (num_1 - 64) * 100 + (num_2 - 64)


def main(args):
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        print(f"\n{file_path}:")
        map = Map.from_text(file_path.read_text())
        map.fill_dead_ends()

        # Part 1
        path = map.search_shortest(level_diff=0)
        if "--draw" in args:
            map.draw_path(path)
        print(f"{len(path)} steps from AA to ZZ")

        # Part 2
        path = map.search_shortest(level_diff=1)
        if "--draw" in args:
            map.draw_path(path)
        print(f"{len(path)} recursive steps from AA to ZZ")


if __name__ == "__main__":
    main(sys.argv[1:])
