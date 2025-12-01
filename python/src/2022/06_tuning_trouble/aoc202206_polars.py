"""AoC 6, 2022: Tuning Trouble."""

# Standard library imports
import io
import pathlib
import sys
from itertools import zip_longest

# Third party imports
import polars as pl

pl.Config.set_tbl_rows(100)


def parse_data(puzzle_input):
    """Parse input."""
    return pl.read_csv(
        io.StringIO("\n".join(puzzle_input)), has_header=False, new_columns=["char"]
    )


def part1(sequence):
    """Solve part 1."""
    return find_marker(sequence, 4)


def part2(sequence):
    """Solve part 2."""
    return find_marker(sequence, 14)


def find_marker(sequence, length):
    """Find the first marker of the given length."""
    return (
        sequence.with_row_count("char_num", offset=1)
        .groupby("char")
        .agg(pl.col("char_num").list())
        .with_columns(
            pl.col("char_num")
            .apply(
                lambda nums: [
                    num
                    for prev, num, next in zip_longest(nums, nums[1:], nums[2:])
                    if num is not None and (next is None or next - prev >= length)
                ]
            )
            .alias("valid")
        )
        .explode("valid")
        .drop_nulls("valid")
        .sort("valid")
        # .groupby_rolling("char_num", period=f"{length}i")
        # .agg([pl.col("char"), pl.count(), pl.list("char_num").alias("asda")])
        # .filter(pl.col("count") == length)
        # .head(1)
        # .select("char_num")
    )


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    yield part1(data)  # .to_numpy().item()
    yield part2(data)  # .to_numpy().item()


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().rstrip())
        print("\n".join(str(solution) for solution in solutions))
