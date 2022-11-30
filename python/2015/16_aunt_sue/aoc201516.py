"""AoC 16, 2015: Aunt Sue"""

# Standard library imports
import pathlib
import sys

GIFT = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}


def parse_data(puzzle_input):
    """Parse input"""
    return dict(parse_sue(line) for line in puzzle_input.split("\n"))


def parse_sue(line):
    """Parse the description of one Aunt Sue.

    ## Example:

    >>> parse_sue("Sue 42: perfumes: 10, trees: 3, cars: 0")
    (42, {'perfumes': 10, 'trees': 3, 'cars': 0})
    """
    sue, _, compounds = line.partition(": ")
    return (
        int(sue.split()[-1]),
        dict(parse_compound(compound) for compound in compounds.split(", ")),
    )


def parse_compound(compound):
    """Parse one compound.

    ## Example:

    >>> parse_compound("goldfish: 6")
    ('goldfish', 6)
    """
    name, _, num = compound.partition(": ")
    return name, int(num)


def part1(aunt_sues):
    """Solve part 1"""
    return next(
        sue
        for sue, compounds in aunt_sues.items()
        if all(value == GIFT[compound] for compound, value in compounds.items())
    )


def part2(aunt_sues):
    """Solve part 2"""
    return next(
        sue for sue, compounds in aunt_sues.items() if retroencabulate(compounds, GIFT)
    )


def retroencabulate(aunt_sue, gift):
    """Retroencabulate the gift to compare it to one Aunt Sue.

    ## Examples:

    >>> retroencabulate({"cats": 3, "cars": 5}, {"cats": 3, "cars": 5})
    False
    >>> retroencabulate({"cats": 4, "cars": 5}, {"cats": 3, "cars": 5})
    True
    >>> retroencabulate({"cars": 5}, {"cats": 3, "cars": 5})
    True
    """
    greater = ("cats", "trees")
    fewer = ("pomeranians", "goldfish")

    for compound, aunt_value in aunt_sue.items():
        gift_value = gift[compound]
        if (
            (compound in greater and gift_value >= aunt_value)
            or (compound in fewer and gift_value <= aunt_value)
            or (compound not in greater + fewer and gift_value != aunt_value)
        ):
            return False
    return True


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
