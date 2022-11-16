"""Toboggan Trajectory

Advent of Code 2020, day 3
Solution by Geir Arne Hjelle, 2020-12-03
"""
# Standard library imports
import math
import pathlib
import sys

debug = print if "--debug" in sys.argv else lambda *_: None


def trees(slope, right=3, down=1):
    """Yield trees along the slope in the given direction"""
    idx_y, idx_x = 0, 0
    max_y, max_x = len(slope), len(slope[0])

    while idx_y < max_y:
        yield slope[idx_y][idx_x]
        idx_y += down
        idx_x = (idx_x + right) % max_x


def main(args):
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        print(f"\n{file_path}:")
        slope = [[c == "#" for c in ln.strip()] for ln in file_path.open()]

        # Part 1
        num_trees = sum(trees(slope))
        print(f"Encountered {num_trees} trees")

        # Part 2
        nums_trees = [
            sum(trees(slope, right=1, down=1)),
            sum(trees(slope, right=3, down=1)),
            sum(trees(slope, right=5, down=1)),
            sum(trees(slope, right=7, down=1)),
            sum(trees(slope, right=1, down=2)),
        ]
        tree_score = math.prod(nums_trees)
        print(
            f"Encountered {', '.join(str(t) for t in nums_trees)} "
            f"for a score of {tree_score}"
        )


if __name__ == "__main__":
    main(sys.argv[1:])
