"""Set and Forget

Advent of Code 2019, day 17
Solution by Geir Arne Hjelle, 2019-12-17
"""
# Standard library imports
import collections
import enum
import pathlib
import sys
import time
from dataclasses import dataclass, field

# Third party imports
import colorama as col
import numpy as np

# Advent of Code imports
from aoc2019.intcode_computer import IntcodeComputer

col.init(autoreset=True)
debug = print if "--debug" in sys.argv else lambda *_: None

MAX_CMD_LEN = 20
MOVEMENT_FUNCTIONS = "ABC"
SLEEP = 0.01


class Block(enum.IntEnum):
    SPACE = 0
    SCAFFOLD = 1
    VISITED = 2
    INTERSECTION = 3
    ROBOT = 10
    ROBOT_EAST = 11
    ROBOT_WEST = 12
    ROBOT_NORTH = 13
    ROBOT_SOUTH = 14
    ROBOT_CRASH = 99


STR2BLOCK = {
    ".": Block.SPACE,
    "#": Block.SCAFFOLD,
    ">": Block.ROBOT_EAST,
    "<": Block.ROBOT_WEST,
    "^": Block.ROBOT_NORTH,
    "v": Block.ROBOT_SOUTH,
    "X": Block.ROBOT_CRASH,
}


BLOCK2DRAW = {
    Block.SPACE: " ",
    Block.SCAFFOLD: f"{col.Fore.WHITE}{col.Style.DIM}▮{col.Style.NORMAL}",
    Block.VISITED: f"{col.Fore.GREEN}{col.Style.DIM}▮{col.Style.NORMAL}",
    Block.INTERSECTION: f"{col.Fore.BLUE}{col.Style.DIM}▮{col.Style.NORMAL}",
    Block.ROBOT_EAST: f"{col.Fore.GREEN}{col.Style.BRIGHT}▶{col.Style.NORMAL}",
    Block.ROBOT_WEST: f"{col.Fore.GREEN}{col.Style.BRIGHT}◀{col.Style.NORMAL}",
    Block.ROBOT_NORTH: f"{col.Fore.GREEN}{col.Style.BRIGHT}▲{col.Style.NORMAL}",
    Block.ROBOT_SOUTH: f"{col.Fore.GREEN}{col.Style.BRIGHT}▼{col.Style.NORMAL}",
    Block.ROBOT_CRASH: f"{col.Fore.RED}{col.Style.BRIGHT}●{col.Style.NORMAL}",
}

FORWARD = {
    Block.ROBOT_EAST: (0, 1),
    Block.ROBOT_WEST: (0, -1),
    Block.ROBOT_NORTH: (-1, 0),
    Block.ROBOT_SOUTH: (1, 0),
}

TURN = {
    "R": {
        Block.ROBOT_EAST: Block.ROBOT_SOUTH,
        Block.ROBOT_WEST: Block.ROBOT_NORTH,
        Block.ROBOT_NORTH: Block.ROBOT_EAST,
        Block.ROBOT_SOUTH: Block.ROBOT_WEST,
    },
    "L": {
        Block.ROBOT_EAST: Block.ROBOT_NORTH,
        Block.ROBOT_WEST: Block.ROBOT_SOUTH,
        Block.ROBOT_NORTH: Block.ROBOT_WEST,
        Block.ROBOT_SOUTH: Block.ROBOT_EAST,
    },
}


