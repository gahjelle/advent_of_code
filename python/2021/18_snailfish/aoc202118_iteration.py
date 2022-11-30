"""AoC 18, 2021: Snailfish"""

# Standard library imports
import functools
import itertools
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input"""
    return [parse_snailfish(line) for line in puzzle_input.split("\n")]


def parse_snailfish(line):
    """Parse one line of input

    >>> parse_snailfish("[1,2]")
    [(1, 1), (1, 2)]

    >>> parse_snailfish("[[1,2],[[3,4],5]]")
    [(2, 1), (2, 2), (3, 3), (3, 4), (2, 5)]
    """
    level, fish = 0, []
    for char in line:
        match char:
            case "[":
                level += 1
            case "]":
                level -= 1
            case ",":
                pass
            case number:
                fish.append((level, int(number)))

    return fish


def part1(data):
    """Solve part 1"""
    return magnitude(functools.reduce(add_and_reduce, data))


def part2(data):
    """Solve part 2"""
    return max(
        magnitude(add_and_reduce(first, second))
        for first, second in itertools.permutations(data, r=2)
    )


def add_and_reduce(first, second):
    """Add two elements and reduce the result

    >>> add_and_reduce([(1, 1), (1, 2)], [(2, 3), (2, 4), (1, 5)])
    [(2, 1), (2, 2), (3, 3), (3, 4), (2, 5)]
    """
    return reduce([(level + 1, number) for level, number in first + second])


def reduce(snailfish):
    """Reduce a snailfish through explosions and splits

    >>> reduce([(5, 4), (5, 3), (4, 4), (3, 4), (3, 7), (5, 8), (5, 4), (4, 9), (2, 1), (2, 1)])
    [(4, 0), (4, 7), (3, 4), (4, 7), (4, 8), (4, 6), (4, 0), (2, 8), (2, 1)]
    """
    while True:
        snailfish, did_explode = explode(snailfish)
        if did_explode:
            continue

        snailfish, did_split = split(snailfish)
        if did_split:
            continue

        return snailfish


def explode(snailfish):
    """Explode the leftmost deeply nested snailfish

    >>> explode([(0, 1)])
    ([(0, 1)], False)

    >>> explode([(4, 1), (4, 2)])
    ([(4, 1), (4, 2)], False)

    >>> explode([(5, 9), (5, 8), (4, 1), (3, 2), (2, 3), (1, 4)])
    ([(4, 0), (4, 9), (3, 2), (2, 3), (1, 4)], True)

    >>> explode([(2, 3), (3, 2), (4, 1), (5, 7), (5, 3), (2, 6), (3, 5), (4, 4), (5, 3), (5, 2)])
    ([(2, 3), (3, 2), (4, 8), (4, 0), (2, 9), (3, 5), (4, 4), (5, 3), (5, 2)], True)

    >>> explode([(2, 3), (3, 2), (4, 8), (4, 0), (2, 9), (3, 5), (4, 4), (5, 3), (5, 2)])
    ([(2, 3), (3, 2), (4, 8), (4, 0), (2, 9), (3, 5), (4, 7), (4, 0)], True)
    """
    explosive_levels = [idx for idx, (lv, _) in enumerate(snailfish) if lv >= 5]
    if not explosive_levels:
        return snailfish, False
    idx1, idx2, *_ = explosive_levels

    (lv1, nmb1), (_, nmb2) = snailfish[idx1], snailfish[idx2]
    if idx1 == 0:
        before, left = [], []
    else:
        lvlt, nmblt = snailfish[idx1 - 1]
        before, left = snailfish[: idx1 - 1], [(lvlt, nmblt + nmb1)]

    if idx2 + 1 == len(snailfish):
        right, after = [], []
    else:
        (lvrt, nmbrt) = snailfish[idx2 + 1]
        right, after = [(lvrt, nmb2 + nmbrt)], snailfish[idx2 + 2 :]

    return before + left + [(lv1 - 1, 0)] + right + after, True


def split(snailfish):
    """Split the leftmost too high snailfish

    >>> split([(1, 9)])
    ([(1, 9)], False)

    >>> split([(2, 10)])
    ([(3, 5), (3, 5)], True)

    >>> split([(1, 11)])
    ([(2, 5), (2, 6)], True)

    >>> split([(5, 1), (5, 2), (4, 3), (3, 4), (2, 5), (1, 6)])
    ([(5, 1), (5, 2), (4, 3), (3, 4), (2, 5), (1, 6)], False)

    >>> split([(5, 1), (5, 2), (4, 13), (3, 4), (2, 5), (1, 6)])
    ([(5, 1), (5, 2), (5, 6), (5, 7), (3, 4), (2, 5), (1, 6)], True)
    """
    high_fish = [idx for idx, (_, nmb) in enumerate(snailfish) if nmb >= 10]
    if not high_fish:
        return snailfish, False
    idx, *_ = high_fish

    before, (lv, nmb), after = snailfish[:idx], snailfish[idx], snailfish[idx + 1 :]
    return before + [(lv + 1, first := nmb // 2), (lv + 1, nmb - first)] + after, True


def magnitude(snailfish):
    """Find the magnitude of a snailfish

    >>> magnitude([(1, 9), (1, 1)])
    29

    >>> magnitude([(1, 1), (1, 9)])
    21

    >>> magnitude([(2, 9), (2, 1), (2, 1), (2, 9)])
    129

    >>> magnitude([(2, 1), (2, 2), (3, 3), (3, 4), (2, 5)])
    143
    """
    while len(snailfish) > 1:
        levels = [lv for lv, _ in snailfish]
        equal_levels = [
            idx
            for idx, (lv1, lv2) in enumerate(zip(levels[:-1], levels[1:]))
            if lv1 == lv2
        ]
        idx, *_ = equal_levels

        before, after = (snailfish[:idx], snailfish[idx + 2 :])
        (lv, nmblt), (_, nmbrt) = (snailfish[idx], snailfish[idx + 1])
        snailfish = before + [(lv - 1, 3 * nmblt + 2 * nmbrt)] + after

    return snailfish[0][1]


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
