"""Seating System

Advent of Code 2020, day 11
Solution by Geir Arne Hjelle, 2020-12-11
"""
import enum
import itertools
import pathlib
import sys
import time

import colorama
import numpy as np

colorama.init(autoreset=True)
debug = print if "--debug" in sys.argv else lambda *_: None

SLEEP = 0.1
DIRECTIONS = ((-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1))


class Cell(enum.IntEnum):
    FLOOR = 0
    EMPTY = -1
    OCCUPIED = 1


SLEEP = 0.1
DIRECTIONS = ((-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1))
TEXT2CELL = {".": Cell.FLOOR, "L": Cell.EMPTY, "#": Cell.OCCUPIED}
CELL2MAP = {
    Cell.FLOOR: " ",
    Cell.EMPTY: f"{colorama.Fore.GREEN}⎣",
    Cell.OCCUPIED: f"{colorama.Fore.RED}▌",
}
INLINE_NEIGHBORS = {}


def parse_cells(lines):
    return add_border(np.array([[TEXT2CELL[c] for c in line] for line in lines]))


def add_border(cells):
    bordered = np.full(tuple(d + 2 for d in cells.shape), TEXT2CELL["."])
    bordered[1:-1, 1:-1] = cells
    return bordered


def draw_cells(cells):
    print(
        f"{colorama.Cursor.POS(0, 4)}"
        + "\n".join("".join(CELL2MAP[c] for c in row) for row in cells)
    )


def adjacent_neighbors(cells):
    return (
        (cells[:-2, :-2] == Cell.OCCUPIED).astype(int)
        + (cells[1:-1, :-2] == Cell.OCCUPIED)
        + (cells[2:, :-2] == Cell.OCCUPIED)
        + (cells[:-2, 1:-1] == Cell.OCCUPIED)
        + (cells[2:, 1:-1] == Cell.OCCUPIED)
        + (cells[:-2, 2:] == Cell.OCCUPIED)
        + (cells[1:-1, 2:] == Cell.OCCUPIED)
        + (cells[2:, 2:] == Cell.OCCUPIED)
    )


def inline_neighbors(cells):
    # Cache indices of neighbors for all cells
    if not INLINE_NEIGHBORS:
        for x, y in itertools.product(
            range(1, cells.shape[0] - 1), range(1, cells.shape[1] - 1)
        ):
            if cells[x, y] == Cell.FLOOR:
                continue
            INLINE_NEIGHBORS[(x, y)] = find_inline_neighbors(cells, x, y)

    # Calculate number of occupied neighbors
    neighbors = np.zeros(cells.shape)
    for (x, y), cell_nbs in INLINE_NEIGHBORS.items():
        neighbors[x, y] = np.sum(cells[cell_nbs] == Cell.OCCUPIED)

    return neighbors[1:-1, 1:-1]


def find_inline_neighbors(cells, cell_x, cell_y):
    neighbors_x, neighbors_y = [], []
    max_x, max_y = [s - 1 for s in cells.shape]
    for dx, dy in DIRECTIONS:
        x, y = cell_x + dx, cell_y + dy
        while cells[x, y] == Cell.FLOOR:
            if x <= 0 or x >= max_x or y <= 0 or y >= max_y:
                break
            x, y = x + dx, y + dy
        if cells[x, y] != Cell.FLOOR:
            neighbors_x.append(x)
            neighbors_y.append(y)

    return neighbors_x, neighbors_y


def simulate_until_stable(cells, count_neighbors, occupied_threshold):
    while True:
        if "--draw" in sys.argv:
            draw_cells(cells)
            time.sleep(SLEEP)

        cells, changed = next_generation(cells, count_neighbors, occupied_threshold)
        if not changed:
            return cells


def next_generation(cells, count_neighbors, occupied_threshold):
    neighbors = count_neighbors(cells)

    current = cells[1:-1, 1:-1]
    new_generation = current.copy()
    new_generation[(current == Cell.EMPTY) & (neighbors == 0)] = Cell.OCCUPIED
    new_generation[
        (current == Cell.OCCUPIED) & (neighbors >= occupied_threshold)
    ] = Cell.EMPTY

    return add_border(new_generation), np.any(new_generation != current)


def main(args):
    """Solve the problem for all file paths"""
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        solve(file_path)


def solve(file_path):
    """Solve the problem for one file path"""
    print(f"\n{file_path}:")
    cells = parse_cells(file_path.read_text().strip().split("\n"))

    # Part 1
    part_1 = simulate_until_stable(cells, adjacent_neighbors, occupied_threshold=4)
    num_occupied = np.sum(part_1 == Cell.OCCUPIED)
    print(f"Occupied seats in the end: {num_occupied}")

    # Part 1
    part_2 = simulate_until_stable(cells, inline_neighbors, occupied_threshold=5)
    num_occupied = np.sum(part_2 == Cell.OCCUPIED)
    print(f"Occupied seats in the end: {num_occupied}")


if __name__ == "__main__":
    main(sys.argv[1:])
