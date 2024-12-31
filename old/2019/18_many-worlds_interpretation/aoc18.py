"""Many-Worlds Interpretation

Advent of Code 2019, day 18
Solution by Geir Arne Hjelle, 2019-12-21
"""
# Standard library imports
import collections
import enum
import heapq
import itertools
import pathlib
import sys
import time
from dataclasses import dataclass, field

# Third party imports
import colorama
import numpy as np

colorama.init(autoreset=True)
debug = print if "--debug" in sys.argv else lambda *_: None

SLEEP = 0.02


class Block(enum.IntEnum):
    WALL = 0
    SPACE = 1
    START = 2
    KEY = 4
    DOOR = 5
    VISITED = 1000


_COLORS = [
    colorama.Fore.LIGHTBLACK_EX,
    colorama.Fore.RED,
    colorama.Fore.GREEN,
    colorama.Fore.BLUE,
    colorama.Fore.YELLOW,
    colorama.Fore.BLACK,
    colorama.Fore.WHITE,
    colorama.Fore.MAGENTA,
    colorama.Fore.CYAN,
    colorama.Fore.LIGHTBLUE_EX,
    colorama.Fore.LIGHTRED_EX,
    colorama.Fore.LIGHTGREEN_EX,
    colorama.Fore.LIGHTYELLOW_EX,
    colorama.Fore.LIGHTWHITE_EX,
    colorama.Fore.LIGHTMAGENTA_EX,
    colorama.Fore.LIGHTCYAN_EX,
]
_STYLES = [colorama.Style.NORMAL, colorama.Style.BRIGHT]
COLORS = [s + c for s, c in itertools.product(_STYLES, _COLORS)]

STR2BLOCK = {
    "#": Block.WALL,
    ".": Block.SPACE,
    "@": Block.START,
    "[a-z]": Block.KEY,  # Handled by Map.parse_char()
    "[A-Z]": Block.DOOR,  # Handled by Map.parse_char()
}

BLOCK2DRAW = {
    Block.WALL: f"█",
    Block.SPACE: f" ",
    Block.START: f"▪",
    Block.VISITED: f"▣",
    Block.KEY: f"⚷",
    Block.DOOR: f"◫",
}

MOVES = [np.array([0, 1]), np.array([1, 0]), np.array([0, -1]), np.array([-1, 0])]


