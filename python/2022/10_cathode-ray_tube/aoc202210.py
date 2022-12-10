"""AoC 10, 2022: Cathode-Ray Tube."""


# Standard library imports
import contextlib
import itertools
import pathlib
import sys

# Third party imports
from advent_of_code_ocr import convert_6


def parse_data(puzzle_input):
    """Parse input."""
    return list(
        itertools.accumulate(
            (
                int(num)
                for line in puzzle_input.split("\n")
                for num in [0] + line.split()[1:]
            ),
            initial=1,
        )
    )[:-1]


def part1(registers):
    """Solve part 1."""
    return sum(
        [idx * register for idx, register in enumerate(registers, start=1)][19::40]
    )


def part2(registers, return_screen=False):
    """Solve part 2."""
    lit_pixels = "".join(
        "#" if abs(register - (idx % 40)) <= 1 else "."
        for idx, register in enumerate(registers)
    )
    screen = "\n".join(
        lit_pixels[idx : idx + 40] for idx in range(0, len(lit_pixels), 40)
    )

    if "--viz" in sys.argv:
        print(screen.replace("#", "█"))

    if return_screen:
        return screen
    with contextlib.suppress(KeyError, ValueError):
        return convert_6(screen)


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        if path.startswith("-"):
            continue
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().rstrip())
        print("\n".join(str(solution) for solution in solutions))
