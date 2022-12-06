"""AoC 6, 2022: Tuning Trouble."""

# Standard library imports
import pathlib
import sys

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        # fmt: off
        part1 = next(idx for idx, rl in enumerate((len(set(m)) for m in zip(*(pathlib.Path(path).read_text()[n:] for n in range(4)))), start=4) if rl == 4)
        part2 = next(idx for idx, rl in enumerate((len(set(m)) for m in zip(*(pathlib.Path(path).read_text()[n:] for n in range(14)))), start=14) if rl == 14)
        # fmt: on
        print(part1)
        print(part2)