@dataclass
class Map:
    _map: np.array = field(default=None, repr=False)
    num_keys: int = field(default=-1, init=False)
    keys: list = field(default=None, init=False)
    _paths: dict = field(default=None, init=False, repr=False)

    def __post_init__(self):
        self.keys = np.unique(self._map[self._map // 100 == Block.KEY]).tolist()
        self.num_keys = len(self.keys)

    @classmethod
    def from_text(cls, text):
        def parse_block(char):
            num = ord(char)
            if "a" <= char <= "z":
                return 100 * Block.KEY + (num - 96)
            if "A" <= char <= "Z":
                return 100 * Block.DOOR + (num - 64)
            return STR2BLOCK[char]

        return cls(
            np.array(
                [[parse_block(c) for c in row] for row in text.strip().split("\n")]
            )
        )

    def draw(self):
        def draw_block(num):
            if num >= Block.VISITED:
                block, color = Block.VISITED, num % 100
            elif num >= 100:
                block, color = divmod(num, 100)
            else:
                block, color = num, num

            return COLORS[color] + BLOCK2DRAW[Block(block)]

        print(
            colorama.Cursor.POS(1, 5)
            + "\n".join("".join(draw_block(b) for b in row) for row in self._map)
        )

    def fill_dead_ends(self):
        pos = tuple(np.concatenate(np.where(self._map == Block.START)))
        stack = collections.deque([(pos, (pos,))])
        visited = set()

        while stack:
            (y, x), path = stack.pop()
            available_moves = 0
            for dy, dx in MOVES:
                if (
                    0 <= y + dy < self._map.shape[0]
                    and 0 <= x + dx < self._map.shape[1]
                ):
                    new_pos = (y + dy, x + dx)
                    if len(path) >= 2 and new_pos == path[-2]:
                        continue
                    if self._map[new_pos] == Block.WALL:
                        continue
                    available_moves += 1
                    if new_pos in visited:
                        continue
                    stack.append((new_pos, path + (new_pos,)))
            visited.add((y, x))
            if available_moves == 0:
                if self._map[y, x] == Block.SPACE:
                    stack.append((path[-2], path[:-1]))
                    self._map[y, x] = Block.WALL

            if "--debug_draw" in sys.argv:
                self._map[y, x] += Block.VISITED
                self.draw()
                time.sleep(0.0)
                self._map[y, x] -= Block.VISITED

    def get_paths(self):
        if self._paths is not None:
            return self._paths

        size_y, size_x = self._map.shape
        paths = collections.defaultdict(dict)
        nodes = [Block.START] + self.keys
        for node in nodes:
            pos = tuple(np.concatenate(np.where(self._map == node)))
            seen = {}
            stack = collections.deque([(pos, set(), [])])
            while stack:
                pos, keys, path = stack.pop()
                if pos in seen:
                    continue
                seen[pos] = path

                if self._map[pos] // 100 == Block.KEY and self._map[pos] != node:
                    key = self._map[pos]
                    if key not in keys:
                        paths[node][key] = path, keys

                y, x = pos
                for dy, dx in MOVES:
                    if 0 <= y + dy < size_y and 0 <= x + dx < size_x:
                        new_pos = (y + dy, x + dx)
                        if self._map[new_pos] == Block.WALL:
                            continue
                        if self._map[new_pos] // 100 == Block.DOOR:
                            keys = keys | set(
                                [self._map[new_pos] % 100 + Block.KEY * 100]
                            )
                        stack.appendleft((new_pos, keys, path + [pos]))
        self._paths = paths
        return self._paths

    def find_path(self):
        paths = self.get_paths()
        heap = [(0, Block.START, set(), [])]
        seen = set()

        while heap:
            score, node, keys, path = heapq.heappop(heap)
            if len(keys) == self.num_keys:
                return path

            node_id = node, frozenset(keys)
            if node_id in seen:
                continue
            seen.add(node_id)
            debug(
                colorama.Cursor.UP(1)
                + f"|{'<' * len(keys):>{self.num_keys}}| {len(keys):02d} {score:08d}"
            )
            for other, (to_other, doors) in paths[node].items():
                if keys >= doors:
                    heapq.heappush(
                        heap,
                        (
                            score + len(to_other),
                            other,
                            keys | set([other]),
                            path + to_other,
                        ),
                    )

    def find_path_old(self):
        pos = tuple(np.concatenate(np.where(self._map == Block.START)))
        stack = collections.deque([(pos, (), ())])
        visited = collections.defaultdict(set)

        while stack:
            (y, x), keys, path = stack.pop()
            if len(keys) == self.num_keys:
                break

            for dy, dx in MOVES:
                if (
                    0 <= y + dy < self._map.shape[0]
                    and 0 <= x + dx < self._map.shape[1]
                ):
                    new_pos = (y + dy, x + dx)
                    if new_pos in visited[keys]:
                        continue
                    if self._map[new_pos] == Block.WALL:
                        continue
                    if self._map[new_pos] // 100 == Block.DOOR:
                        if self._map[new_pos] % 100 not in keys:
                            continue
                    new_keys = keys[:]
                    if self._map[new_pos] // 100 == Block.KEY:
                        key = self._map[new_pos] % 100
                        if key not in keys:
                            new_keys = tuple(sorted(keys + (key,)))
                            print(
                                colorama.Cursor.POS(1, 1)
                                + (
                                    f"|{'<' * len(new_keys):>{self.num_keys}}| "
                                    f"{len(new_keys):2d} {len(stack):10d} "
                                    f"{len(visited):7d}"
                                )
                            )
                    stack.appendleft((new_pos, new_keys, path + (new_pos,)))

            for num in range(len(keys) + 1):
                for key_comb in itertools.combinations(keys, num):
                    visited[key_comb].add((y, x))

        return path

    def walk_path(self, path):
        num_keys = 0
        for step, pos in enumerate(path, start=1):
            if self._map[pos] // 100 == Block.KEY:
                self._map[pos] = Block.SPACE
                num_keys += 1
            self._map[pos] += Block.VISITED
            self.draw()
            self._map[pos] -= Block.VISITED
            print(f"Steps: {step:06d}   Keys: {num_keys:02d}")
            time.sleep(SLEEP)


def main(args):
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        print(f"\n{file_path}:")
        map = Map.from_text(file_path.read_text())
        map.fill_dead_ends()

        path = map.find_path()
        if "--draw" in sys.argv:
            map.walk_path(path)
        print(len(path))


if __name__ == "__main__":
    main(sys.argv[1:])
