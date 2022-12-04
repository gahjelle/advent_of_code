"""AoC 4, 2022: Camp Cleanup."""

# Standard library imports
import pathlib
import sys

# Third party imports
import polars as pl


def parse_data(puzzle_input):
    """Parse input."""
    return (
        pl.read_csv(puzzle_input, has_header=False, new_columns=["first", "second"])
        .with_row_count("id")
        .with_columns(
            [
                pl.col("first").str.split("-").alias("low_high_1"),
                pl.col("second").str.split("-").alias("low_high_2"),
            ]
        )
        .select(
            [
                pl.col("low_high_1").arr.get(0).cast(int).alias("low_1"),
                pl.col("low_high_1").arr.get(1).cast(int).alias("high_1"),
                pl.col("low_high_2").arr.get(0).cast(int).alias("low_2"),
                pl.col("low_high_2").arr.get(1).cast(int).alias("high_2"),
            ]
        )
    )


def part1(pairs):
    """Solve part 1."""
    return (
        pairs.filter(
            (pl.col("low_1") <= pl.col("low_2"))
            & (pl.col("high_1") >= pl.col("high_2"))
            | (pl.col("low_2") <= pl.col("low_1"))
            & (pl.col("high_2") >= pl.col("high_1"))
        )
        .with_columns(pl.lit(1).alias("count"))
        .select("count")
        .sum()
    )


def part2(pairs):
    """Solve part 2."""
    return (
        pairs.filter(
            (pl.col("low_1") <= pl.col("high_2"))
            & (pl.col("low_2") <= pl.col("high_1"))
        )
        .with_columns(pl.lit(1).alias("count"))
        .select("count")
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
        solutions = solve(puzzle_input=pathlib.Path(path))
        print("\n".join(str(solution) for solution in solutions))
