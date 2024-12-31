"""Planet of Discord

Advent of Code 2019, day 24
Solution by Geir Arne Hjelle, 2019-12-26
"""
# Standard library imports
import pathlib
import sys

# Third party imports
import numpy as np

debug = print if "--debug" in sys.argv else lambda *_: None

BIODIVERSITY = 2 ** np.arange(25).reshape(5, 5)


def read_map(text):
    map = np.array(
        [[1 if c == "#" else 0 for c in row] for row in text.strip().split("\n")]
    )
    buffered_shape = [s + 2 for s in map.shape]
    buffered_map = np.zeros(buffered_shape, dtype=int)
    buffered_map[1:-1, 1:-1] = map
    return buffered_map


def calculate_neighbours(map):
    return map[:-2, 1:-1] + map[2:, 1:-1] + map[1:-1, :-2] + map[1:-1, 2:]


def next_step(map, neighbours):
    state = neighbours * (2 * map - 1)
    return ((state == 1) + (state == -1) + (state == -2)).astype(int)


def calculate_biodiversity(map):
    return np.sum(map * BIODIVERSITY)


def evolve_map(map):
    seen = set()
    while True:
        neighbours = calculate_neighbours(map)
        map[1:-1, 1:-1] = next_step(map[1:-1, 1:-1], neighbours)
        biodiversity = calculate_biodiversity(map[1:-1, 1:-1])
        if biodiversity in seen:
            return map[1:-1, 1:-1]

        seen.add(biodiversity)


def main(args):
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        print(f"\n{file_path}:")
        map = read_map(file_path.read_text())

        # Part 1
        part_1 = evolve_map(map.copy())
        print(calculate_biodiversity(part_1))

        # Part 2

        # Third party imports
        import IPython

        IPython.embed()


if __name__ == "__main__":
    main(sys.argv[1:])
