"""AoC 7, 2020: Handy Haversacks"""

# Standard library imports
import pathlib
import sys
from functools import cache

# Third party imports
import parse

BAGS = parse.compile("{color} bags contain {inner}.")
BAGS_INNER = parse.compile("{num:d} {color} ba{gs}")


def parse(puzzle_input):
    """Parse input"""
    return tuple(parse_line(line) for line in puzzle_input.split("\n"))


def parse_line(line):
    """Parse one line of input

    ## Examples:

    >>> parse_line("shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.")
    ('shiny gold', (('dark olive', 1), ('vibrant plum', 2)))
    >>> parse_line("faded blue bags contain no other bags.")
    ('faded blue', ())
    """
    outer = BAGS.parse(line)
    return outer["color"], tuple(
        (inner["color"], inner["num"])
        for bag in outer["inner"].split(", ")
        if (inner := BAGS_INNER.parse(bag))
    )


def part1(data):
    """Solve part 1"""
    bags = tuple((outer, tuple(bag for bag, _ in inner)) for outer, inner in data)
    return len(can_contain(bags, "shiny gold"))


def part2(data):
    """Solve part 2"""
    return must_contain(data, "shiny gold") - 1


@cache
def can_contain(bags, color):
    """List all bags that can contain the given color

    ## Example:

    >>> bags = (("a", ()), ("b", ("a",)), ("c", ("b",)), ("d", ()), ("e", ("d",)))
    >>> sorted(can_contain(bags, "a"))
    ['b', 'c']
    """
    directly = {outer for outer, inner in bags if color in inner}
    if inside := [can_contain(bags, bag) for bag in directly]:
        return directly | set.union(*inside)
    else:
        return directly


@cache
def must_contain(bags, color):
    """Count the number of bags that a given color must contain

    The bag itself is included in the count.

    ## Example:

    >>> bags = (("a", ()), ("b", (("a", 3),)), ("c", (("b", 2),)))
    >>> must_contain(bags, "c")
    9
    """
    inner = next(inner for bag, inner in bags if bag == color)
    return 1 + sum(num * must_contain(bags, bag) for bag, num in inner)


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
