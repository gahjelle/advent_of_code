"""AoC 21, 2024: Keypad Conundrum."""

# Standard library imports
import collections
import itertools
import pathlib
import sys

NUMBER_PAD = "789\n456\n123\n 0A"
ARROW_PAD = " ^A\n<v>"
DIRECTIONS = {(-1, 0): "^", (0, 1): ">", (1, 0): "v", (0, -1): "<"}
ARROW_CACHE = {}


def parse_data(puzzle_input):
    """Parse input."""
    return (
        [code.rstrip("A") for code in puzzle_input.split("\n")],
        parse_pad(NUMBER_PAD),
        parse_pad(ARROW_PAD),
    )


def parse_pad(string):
    """Parse the grid of a pad into moves"""
    grid = {
        (row, col): char
        for row, line in enumerate(string.split("\n"))
        for col, char in enumerate(line)
        if char != " "
    }
    keys = set(grid.values())
    return {
        (start, target): find_moves(grid, start, target)
        for start, target in itertools.product(keys, keys)
    }


def part1(data):
    """Solve part 1."""
    codes, number_pad, arrow_pad = data
    return sum(
        int(code) * type_code(code, number_pad, arrow_pad, num_arrow_pads=2)
        for code in codes
    )


def part2(data):
    """Solve part 2."""
    codes, number_pad, arrow_pad = data
    return sum(
        int(code) * type_code(code, number_pad, arrow_pad, num_arrow_pads=25)
        for code in codes
    )


def type_code(code, number_pad, arrow_pad, num_arrow_pads):
    """Find number of pushes necessary to type one code"""
    sequences = push_pad(number_pad, code)
    return min(
        push_arrows(arrow_pad, sequence, num_arrow_pads) for sequence in sequences
    )


def push_arrows(pad, strings, num_times):
    """Push the arrows on an arrow pad num_times times"""
    if num_times == 0:
        return len(strings)

    for string in strings.split("A"):
        if (string, num_times) in ARROW_CACHE:
            continue

        sequences = push_pad(pad, string)
        ARROW_CACHE[string, num_times] = min(
            push_arrows(pad, sequence, num_times - 1) for sequence in sequences
        )

    return sum(ARROW_CACHE[string, num_times] for string in strings[:-1].split("A"))


def push_pad(pad, string):
    """Find the possible shortest sequences of moves for typing a string"""
    sequences = [""]
    for prev_code, code in zip(f"A{string}", f"{string}A"):
        sequences = [
            sequence + move for sequence in sequences for move in pad[prev_code, code]
        ]
    return sequences


def find_moves(pad, start, target):
    """Find the necessary moves for pushing a pad directly

    Find all shortest sequences of moves.
    """
    start_pos = next(pos for pos, char in pad.items() if char == start)
    queue = collections.deque([(start_pos, "")])
    sequences = []
    max_len = None
    best = {}
    while queue:
        (row, col), moves = queue.popleft()
        if max_len and len(moves) > max_len:
            continue
        if pad[row, col] == target:
            moves += "A"
            max_len = len(moves)
            sequences.append(moves)
            continue
        if len(moves.strip("A")) > best.get((row, col), 999):
            continue
        best[row, col] = len(moves.strip("A"))

        for (drow, dcol), move in DIRECTIONS.items():
            new_pos = (row + drow, col + dcol)
            if new_pos in pad:
                queue.append((new_pos, moves + move))
    return sequences


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
