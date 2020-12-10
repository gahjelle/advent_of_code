"""Handy Haversacks

Advent of Code 2020, day 7
Solution by Geir Arne Hjelle, 2020-12-07
"""
import functools
import pathlib
import re
import sys

BAGS = re.compile(r"(?P<outer>.+) bags contain (?P<inner>.+).")
BAGS_INNER = re.compile(r"(?P<num>\d+) (?P<color>[\w ]+) bags?")
BAG_TREE = {}

debug = print if "--debug" in sys.argv else lambda *_: None


def build_bag_tree(lines):
    """Build a tree of bags containing each other"""
    for line in lines:
        match = BAGS.match(line).groupdict()
        outer, inner_bags = match["outer"], match["inner"].split(", ")
        BAG_TREE.setdefault(outer, dict())
        for inner in inner_bags:
            match = BAGS_INNER.match(inner)
            if match:
                bag = match.groupdict()
                BAG_TREE[outer][bag["color"]] = int(bag["num"])


@functools.lru_cache
def can_contain(color):
    """Find bags that can eventually contain the given color"""
    directly = {b for b, c in BAG_TREE.items() if color in c}
    inside = [can_contain(c) for c in directly]
    if inside:
        return directly | set.union(*[can_contain(c) for c in directly])
    else:
        return directly


@functools.lru_cache
def must_contain(color):
    """Find number of bags that must be contained within a bag of the given color"""
    return 1 + sum(must_contain(c) * n for c, n in BAG_TREE[color].items())


def main(args):
    """Solve the problem for all file paths"""
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        solve(file_path)


def solve(file_path):
    """Solve the problem for one file path"""
    # Reset cache
    BAG_TREE.clear()
    can_contain.cache_clear()
    must_contain.cache_clear()

    # Read input file
    print(f"\n{file_path}:")
    build_bag_tree(file_path.read_text().strip().split("\n"))

    # Part 1
    colors_outside = len(can_contain(color="shiny gold"))
    print(f"{colors_outside} colors can eventually contain a shiny gold bag")

    # Part 2
    bags_inside = must_contain(color="shiny gold") - 1
    print(f"{bags_inside} bags are required inside a shiny gold bag")


if __name__ == "__main__":
    main(sys.argv[1:])
