"""No Matter How You Slice It

Advent of Code 2018, day 3
Solution by Geir Arne Hjelle, 2018-12-03
"""
# Standard library imports
import re
import sys

# Third party imports
import numpy as np

MAX_SIZE = 1000

debug = print if "--debug" in sys.argv else lambda *_: None


def overlaps(claims):
    counts = np.zeros((MAX_SIZE, MAX_SIZE), dtype=int)
    claim_dict = dict()

    for claim in claims:
        claim_id, _, claim_spec = claim.partition("@")
        x0, y0, dx, dy = (int(d) for d in re.split(r"[,:x]", claim_spec))
        counts[x0 : x0 + dx, y0 : y0 + dy] += 1
        claim_dict[claim_id.strip()] = counts[x0 : x0 + dx, y0 : y0 + dy]

    num_overlaps = np.sum(counts >= 2)
    no_overlaps = [k for k, v in claim_dict.items() if np.all(v == 1)]

    return num_overlaps, no_overlaps


def main(args):
    for filename in args:
        if filename.startswith("--"):
            continue

        print(f"\n{filename}:")
        with open(filename, mode="r") as fid:
            claims = [l.strip() for l in fid]
            num_overlaps, no_overlaps = overlaps(claims)
            print(f"Number of overlaps: {num_overlaps}")
            print(f"No overlaps: {', '.join(no_overlaps)}")


if __name__ == "__main__":
    main(sys.argv[1:])
