"""AoC 2, 2022: Rock Paper Scissors."""

# Standard library imports
import sys
from functools import reduce
from pathlib import Path

if __name__ == "__main__":
    for path in sys.argv[1:] or [Path(__file__).parent / "input.txt"]:
        print(f"\n{path}:")
        # fmt: off
        part1 = reduce(lambda acc, el: (acc[0].replace(el[1], ""), acc[1] + (el[0] + 1) * acc[0].count(el[1])), enumerate(["BX", "CY", "AZ", "AX", "BY", "CZ", "CX", "AY", "BZ"]), (Path(path).read_text().replace(" ","").rstrip(), 0))[1]
        part2 = reduce(lambda acc, el: (acc[0].replace(el[1], ""), acc[1] + (el[0] + 1) * acc[0].count(el[1])), enumerate(["BX", "CX", "AX", "AY", "BY", "CY", "CZ", "AZ", "BZ"]), (Path(path).read_text().replace(" ","").rstrip(), 0))[1]
        # fmt: on
        print(part1)
        print(part2)
