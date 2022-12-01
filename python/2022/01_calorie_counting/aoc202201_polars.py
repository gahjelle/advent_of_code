"""AoC 1, 2022: Calorie Counting."""

# Standard library imports
import pathlib
import sys

# Third party imports
import polars as pl


def parse_data(puzzle_input):
    """Parse input."""
    return pl.DataFrame(enumerate_elfs(puzzle_input), columns=("elf", "calorie_count"))


def enumerate_elfs(puzzle_input):
    """Enumerate elfs and their calorie counts.

    ## Example:

    >>> list(enumerate_elfs("3\\n1\\n\\n4\\n\\n1\\n5\\n9"))
    [(1, 3), (1, 1), (2, 4), (3, 1), (3, 5), (3, 9)]
    """
    elf = 1
    for line in puzzle_input.split("\n"):
        if line:
            yield elf, int(line)
        else:
            elf += 1


def part1(calories):
    """Solve part 1."""
    return (
        calories.groupby("elf")
        .agg(pl.col("calorie_count").sum())
        .select("calorie_count")
        .max()
    )


def part2(calories):
    """Solve part 2."""
    return (
        calories.groupby("elf")
        .agg(pl.col("calorie_count").sum())
        .sort(by="calorie_count", reverse=True)
        .head(3)
        .select("calorie_count")
        .sum()
    )


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    yield part1(data).to_numpy().item()
    yield part2(data).to_numpy().item()


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