@dataclass
class Map:
    computer: IntcodeComputer
    _map: str = field(default="", init=False, repr=False)

    def scan(self):
        map_list = []
        while map_list[-2:] != ["\n", "\n"]:
            output = next(self.computer)
            if output is None:
                break
            if output > 127:
                return output
            block = chr(output)
            if block in STR2BLOCK or block == "\n":
                map_list.append(block)
        map_str = "".join(map_list)
        self._map = np.array(
            [[STR2BLOCK[c] for c in row] for row in map_str.strip().split("\n")]
        )

    def draw(self):
        print(
            col.Cursor.POS(1, 5)
            + "\n".join("".join(BLOCK2DRAW[b] for b in row) for row in self._map)
        )

    def walk(self):
        path, directions = [], []
        pos = tuple(np.concatenate(np.where(self._map >= Block.ROBOT)))
        heading = Block(self._map[pos])
        while True:
            if self._check_move(*pos, heading):
                next_pos = self._next_pos(*pos, heading)
                self._map[pos] = Block.SCAFFOLD + path.count(pos)
                self._map[next_pos] = heading
                path.append(next_pos)
                directions.append("F")
                pos = next_pos
            else:
                for turn, move in TURN.items():
                    if self._check_move(*pos, move[heading]):
                        heading = move[heading]
                        self._map[pos] = heading
                        directions.append(turn)
                        break
                else:
                    break

            if "--draw" in sys.argv:
                self.draw()
                time.sleep(SLEEP)

        return path, directions

    def _next_pos(self, y, x, heading):
        dy, dx = FORWARD[heading]
        return y + dy, x + dx

    def _check_move(self, y, x, heading):
        next_y, next_x = next_pos = self._next_pos(y, x, heading)
        if (0 <= next_y < self._map.shape[0]) and (0 <= next_x < self._map.shape[1]):
            return self._map[next_pos] != Block.SPACE
        else:
            return False


def generate_map(program):
    map = Map(IntcodeComputer(program, input=iter([])))
    map.scan()
    if "--draw" in sys.argv:
        map.draw()

    return map


def count_intersections(path):
    visits = collections.Counter(path)
    return sum(x * y for (y, x), v in visits.items() if v >= 2)


def compile_instructions(directions):
    directions = compress_directions(directions)
    functions = find_functions(directions)
    fragments = split_instructions(directions, functions)
    instructions = assemble_instructions(fragments)
    return f"{instructions}\nn\n"


def compress_directions(directions):
    compressed = []
    counter = 0
    for direction in directions:
        if direction == "F":
            counter += 1
        else:
            if counter > 0:
                compressed.append(str(counter))
                counter = 0
            compressed.append(direction)
    compressed.append(str(counter))

    return compressed


def find_functions(directions):
    functions = collections.defaultdict(int)
    for start in range(0, len(directions), 2):
        for end in range(start + 4, len(directions), 2):
            cmd = ",".join(directions[start:end])
            functions[cmd] += 1

    return sorted(
        [f for f, num in functions.items() if num > 1 and len(f) <= MAX_CMD_LEN],
        key=len,
        reverse=True,
    )


def split_instructions(directions, functions):
    """Depth first search for instruction splits"""
    stack = [(",".join(directions), [])]
    while stack:
        instructions, fragments = stack.pop()
        if not instructions:
            return fragments

        for function in functions:
            if not instructions.startswith(function):
                continue
            if len(set(fragments) | {function}) > len(MOVEMENT_FUNCTIONS):
                continue
            stack.append((instructions[len(function) + 1 :], fragments + [function]))


def assemble_instructions(fragments):
    functions = dict(zip(sorted(set(fragments)), MOVEMENT_FUNCTIONS))
    main_code = ",".join(functions[f] for f in fragments)
    return "\n".join([main_code] + list(functions))


def run_robot(program, instructions):
    program[0] = 2
    input = iter([ord(i) for i in instructions])
    robot = IntcodeComputer(program, input=input)

    while True:
        output = next(robot)
        if output is not None and output > 127:
            return output


def main(args):
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        print(f"\n{file_path}:")
        program = [int(s) for s in file_path.read_text().split(",")]

        # Generate map
        map = generate_map(program)
        path, directions = map.walk()

        # Part 1
        part_1 = count_intersections(path)
        print(f"Sum of alignment parameters are {part_1}")

        # Part 2
        instructions = compile_instructions(directions)
        part_2 = run_robot(program, instructions)
        print(f"Total dust gathered is {part_2}")


if __name__ == "__main__":
    main(sys.argv[1:])
