"""Seating System

Advent of Code 2020, day 11
Solution by Geir Arne Hjelle, 2020-12-11
"""
import enum
import pathlib
import sys
import time

import colorama
import numpy as np
from colorama import Cursor

colorama.init(autoreset=True)
debug = print if "--debug" in sys.argv else lambda *_: None

SLEEP = 0.1
DIRECTIONS = ((-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1))


class Cell(enum.IntEnum):
    FLOOR = -1
    EMPTY = 0
    OCCUPIED = 1


SLEEP = 0.1
DIRECTIONS = ((-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1))
TEXT2CELL = {".": Cell.FLOOR, "L": Cell.EMPTY, "#": Cell.OCCUPIED}
CELL2MAP = {
    Cell.FLOOR: " ",
    Cell.EMPTY: f"{colorama.Fore.GREEN}⎣",
    Cell.OCCUPIED: f"{colorama.Fore.RED}▌",
}


def parse_cells(lines):
    return add_border(np.array([[TEXT2CELL[c] for c in line] for line in lines]))


def cells_to_graph(cells):
    nodes, edges = {}, {}
    rows, cols = cells.shape

    for row in range(rows):
        for col in range(cols):
            if cells[row, col] == Cell.FLOOR:
                continue

            cell_num = row * cols + col
            nodes[cell_num] = cells[row, col]
            edges[cell_num] = find_los_neighbors(cells, row, col)

    return nodes, edges


def find_los_neighbors(cells, row, col):
    rows, cols = cells.shape
    neighbors = []

    for dr, dc in DIRECTIONS:
        cr, cc = row + dr, col + dc
        while 0 <= cr < rows and 0 <= cc < cols:
            if cells[cr, cc] != Cell.FLOOR:
                neighbors.append(cr * cols + cc)
                break
            cr, cc = cr + dr, cc + dc

    return neighbors


def add_border(cells):
    bordered = np.full(tuple(d + 2 for d in cells.shape), TEXT2CELL["."])
    bordered[1:-1, 1:-1] = cells
    return bordered


def draw_cells(cells):
    print(
        f"{Cursor.POS(0, 4)}"
        + "\n".join("".join(CELL2MAP[c] for c in row) for row in cells)
    )


def draw_nodes(nodes, cols):
    def col_row(node):
        return divmod(4 * cols + node, cols)[::-1]

    print(
        "".join(
            f"{Cursor.POS(*col_row(n))}{Cursor.FORWARD()}{CELL2MAP[c]}"
            for n, c in nodes.items()
        )
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


def simulate_cells(cells, occupied_threshold):
    while True:
        if "--draw" in sys.argv:
            draw_cells(cells)
            time.sleep(SLEEP)

        cells, changed = next_cells(cells, adjacent_neighbors, occupied_threshold)
        if not changed:
            return cells


def next_cells(cells, count_neighbors, occupied_threshold):
    neighbors = count_neighbors(cells)

    current = cells[1:-1, 1:-1]
    new_generation = current.copy()
    new_generation[(current == Cell.EMPTY) & (neighbors == 0)] = Cell.OCCUPIED
    new_generation[
        (current == Cell.OCCUPIED) & (neighbors >= occupied_threshold)
    ] = Cell.EMPTY

    return add_border(new_generation), np.any(new_generation != current)


def simulate_nodes(nodes, edges, occupied_threshold, cols):
    while True:
        if "--draw" in sys.argv:
            draw_nodes(nodes, cols)
            time.sleep(SLEEP)

        nodes, changed = next_nodes(nodes, edges, occupied_threshold)
        if not changed:
            return nodes


def next_nodes(nodes, edges, occupied_threshold):
    neighbors = {
        n: (nodes[n], sum(nodes[nb] for nb in nbs)) for n, nbs in edges.items()
    }
    occupied = [n for n, (c, nbs) in neighbors.items() if c == Cell.EMPTY and nbs == 0]
    for node in occupied:
        nodes[node] = Cell.OCCUPIED

    empty = [
        n
        for n, (c, nbs) in neighbors.items()
        if c == Cell.OCCUPIED and nbs >= occupied_threshold
    ]
    for node in empty:
        nodes[node] = Cell.EMPTY

    return nodes, bool(occupied + empty)


def main(args):
    """Solve the problem for all file paths"""
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        solve(file_path)


def solve(file_path):
    """Solve the problem for one file path"""
    print(f"\n{file_path}:")
    cells = parse_cells(file_path.read_text().strip().split("\n"))
    graph = cells_to_graph(cells)

    # Part 1
    part_1 = simulate_cells(cells, occupied_threshold=4)
    num_occupied = np.sum(part_1 == Cell.OCCUPIED)
    print(f"Occupied seats in the end: {num_occupied}")

    # Part 1
    part_2 = simulate_nodes(*graph, occupied_threshold=5, cols=cells.shape[1])
    num_occupied = sum(part_2.values())
    print(f"Occupied seats in the end: {num_occupied}")


if __name__ == "__main__":
    main(sys.argv[1:])
