"""AoC 21, 2017: Fractal Art."""

# Standard library imports
import collections
import math
import pathlib
import sys

# Third party imports
import numpy as np

FINGERPRINTS = {
    2: [
        [1, 2, 4, 8],
        [2, 8, 1, 4],
        [8, 4, 2, 1],
        [4, 1, 8, 2],
        [2, 1, 8, 4],
        [1, 4, 2, 8],
        [4, 8, 1, 2],
        [8, 2, 4, 1],
    ],
    3: [
        [1, 2, 4, 8, 16, 32, 64, 128, 256],
        [4, 32, 256, 2, 16, 128, 1, 8, 64],
        [256, 128, 64, 32, 16, 8, 4, 2, 1],
        [64, 8, 1, 128, 16, 2, 256, 32, 4],
        [4, 2, 1, 32, 16, 8, 256, 128, 64],
        [1, 8, 64, 2, 16, 128, 4, 32, 256],
        [64, 128, 256, 8, 16, 32, 1, 2, 4],
        [256, 32, 4, 128, 16, 2, 64, 8, 1],
    ],
}


def parse_data(puzzle_input):
    """Parse input."""
    return [
        (parse_pattern(pattern), parse_pattern(replace))
        for pattern, replace in [ln.split(" => ") for ln in puzzle_input.split("\n")]
    ]


def parse_pattern(pattern):
    """Parse one pattern into a NumPy array.

    ## Examples:

    >>> parse_pattern("#./.#")
    array([[1, 0],
           [0, 1]])
    >>> parse_pattern("#..#/..../..../#..#")
    array([[1, 0, 0, 1],
           [0, 0, 0, 0],
           [0, 0, 0, 0],
           [1, 0, 0, 1]])
    """
    chars = pattern.replace("/", "")
    dim = math.isqrt(len(chars))
    return np.array([1 if ch == "#" else 0 for ch in chars]).reshape(dim, dim)


def part1(rule_list, num_iterations=5):
    """Solve part 1."""
    board = np.array([[0, 1, 0], [0, 0, 1], [1, 1, 1]])
    rules = {fingerprint(pattern): replace for pattern, replace in rule_list}
    return evolve_board(rules, board, num_iterations).sum()


def part2(rule_list, num_iterations=18):
    """Solve part 2.

    A 3x3 pattern evolves from 3x3 -> 4x4 -> 6x6 -> 9x9 in three steps. The 9x9
    board consists of nine 3x3 boards. Pre-calculate all 3x3 three-step
    patterns. Then, eighteen iterations are quickly calculated as six iterations
    of three-step patterns.
    """
    nine_x_nine = [
        (slice(0, 3), slice(0, 3)),
        (slice(0, 3), slice(3, 6)),
        (slice(0, 3), slice(6, 9)),
        (slice(3, 6), slice(0, 3)),
        (slice(3, 6), slice(3, 6)),
        (slice(3, 6), slice(6, 9)),
        (slice(6, 9), slice(0, 3)),
        (slice(6, 9), slice(3, 6)),
        (slice(6, 9), slice(6, 9)),
    ]
    rules = {fingerprint(pattern): replace for pattern, replace in rule_list}
    lights = {fingerprint(pattern): pattern.sum() for pattern, _ in rule_list}

    # Precalculate all three-step patterns
    steps = {}
    for board, _ in rule_list:
        if len(board) != 3:
            continue
        new_board = evolve_board(rules, board, num_iterations=3)
        steps[fingerprint(board)] = collections.Counter(
            fingerprint(new_board[pos]) for pos in nine_x_nine
        )

    # Iterate in three-steps
    boards = collections.Counter(
        [fingerprint(np.array([[0, 1, 0], [0, 0, 1], [1, 1, 1]]))]
    )
    for _ in range(num_iterations // 3):
        new_boards = collections.Counter()
        for fp, count in boards.items():
            new_boards.update(
                {new_fp: count * new_count for new_fp, new_count in steps[fp].items()}
            )
        boards = new_boards

    return sum(lights[fp] * count for fp, count in boards.items())


def fingerprint(pattern):
    """Create a fingerprint that is independent of rotations and flips.

    2x2 board rotations and flips:

     1 2 | 2 8 | 8 4 | 4 1 | 2 1 | 1 4 | 4 8 | 8 2
     4 8 | 1 4 | 2 1 | 8 2 | 8 4 | 2 8 | 1 2 | 4 1

    3x3 board rotations and flips:

      1   2   4  |   4  32 256  | 256 128  64  |  64   8   1
      8  16  32  |   2  16 128  |  32  16   8  | 128  16   2
     64 128 256  |   1   8  64  |   4   2   1  | 256  32   4

      4   2   1  |   1   8  64  |  64 128 256  | 256  32   4
     32  16   8  |   2  16 128  |   8  16  32  | 128  16   2
    256 128  64  |   4  32 256  |   1   2   4  |  64   8   1

    ## Examples:

    >>> fingerprint(np.array([[1, 0], [0, 0]]))
    (2, 1, 1, 2, 2, 4, 4, 8, 8)
    >>> fingerprint(np.array([[1, 1], [0, 0]]))
    (2, 3, 3, 5, 5, 10, 10, 12, 12)
    >>> fingerprint(np.array([[1, 0], [0, 1]]))
    (2, 6, 6, 6, 6, 9, 9, 9, 9)

    >>> fingerprint(np.array([[0, 1, 0], [0, 0, 0], [0, 0, 0]]))
    (3, 2, 2, 8, 8, 32, 32, 128, 128)
    >>> fingerprint(np.array([[0, 1, 0], [0, 0, 1], [1, 1, 1]]))
    (3, 107, 143, 167, 233, 302, 428, 458, 482)
    >>> fingerprint(np.array([[0, 1, 0], [1, 0, 0], [1, 1, 1]]))
    (3, 107, 143, 167, 233, 302, 428, 458, 482)
    >>> fingerprint(np.array([[1, 0, 0], [1, 0, 1], [1, 1, 0]]))
    (3, 107, 143, 167, 233, 302, 428, 458, 482)
    >>> fingerprint(np.array([[1, 1, 1], [1, 1, 0], [0, 0, 0]]))
    (3, 31, 55, 91, 217, 310, 436, 472, 496)
    """
    return (
        len(pattern),
        *sorted(
            sum(factor * pixel for factor, pixel in zip(mask, pattern.flatten()))
            for mask in FINGERPRINTS[len(pattern)]
        ),
    )


def evolve_board(rules, board, num_iterations):
    """Evolve the board the given number of iterations."""
    for _ in range(num_iterations):
        dim = len(board)
        grid = 2 if dim % 2 == 0 else 3
        shape = dim // grid

        board = np.vstack(
            [
                np.hstack(
                    [
                        rules[
                            fingerprint(
                                board[
                                    row * grid : (row + 1) * grid,
                                    col * grid : (col + 1) * grid,
                                ]
                            )
                        ]
                        for col in range(shape)
                    ]
                )
                for row in range(shape)
            ]
        )
    return board


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().rstrip())
        print("\n".join(str(solution) for solution in solutions))
