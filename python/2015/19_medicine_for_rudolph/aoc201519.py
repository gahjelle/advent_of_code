"""AoC 19, 2015: Medicine for Rudolph"""

# Standard library imports
import functools
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input"""
    replacements, molecule = puzzle_input.split("\n\n")
    return (
        molecule,
        [tuple(transition.split(" => ")) for transition in replacements.split("\n")],
    )


def part1(data):
    """Solve part 1"""
    return len(replace(*data))


def part2(data):
    """Solve part 2"""
    molecule, replacements = data
    reductions = [(after, before) for before, after in replacements]
    return len(reduce(molecule, reductions))


@functools.cache
def find_all(molecule, atom):
    """Find the indices of all occurences of atom within molecule.

    ## Examples:

    >>> find_all("HOHOHO", "H")
    [0, 2, 4]
    >>> find_all("HOHOHO", "e")
    []
    """
    idx = 0
    indices = []
    while (next_idx := idx + molecule[idx:].find(atom)) >= idx:
        indices.append(next_idx)
        idx = next_idx + 1
    return indices


def replace(molecule, replacements):
    """Do one series of replacements.

    ## Example:

    >>> sorted(replace("HOH", [("H", "HO"), ("H", "OH"), ("O", "HH")]))
    ['HHHH', 'HOHO', 'HOOH', 'OHOH']
    """
    replaced = set()
    for before, after in replacements:
        for idx in find_all(molecule, before):
            replaced.add(molecule[:idx] + after + molecule[idx + len(before) :])
    return replaced


def reduce(current, replacements, target="e"):
    """Build a target molecule.

    ## Example:

    >>> replacements = [("H", "e"), ("O", "e"), ("HO", "H"), ("OH", "H"), ("HH", "O")]
    >>> reduce("HOH", replacements)
    ['e', 'O', 'HH']
    """
    if current == target:
        return []

    for molecule in sorted(replace(current, replacements), key=len):
        steps = reduce(molecule, replacements, target=target)
        if steps is not None:
            return steps + [molecule]


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
