"""AoC 5, 2021: Hydrothermal Venture"""

# Standard library imports
import collections
import pathlib
import sys
from dataclasses import dataclass


@dataclass
class Line:
    kind: str
    x1: int
    y1: int
    x2: int
    y2: int

    @classmethod
    def from_str(cls, string):
        """Create a Line from a string

        >>> Line.from_str("0,0 -> 0,2")
        Line(kind='vertical', x1=0, y1=0, x2=0, y2=2)

        >>> Line.from_str("2,2 -> 0,2")
        Line(kind='horisontal', x1=0, y1=2, x2=2, y2=2)

        >>> Line.from_str("2,0 -> 0,2")
        Line(kind='diagonal', x1=0, y1=2, x2=2, y2=0)
        """
        match [int(xy) for pt in string.split(" -> ") for xy in pt.split(",")]:
            case [x1, y1, x2, y2] if x1 == x2:
                return cls("vertical", x1=x1, y1=min(y1, y2), x2=x2, y2=max(y1, y2))
            case [x1, y1, x2, y2] if y1 == y2:
                return cls("horisontal", x1=min(x1, x2), y1=y1, x2=max(x1, x2), y2=y2)
            case [x1, y1, x2, y2] if x1 < x2:
                return cls("diagonal", x1=x1, y1=y1, x2=x2, y2=y2)
            case [x1, y1, x2, y2] if x1 > x2:
                return cls("diagonal", x1=x2, y1=y2, x2=x1, y2=y1)

    def points(self):
        """List points in line

        >>> Line.from_str("0,0 -> 0,2").points()
        [(0, 0), (0, 1), (0, 2)]

        >>> Line.from_str("2,2 -> 0,2").points()
        [(0, 2), (1, 2), (2, 2)]

        >>> Line.from_str("2,0 -> 0,2").points()
        [(0, 2), (1, 1), (2, 0)]
        """
        match self:
            case Line("vertical", x, y1, _, y2):
                return [(x, y) for y in range(y1, y2 + 1)]
            case Line("horisontal", x1, y, x2, _):
                return [(x, y) for x in range(x1, x2 + 1)]
            case Line("diagonal", x1, y1, x2, y2):
                xs = range(x1, x2 + 1)
                ys = range(y1, y2 + 1) if y1 < y2 else range(y1, y2 - 2, -1)
                return [(x, y) for x, y in zip(xs, ys)]


def parse_data(puzzle_input):
    """Parse input"""
    return [Line.from_str(line) for line in puzzle_input.split("\n")]


def part1(data):
    """Solve part 1"""
    return count_overlaps(line for line in data if line.kind != "diagonal")


def part2(data):
    """Solve part 2"""
    return count_overlaps(data)


def count_overlaps(lines):
    """Count overlaps created by lines"""
    points = collections.Counter(pt for line in lines for pt in line.points())
    return sum(overlap >= 2 for overlap in points.values())


def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
