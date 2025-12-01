"""AoC 2, 2022: Rock Paper Scissors."""

# Standard library imports
import io
import pathlib
import sys

# Third party imports
import pandas

# rock: 1  paper: 2  scissors: 3
# loss: 0  draw: 1  win: 2
# Use numbers as strings to control type conversion
YOU = {"A": "1", "B": "2", "C": "3"}
ME = {"X": "1", "Y": "2", "Z": "3"}
OUTCOME = {"X": "0", "Y": "1", "Z": "2"}


def parse_data(puzzle_input):
    """Parse input."""
    return (
        pandas.read_csv(
            io.StringIO(puzzle_input),
            sep=" ",
            header=None,
            names=["you", "me"],
        )
        .assign(outcome=lambda df: df["me"])
        .replace({"you": YOU, "me": ME, "outcome": OUTCOME})
        .astype({"you": int, "me": int, "outcome": int})
    )


def part1(rounds):
    """Solve part 1."""
    return (
        rounds.assign(
            outcome=lambda df: (df["me"] - df["you"] + 1) % 3,
            score=lambda df: df["me"] + 3 * df["outcome"],
        )
    )["score"].sum()

def part2(rounds):
    """Solve part 2."""
    return (
        rounds.assign(
            me=lambda df: (df["outcome"] + df["you"] - 2) % 3 + 1,
            score=lambda df: df["me"] + 3 * df["outcome"],
        )
    )["score"].sum()



def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    yield part1(data).item()
    yield part2(data).item()


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
        print("\n".join(str(solution) for solution in solutions))
