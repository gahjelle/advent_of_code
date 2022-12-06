"""AoC 3, 2022: Rucksack Reorganization."""

# Standard library imports
import sys
from pathlib import Path

if __name__ == "__main__":
    for path in sys.argv[1:] or [Path(__file__).parent / "input.txt"]:
        print(f"\n{path}:")
        # fmt: off
        part1 = sum((ord((set(r[:len(r)//2]) & set(r[len(r)//2:])).pop()) - 38) % 58 for r in Path(path).read_text().rstrip().split())
        part2 = sum((ord((set(r1) & set(r2) & set(r3)).pop()) - 38) % 58 for lines in [Path(path).read_text().rstrip().split()] for r1, r2, r3 in zip(lines[::3], lines[1::3], lines[2::3]))
        # fmt: on
        print(part1)
        print(part2)
