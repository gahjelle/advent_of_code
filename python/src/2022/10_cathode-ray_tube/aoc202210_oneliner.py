"""AoC 10, 2022: Cathode-Ray Tube."""

# Standard library imports
import sys
from itertools import accumulate, islice
from math import prod
from pathlib import Path
from textwrap import wrap

if __name__ == "__main__":
    for path in sys.argv[1:] or [Path(__file__).parent / "input.txt"]:
        print(f"\n{path}:")
        # fmt: off
        part1 = sum(islice((prod(ns) for ns in enumerate(accumulate((int(n) for n in Path(path).read_text().replace("noop", "0").replace("addx", "0").split()), initial=1), 1)), 19, None, 40))
        part2 = "\n".join(wrap("".join(" █"[(abs(r - (i % 40)) <= 1)] for i, r in enumerate(accumulate((int(n) for n in Path(path).read_text().replace("noop", "0").replace("addx", "0").split()), initial=1))),40))
        # fmt: on
        print(part1)
        print(part2)
