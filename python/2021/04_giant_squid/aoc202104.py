"""AoC 4, 2021: Giant Squid."""

# Standard library imports
import math
import pathlib
import sys
from collections import UserList, deque
from dataclasses import dataclass


@dataclass
class BingoBoard:
    """A bingo board including a list of moves."""

    moves: deque[int]
    board: dict[int, tuple[int, int] | None]
    last_move: int | None = None

    @classmethod
    def from_str(cls, moves, board_str):
        """Create a board from a string."""
        board = {}
        for row, line in enumerate(board_str.split("\n")):
            for col, number in enumerate(line.split()):
                board[int(number)] = (row, col)

        return cls(deque(moves), board)

    def check_bingo(self):
        """Check if a board has scored a bingo.

        >>> board = BingoBoard(deque(), {0: (0, 0), 1: None, 2: None, 3: (1,1)})
        >>> board.check_bingo()
        False

        >>> board = BingoBoard(deque(), {0: None, 1: None, 2: (1, 0), 3: (1,1)})
        >>> board.check_bingo()
        True
        """
        num_lines = round(math.sqrt(len(self.board)))
        rows = {pos[0] for pos in self.board.values() if pos is not None}
        cols = {pos[1] for pos in self.board.values() if pos is not None}

        return len(rows) != num_lines or len(cols) != num_lines

    def make_moves(self):
        """Make moves until bingo, will not make additional moves if called a
        second time.

        >>> board = BingoBoard(deque([0, 3, 1, 2]), {0: (0, 0), 1: (0, 1), 2: (1, 0), 3: (1,1)})
        >>> board.make_moves()
        >>> board
        BingoBoard(moves=deque([2]), board={0: None, 1: None, 2: (1, 0), 3: None}, last_move=1)
        """
        while not self.check_bingo():
            move = self.last_move = self.moves.popleft()
            if move in self.board:
                self.board[move] = None

    @property
    def score(self):
        """Score a board.

        >>> board = BingoBoard(moves=deque([2]), board={0: None, 1: None, 2: (1, 0), 3: None}, last_move=1)
        >>> board.score
        2
        """
        board_sum = sum(number for number, pos in self.board.items() if pos is not None)
        return self.last_move * board_sum


class BingoBoards(UserList):
    """List of BingoBoard objects."""

    def play_bingo(self):
        """Play bingo on all boards."""
        for board in self.data:
            board.make_moves()

    @property
    def best_board(self):
        """Find the board that wins first."""
        return max(self.data, key=lambda board: len(board.moves))

    @property
    def worst_board(self):
        """Find the board that wins last."""
        return min(self.data, key=lambda board: len(board.moves))


def parse_data(puzzle_input):
    """Parse input."""
    moves_str, *board_strs = puzzle_input.split("\n\n")
    moves = [int(move) for move in moves_str.split(",")]

    return BingoBoards(
        BingoBoard.from_str(moves, board_str) for board_str in board_strs
    )


def part1(data):
    """Solve part 1."""
    data.play_bingo()
    return data.best_board.score


def part2(data):
    """Solve part 2."""
    data.play_bingo()
    return data.worst_board.score


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
