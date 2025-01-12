"""AoC 9, 2018: Marble Mania."""

# Standard library imports
import itertools
import pathlib
import sys
from collections import deque
from dataclasses import dataclass, field

# Third party imports
import parse

PATTERN = parse.compile("{players:d} players; last marble is worth {marbles:d} points")


@dataclass
class CircularList:
    """
    A circular list where the first element follows the last one.

    Implemented as a tuple of lists containing the next elements and the
    elements before the pointer, respectively.

    ## Example:

    >>> CircularList(deque([1, 2, 3]))
    CircularList(next=deque([1, 2, 3]), previous=deque([]))
    """

    next: deque[int] = field(default_factory=deque)
    previous: deque[int] = field(default_factory=deque)

    def forward(self):
        """Move to the next element in the list.

        ## Example:

        >>> numbers = CircularList(deque([1, 2, 3]))
        >>> numbers.forward()
        CircularList(next=deque([2, 3]), previous=deque([1]))
        >>> numbers.forward().forward()
        CircularList(next=deque([]), previous=deque([3, 2, 1]))
        >>> numbers.forward()
        CircularList(next=deque([2, 3]), previous=deque([1]))
        """
        if not self.next:
            self.next, self.previous = self.previous, self.next
            self.next.reverse()
        self.previous.appendleft(self.next.popleft())
        return self

    def back(self):
        """Move to the previous element in the list.

        ## Example:

        >>> numbers = CircularList(deque([1, 2, 3]))
        >>> numbers.back()
        CircularList(next=deque([3]), previous=deque([2, 1]))
        >>> numbers.back()
        CircularList(next=deque([2, 3]), previous=deque([1]))
        """
        if not self.previous:
            self.next, self.previous = self.previous, self.next
            self.previous.reverse()
        self.next.appendleft(self.previous.popleft())
        return self

    def insert(self, element):
        """Insert an element into the list.

        ## Example:

        >>> numbers = CircularList(deque([1, 2, 3]))
        >>> numbers.insert(4)
        CircularList(next=deque([4, 1, 2, 3]), previous=deque([]))

        >>> numbers = CircularList(deque([1, 2, 3]))
        >>> numbers.forward().forward().insert(4)
        CircularList(next=deque([4, 3]), previous=deque([2, 1]))
        """
        self.next.appendleft(element)
        return self

    def pop(self):
        """Pop the current element from the list.

        ## Example:

        >>> numbers = CircularList(deque([1, 2, 3]))
        >>> numbers.pop()
        1
        >>> numbers
        CircularList(next=deque([2, 3]), previous=deque([]))

        >>> numbers = CircularList(deque([1, 2, 3]))
        >>> numbers.forward().forward().pop()
        3
        >>> numbers
        CircularList(next=deque([]), previous=deque([2, 1]))

        >>> numbers = CircularList(deque([1, 2, 3]))
        >>> numbers.back().pop()
        3
        >>> numbers
        CircularList(next=deque([]), previous=deque([2, 1]))
        """
        return self.next.popleft() if self.next else self.previous.popleft()


def parse_data(puzzle_input):
    """Parse input."""
    match = PATTERN.parse(puzzle_input)
    return match["players"], match["marbles"]


def part1(data):
    """Solve part 1."""
    players, marbles = data
    return max(play(players, marbles).values())


def part2(data):
    """Solve part 2."""
    players, marbles = data
    return max(play(players, 100 * marbles).values())


def play(num_players, num_marbles):
    """Play a game with the given number of players and marbles."""
    marbles = CircularList(deque([0]))
    scores = {player: 0 for player in range(1, num_players + 1)}
    for player, marble in zip(
        itertools.cycle(range(1, num_players + 1)), range(1, num_marbles + 1)
    ):
        if marble % 23 == 0:
            (marbles.back().back().back().back().back().back().back())
            scores[player] += marble + marbles.pop()
        else:
            marbles.forward().forward().insert(marble)
    return scores


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
