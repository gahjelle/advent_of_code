"""AoC 2, 2022: Rock Paper Scissors."""

# Standard library imports
import io
import pathlib
import sys

# Third party imports
import polars as pl

# rock: 1  paper: 2  scissors: 3
# loss: 0  draw: 1  win: 2
YOU = {"A": 1, "B": 2, "C": 3}
ME = {"X": 1, "Y": 2, "Z": 3}
OUTCOME = {"X": 0, "Y": 1, "Z": 2}


def parse_data(puzzle_input):
    """Parse input."""
    return pl.read_csv(
        io.StringIO(puzzle_input),
        separator=" ",
        has_header=False,
        new_columns=["you", "me"],
    ).with_columns(
        [
            pl.col("you").replace_strict(YOU, return_dtype=pl.Int32),
            pl.col("me").replace_strict(ME, return_dtype=pl.Int32),
            pl.col("me")
            .replace_strict(OUTCOME, return_dtype=pl.Int32)
            .alias("outcome"),
        ]
    )


def part1(rounds):
    """Solve part 1."""
    outcome = (pl.col("me") - pl.col("you") + 1).mod(3)
    score = pl.col("me") + 3 * outcome
    return rounds.select(score.sum())


def part2(rounds):
    """Solve part 2."""
    me = (pl.col("outcome") + pl.col("you") - 2).mod(3) + 1
    score = me + 3 * pl.col("outcome")
    return rounds.select(score.sum())


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
