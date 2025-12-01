"""AoC 2, 2022: Rock Paper Scissors."""

# Standard library imports
import pathlib
import sys

OTHER = {"A": "rock", "B": "paper", "C": "scissors"}
SELF = {"X": "rock", "Y": "paper", "Z": "scissors"}
LOSE_DRAW_WIN = {"X": "lose", "Y": "draw", "Z": "win"}
LOSE_AGAINST = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
POINTS = {"rock": 1, "paper": 2, "scissors": 3}


def parse_data(puzzle_input):
    """Parse input."""
    return [
        (OTHER[line[0]], SELF[line[2]], LOSE_DRAW_WIN[line[2]])
        for line in puzzle_input.split("\n")
    ]


def part1(rounds):
    """Solve part 1."""
    return sum(score(self, other) for other, self, _ in rounds)


def part2(rounds):
    """Solve part 2."""
    return sum(score(choose(strategy, other), other) for other, _, strategy in rounds)


def score(self, other):
    """Score one round.

    The score for a single round is the score for the shape you selected (1 for
    Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the
    round (0 if you lost, 3 if the round was a draw, and 6 if you won).

    ## Examples:

    >>> score("rock", "scissors")
    7
    >>> score("paper", "paper")
    5
    """
    return POINTS[self] + (
        6 if other == LOSE_AGAINST[self] else 3 if other == self else 0
    )


def choose(strategy, other):
    """Choose a move based on the strategy.

    ## Examples:

    >>> choose("win", "paper")
    'scissors'
    >>> choose("draw", "rock")
    'rock'
    """
    match strategy:
        case "lose":
            return LOSE_AGAINST[other]
        case "draw":
            return other
        case "win":
            return next(win for win, lose in LOSE_AGAINST.items() if other == lose)


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
