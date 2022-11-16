"""Conway Cubes

Advent of Code 2020, day 17
Solution by Geir Arne Hjelle, 2020-12-17
"""
# Standard library imports
import itertools
import pathlib
import sys

# Third party imports
import numpy as np

debug = print if "--debug" in sys.argv else lambda *_: None


def parse_cells(text):
    return np.array([[0 if c == "." else 1 for c in ln] for ln in text.split("\n")])


def cells_to_nd(center, ndim, max_generations=6):
    cube = np.zeros(
        np.array(center.shape + (1,) * (ndim - 2)) + 2 * (max_generations + 1),
        dtype=np.uint8,
    )
    # Initialize center plane
    cx, cy, cz = np.array(cube.shape)[:3] // 2
    dx1, dy1 = np.array(center.shape) // 2
    dx2, dy2 = (np.array(center.shape) + 1) // 2
    plane = (
        slice(cx - dx1, cx + dx2),
        slice(cy - dy1, cy + dy2),
    ) + ((slice(cz, cz + 1),) * (ndim - 2))
    cube[plane] = center.reshape(cube[plane].shape)

    return cube


def next_gen(current):
    ndim = current.ndim
    center = (slice(1, -1),) * ndim

    # Count neighbors
    neighbors = np.zeros(current.shape, dtype=np.uint8)
    slices = itertools.product(
        *[[slice(None, -2), slice(1, -1), slice(2, None)]] * ndim
    )
    neighbors[center] = sum(current[s] for s in slices) - current[center]

    # - Active cube: 2 or 3 neighbors active ==> Active
    # - Inactive cube: 3 neighbors active ==> Active
    return ((neighbors == 3) | ((neighbors == 2) & (current == 1))).astype(np.uint8)


def main(args):
    """Solve the problem for all file paths"""
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        solve(file_path)


def solve(file_path):
    """Solve the problem for one file path"""
    print(f"\n{file_path}:")
    center = parse_cells(file_path.read_text().strip())

    # Part 1
    cube = cells_to_nd(center, ndim=3, max_generations=6)
    for _ in range(6):
        cube = next_gen(cube)
    print(f"Active cells in cube after 6 generations: {cube.sum()}")

    # Part 2
    hypercube = cells_to_nd(center, ndim=4, max_generations=6)
    for _ in range(6):
        hypercube = next_gen(hypercube)
    print(f"Active cells in hypercube after 6 generations: {hypercube.sum()}")


if __name__ == "__main__":
    main(sys.argv[1:])
