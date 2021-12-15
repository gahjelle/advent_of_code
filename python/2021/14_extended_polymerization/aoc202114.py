"""AoC 14, 2021: Extended Polymerization"""

# Standard library imports
import functools
import pathlib
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass


@dataclass
class Polymer:
    first: str
    pairs: dict[str, int]
    rules: dict[str, list[str]]

    @classmethod
    def from_str(cls, text):
        """Create a polymer from a string

        >>> Polymer.from_str(
        ...     "GAH\\n\\nAG -> H\\nAH -> G\\nGA -> H\\nGH -> A\\nHA -> G\\nHG -> A"
        ... )
        Polymer(first='G',
                pairs={'GA': 1, 'AH': 1},
                rules={'AG': ['AH', 'HG'],
                       'AH': ['AG', 'GH'],
                       'GA': ['GH', 'HA'],
                       'GH': ['GA', 'AH'],
                       'HA': ['HG', 'GA'],
                       'HG': ['HA', 'AG']})
        """
        pairs, _, *rules = text.split("\n")
        return cls(
            first=pairs[0],
            pairs=dict(Counter("".join(pair) for pair in zip(pairs[:-1], pairs[1:]))),
            rules=dict(cls.parse_rule(rule) for rule in rules),
        )

    @staticmethod
    def parse_rule(rule):
        """Parse one rule

        >>> Polymer.parse_rule("CH -> B")
        ('CH', ['CB', 'BH'])
        """
        pair, _, insert = rule.partition(" -> ")
        return (pair, [pair[0] + insert, insert + pair[1]])

    def step(self):
        """Do one step of polymer insertion

        >>> Polymer.from_str(
        ...     "GAH\\n\\nAG -> H\\nAH -> G\\nGA -> H\\nGH -> A\\nHA -> G\\nHG -> A"
        ... ).step().step().pairs
        {'GA': 3, 'AH': 3, 'HG': 2}
        """
        cls = self.__class__
        inserted = [
            (pair, count)
            for parent, count in self.pairs.items()
            for pair in self.rules[parent]
        ]
        pairs = defaultdict(int)
        for pair, count in inserted:
            pairs[pair] += count

        return cls(self.first, dict(pairs), self.rules)

    def score(self):
        """Score current polymer based on least and most common elements

        >>> Polymer.from_str(
        ...     "GAH\\n\\nAG -> H\\nAH -> G\\nGA -> H\\nGH -> A\\nHA -> G\\nHG -> A"
        ... ).step().score()
        1
        """
        counts = defaultdict(int, **{self.first: 1})
        for pair, count in self.pairs.items():
            counts[pair[1]] += count

        min_count, max_count = min(counts.values()), max(counts.values())
        return max_count - min_count


def parse(puzzle_input):
    """Parse input"""
    return Polymer.from_str(puzzle_input)


def part1(data):
    """Solve part 1"""
    for _ in range(10):
        data = data.step()

    return data.score()


def part2(data):
    """Solve part 2"""
    for _ in range(40):
        data = data.step()

    return data.score()


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
