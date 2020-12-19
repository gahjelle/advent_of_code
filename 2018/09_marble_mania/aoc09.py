"""Marble Mania

Advent of Code 2018, day 9
Solution by Geir Arne Hjelle, 2019-12-16
"""
# Standard library imports
import pathlib
import sys
from dataclasses import dataclass, field

# Third party imports
import parse

debug = print if "--debug" in sys.argv else lambda *_: None
INPUT = parse.compile(
    "{num_players:d} players; last marble is worth {num_rounds:d} points"
)


@dataclass
class Node:
    value: int
    before: "Node" = field(default=None, repr=False)
    after: "Node" = field(default=None, repr=False)


@dataclass
class LinkedList:
    current: Node

    def __post_init__(self):
        self.current.before = self.current
        self.current.after = self.current

    def clockwise(self, num=1):
        for _ in range(num):
            self.current = self.current.after

    def counterclockwise(self, num=1):
        for _ in range(num + 1):
            self.current = self.current.before

    def insert_after(self, value):
        node = Node(value, before=self.current, after=self.current.after)
        self.current.after.before = node
        self.current.after = node

    def remove_current(self):
        current = self.current
        self.current.before.after = current.after
        self.current.after.before = current.before
        self.current = current.before
        return current.value

    def draw(self):
        current = self.current.after
        while current != self.current:
            print(current.value, end=" ")
            current = current.after
        print(current.value)


def parse_input(line):
    result = INPUT.parse(line).named
    return result["num_players"], result["num_rounds"]


def play_marbles(num_players, num_rounds, scorer=23):
    scores = {k: 0 for k in range(num_players)}
    marbles = LinkedList(Node(0))

    for marble in range(1, num_rounds + 1):
        marbles.clockwise(2)
        if marble % scorer:
            marbles.insert_after(marble)
        else:
            marbles.counterclockwise(7)
            player = marble % num_players
            scores[player] += marble + marbles.remove_current()

    return scores


def main(args):
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        print(f"\n{file_path}:")
        text = file_path.read_text()

        for line in text.strip().split("\n"):
            num_players, num_rounds = parse_input(line)

            # Part 1
            scores = play_marbles(num_players, num_rounds)
            print(f"Highscore in {num_rounds} rounds is {max(scores.values())}")

            # Part 2
            scores = play_marbles(num_players, 100 * num_rounds)
            print(f"Highscore in {100 * num_rounds} rounds is {max(scores.values())}")


if __name__ == "__main__":
    main(sys.argv[1:])
