"""AoC 18, 2021: Snailfish"""

# Standard library imports
import functools
import itertools
import pathlib
import sys


def parse(puzzle_input):
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

        if not did_explode and not did_split:
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
    if all(lv < 5 for lv, _ in snailfish):
        return snailfish, False

    match snailfish:
        case []:
            return [], False
        case [fish]:
            return [fish], False
        case [(lvlt, nmblt), (lvrt, nmbrt)]:
            if lvlt == lvrt and lvlt >= 5:
                return [(lvlt - 1, 0)], True
            else:
                return [(lvlt, nmblt), (lvrt, nmbrt)], False
        case [(lvlt, nmblt), (lvmid, nmbmid), (lvrt, nmbrt)]:
            if lvlt == lvmid and lvlt >= 5:
                return [(lvlt - 1, 0), (lvrt, nmbmid + nmbrt)], True
            elif lvmid == lvrt and lvmid >= 5:
                return [(lvlt, nmblt + nmbmid), (lvrt - 1, 0)], True
            else:
                return [(lvlt, nmblt), (lvmid, nmbmid), (lvrt, nmbrt)], False
        case [
            (lvlt, nmblt),
            (lvmid, nmbmid),
            (lvrt, nmbrt),
            *rest,
        ] if lvlt == lvmid and lvlt >= 5:
            return [(lvlt - 1, 0), (lvrt, nmbmid + nmbrt), *rest], True
        case [
            (lvlt, nmblt),
            (lv1, nmb1),
            (lv2, nmb2),
            (lvrt, nmbrt),
            *rest,
        ] if lv1 == lv2 and lv1 >= 5:
            return [
                (lvlt, nmblt + nmb1),
                (lv1 - 1, 0),
                (lvrt, nmb2 + nmbrt),
                *rest,
            ], True
        case [fish, *rest]:
            explode_rest, did_explode = explode(rest)
            return [fish, *explode_rest], did_explode
        case _:
            raise ValueError(f"Did not explode {snailfish!r}")


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
    match snailfish:
        case []:
            return [], False
        case [(level, number), *rest] if number >= 10:
            return [
                (level + 1, first := number // 2),
                (level + 1, number - first),
                *rest,
            ], True
        case [fish, *rest]:
            split_rest, did_split = split(rest)
            return [fish, *split_rest], did_split
        case _:
            raise ValueError(f"Did not split {snailfish!r}")


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
        equal_levels = [
            lvlt == lvrt for (lvlt, _), (lvrt, _) in zip(snailfish[:-1], snailfish[1:])
        ]
        idx = equal_levels.index(True)

        (lv, nmblt), (_, nmbrt) = snailfish[idx : idx + 2]
        snailfish = (
            snailfish[:idx] + [(lv - 1, 3 * nmblt + 2 * nmbrt)] + snailfish[idx + 2 :]
        )
    ((_, magnitude),) = snailfish
    return magnitude


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
