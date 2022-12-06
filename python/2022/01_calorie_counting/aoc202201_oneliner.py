"""AoC 1, 2022: Calorie Counting."""

# Standard library imports
import sys
from pathlib import Path

if __name__ == "__main__":
    for path in sys.argv[1:] or [Path(__file__).parent / "input.txt"]:
        print(f"\n{path}:")
        # fmt: off
        part1 = max(sum(int(cals) for cals in elf.split("\n")) for elf in Path(path).read_text().rstrip().split("\n\n"))
        part2 = sum(sorted(sum(int(cals) for cals in elf.split("\n")) for elf in Path(path).read_text().rstrip().split("\n\n"))[-3:])
        # fmt: on
        print(part1)
        print(part2)
