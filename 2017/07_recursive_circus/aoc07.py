"""Recursive Circus

Advent of Code 2017, day 7
Solution by Geir Arne Hjelle, 2021-10-25
"""
# Standard library imports
import statistics
import sys

# Third party imports
import parse

TOP_LEVEL_PROGRAM = parse.compile("{program} ({weight:d})")
SUPPORTING_PROGRAM = parse.compile("{program} ({weight:d}) -> {subprograms}")


def read_structure(fid):
    """Read strcture of programs"""
    weights = {}
    structure = {}
    for line in fid:
        if match := TOP_LEVEL_PROGRAM.parse(line.strip()):
            weights[match["program"]] = match["weight"]
            structure[match["program"]] = []

        elif match := SUPPORTING_PROGRAM.parse(line.strip()):
            weights[match["program"]] = match["weight"]
            structure[match["program"]] = match["subprograms"].split(", ")

    return structure, weights


def find_root_program(structure):
    """Find the bottom program"""
    children = set.union(*[set(v) for v in structure.values()])
    return (set(structure) - children).pop()


def balance_towers(root, structure, weights):
    """Balance all towers so that they have the same weights"""
    weight, equal, subweights = zip(
        *(
            tower_weight(child, structure, weights, check_equal=True)
            for child in structure[root]
        )
    )

    if all(equal) and any(w != weight[0] for w in weight):
        correct_weight = statistics.mode(weight)
        wrong_idx = [i for i, w in enumerate(weight) if w != correct_weight][0]
        wrong_disc = structure[root][wrong_idx]
        return wrong_disc, weights[wrong_disc] - (weight[wrong_idx] - correct_weight)

    for child in structure[root]:
        if structure[child]:
            value = balance_towers(child, structure, weights)
            if value is not None:
                return value


def tower_weight(root, structure, weights, check_equal=False):
    """Calculate the weight of one subtower"""
    subweights = [tower_weight(disc, structure, weights) for disc in structure[root]]
    total_weight = weights[root] + sum(subweights)
    if not check_equal:
        return total_weight

    all_equal = all(w == subweights[0] for w in subweights) if subweights else True
    return total_weight, all_equal, subweights


def main(args):
    for filename in args:
        if filename.startswith("--"):
            continue

        print("\n{}:".format(filename))
        with open(filename, mode="r") as fid:
            structure, weights = read_structure(fid)

            root = find_root_program(structure)
            print(f"{root!r} is the bottom program")

            disc, weight = balance_towers(root, structure, weights)
            print(f"{disc!r} has the wrong weight, it should be {weight}")


if __name__ == "__main__":
    debug = print if "--debug" in sys.argv else lambda *_: None
    main(sys.argv[1:])
