"""AoC 3, 2018: No Matter How You Slice It"""

# Standard library imports
import collections
import itertools
import pathlib
import sys

import parse

CLAIM_PATTERN = parse.compile("#{id:d} @ {col:d},{row:d}: {width:d}x{height:d}")


def parse(puzzle_input):
    """Parse input"""
    return dict(parse_claim(claim) for claim in puzzle_input.split("\n"))


def parse_claim(claim_text):
    """Parse one claim

    ## Example:

    >>> parse_claim("#7 @ 19,77: 2x3")
    (7, [(19, 77), (19, 78), (19, 79), (20, 77), (20, 78), (20, 79)])
    """
    claim = CLAIM_PATTERN.parse(claim_text)
    return (
        claim["id"],
        [
            (claim["col"] + dc, claim["row"] + dr)
            for dc in range(claim["width"])
            for dr in range(claim["height"])
        ],
    )


def part1(data):
    """Solve part 1"""
    overlaps = collections.Counter(itertools.chain(*data.values()))
    return sum(count > 1 for count in overlaps.values())


def part2(data):
    """Solve part 2"""
    overlaps = collections.Counter(itertools.chain(*data.values()))
    no_overlaps = {rect for rect, count in overlaps.items() if count == 1}
    return next(
        claim_id
        for claim_id, rects in data.items()
        if all(rect in no_overlaps for rect in rects)
    )


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
