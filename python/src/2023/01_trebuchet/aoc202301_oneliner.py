"""AoC 1, 2023: Trebuchet?!."""

# Standard library imports
import sys
from pathlib import Path

if __name__ == "__main__":
    for path in sys.argv[1:] or [Path(__file__).parent / "input.txt"]:
        print(f"\n{path}:")
        # fmt: off
        part1 = sum(int(next(d for d in line if d.isdigit()) + next(d for d in line[::-1] if d.isdigit())) for line in Path(path).read_text().rstrip().split("\n"))
        part2 = sum(int(next(d for d in line if d.isdigit()) + next(d for d in line[::-1] if d.isdigit())) for line in Path(path).read_text().rstrip().replace("one", "o1e").replace("two", "t2o").replace("three", "t3e").replace("four", "f4r").replace("five", "f5e").replace("six", "s6x").replace("seven", "s7n").replace("eight", "e8t").replace("nine", "n9e").split("\n"))
        # fmt: on
        print(part1)
        print(part2)
