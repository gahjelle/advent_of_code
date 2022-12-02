"""AoC 2, 2022: Rock Paper Scissors."""

# Standard library imports
import pathlib
import sys

GAME_1 = {
    "A X": 4,  # rock vs rock         -> Draw
    "B X": 1,  # paper vs rock        -> Lose
    "C X": 7,  # scissors vs rock     -> Win
    "A Y": 8,  # rock vs paper        -> Win
    "B Y": 5,  # paper vs paper       -> Draw
    "C Y": 2,  # scissors vs paper    -> Lose
    "A Z": 3,  # rock vs scissors     -> Lose
    "B Z": 9,  # paper vs scissors    -> Win
    "C Z": 6,  # scissors vs scissors -> Draw
}
GAME_2 = {
    "A X": 3,  # Lose against rock     -> scissors
    "B X": 1,  # Lose against paper    -> rock
    "C X": 2,  # Lose against scissors -> paper
    "A Y": 4,  # Draw against rock     -> rock
    "B Y": 5,  # Draw against paper    -> paper
    "C Y": 6,  # Draw against scissors -> scissors
    "A Z": 8,  # Win against rock      -> paper
    "B Z": 9,  # Win against paper     -> scissors
    "C Z": 7,  # Win against scissors  -> rock
}


def parse_data(puzzle_input):
    """Parse input."""
    return puzzle_input.split("\n")


def part1(rounds):
    """Solve part 1."""
    return sum(GAME_1[round] for round in rounds)


def part2(rounds):
    """Solve part 2."""
    return sum(GAME_2[round] for round in rounds)


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
