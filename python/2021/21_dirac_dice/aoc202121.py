"""AoC 21, 2021: Dirac Dice"""

# Standard library imports
import collections
import itertools
import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    return tuple(int(player.split()[-1]) for player in puzzle_input.split("\n"))


def part1(data):
    """Solve part 1"""
    num_rolls, scores = play_dice(data, dice=itertools.cycle(range(1, 101)))
    return num_rolls * min(scores)


def part2(data):
    """Solve part 2"""
    return max(
        play_dirac_dice(
            data,
            dice=[(3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1)],
        )
    )


def play_dice(positions, dice, target=1000):
    """Play a game of dice

    Example with dice cycling 1 -> 2 -> 3 -> 4 -> 5 -> 1 ..., target score 30 and
    both players starting at position 1:

              Start pos   Roll   End pos   Score   Num rolls
    Player 1:       1     1,2,3      7        7         3
    Player 2:       1     4,5,1      1        1         6
    Player 1:       7     2,3,4      6       13         9
    Player 2:       1     5,1,2      9       10        12
    Player 1:       6     3,4,5      8       21        15
    Player 2:       9     1,2,3      5       15        18
    Player 1:       8     4,5,1      8       29        21
    Player 2:       5     2,3,4      4       19        24
    Player 1:       8     5,1,2      6       35        27

    This gives the final result of 27 rolls and score 19 for the losing player:
        27 x 19 = 513

    >>> play_dice((1, 1), dice=itertools.cycle(range(1, 6)), target=30)
    (27, [35, 19])
    """
    positions = list(positions)
    scores = [0, 0]
    num_rolls = 0
    current = 0

    while True:
        num_rolls += 3
        roll = next(dice) + next(dice) + next(dice)
        positions[current] = (positions[current] + roll - 1) % 10 + 1
        scores[current] += positions[current]
        if scores[current] >= target:
            break
        current = 1 - current

    return num_rolls, scores


def play_dirac_dice(positions, dice, target=21):
    """Play a game of universe splitting dirac dice

    Small example with outcomes 1 and 2 and target score 7, starting at 1, 2:

    Round 1:

    (4, 2), (4, 0): 1        Player 1 wins: 1
    (5, 2), (5, 0): 3        Player 2 wins: 0
    (6, 2), (6, 0): 3

    Round 2:

    (4, 5), (4, 5): 1        Player 1 wins: 1
    (4, 6), (4, 6): 3        Player 2 wins: (1 + 3 + 3) x 4 = 28
    (5, 5), (5, 5): 3
    (5, 6), (5, 6): 9
    (6, 5), (6, 5): 3
    (6, 6), (6, 6): 9

    Round 3:

    (1, 5), (6, 5): 3        Player 1 wins: 1 + (1 + 3 + 3 + 9) x 8 + (3 + 9) x 7 = 213
    (1, 6), (6, 6): 9        Player 2 wins: 28

    Round 4:

    (1, 1), (6, 6): 3        Player 1 wins: 213
                             Player 2 wins: 28 + 3 x 7 + 9 x 8 = 121

    Round 5:

                             Player 1 wins: 213 + 3 x 8 = 237
                             Player 2 wins: 121

    >>> play_dirac_dice((1, 2), dice=[(3, 1), (4, 3), (5, 3), (6, 1)], target=7)
    [237, 121]
    """
    universes = {(*positions, 0, 0): 1}
    winners = [0, 0]
    current = 0

    while universes:
        next_universes = collections.defaultdict(int)
        for (pos, other_pos, score, other_score), count in universes.items():
            for roll, splits in dice:
                new_pos = (pos + roll - 1) % 10 + 1
                new_score = score + new_pos
                if new_score >= target:
                    winners[current] += count * splits
                else:
                    state = (other_pos, new_pos, other_score, new_score)
                    next_universes[state] += count * splits

        universes = next_universes
        current = 1 - current

    return winners


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
