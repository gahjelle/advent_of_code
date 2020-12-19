"""

Advent of Code 2019, day
Solution by Geir Arne Hjelle, 2019-12-
"""
# Standard library imports
import math
import pathlib
import sys

debug = print if "--debug" in sys.argv else lambda *_: None


def read_reactions(text):
    reactions = {}
    for line in text.strip().split("\n"):
        start, _, end = line.partition("=>")
        end_q, _, end_u = end.strip().partition(" ")
        start_q, start_u = zip(
            *[s.strip().partition(" ")[::2] for s in start.split(",")]
        )
        reactions[end_u] = (
            int(end_q),
            [(s_u, int(s_q)) for s_u, s_q in zip(start_u, start_q)],
        )

    return reactions


def get_raw_quantity(reactions, product_quantity=1, raw="ORE", product="FUEL"):
    needed = {k: v * product_quantity for k, v in reactions[product][1]}
    left_over = {}

    while set(needed) - {raw}:
        for material in needed.copy():
            if material == raw:
                continue

            quantity = needed[material]
            left_over.setdefault(material, 0)
            material_quantity, inputs = reactions[material]
            factor = math.ceil((quantity - left_over[material]) / material_quantity)
            for input_material, input_quantity in inputs:
                needed.setdefault(input_material, 0)
                needed[input_material] += input_quantity * factor
            left_over[material] += material_quantity * factor - quantity
            del needed[material]

    return needed[raw]


def get_product_quantity(reactions, raw_quantity, raw="ORE", product="FUEL"):
    min_quantity, max_quantity = 1, raw_quantity

    while max_quantity - min_quantity > 1:
        test_quantity = (min_quantity + max_quantity) // 2
        cost = get_raw_quantity(
            reactions, raw=raw, product=product, product_quantity=test_quantity
        )
        debug(min_quantity, max_quantity, test_quantity, cost)

        if cost > raw_quantity:
            max_quantity = test_quantity
        elif cost < raw_quantity:
            min_quantity = test_quantity
        else:
            return test_quantity

    return min_quantity


def main(args):
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        print(f"\n{file_path}:")
        reactions = read_reactions(file_path.read_text())

        # Part 1
        ore = get_raw_quantity(reactions)
        print(f"{ore} ORE is needed to produce 1 FUEL")

        # Part 2
        quantity = 1_000_000_000_000
        fuel = get_product_quantity(reactions, raw_quantity=quantity)
        print(f"{quantity:,} ORE can produce {fuel} FUEL")


if __name__ == "__main__":
    main(sys.argv[1:])
