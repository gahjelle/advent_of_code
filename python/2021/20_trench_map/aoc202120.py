"""AoC 20, 2021: Trench Map"""

# Standard library imports
import pathlib
import sys
from dataclasses import dataclass


@dataclass
class Image:
    enhancer: str
    grid: set[tuple[int, int]]
    infinity_light: bool = False

    def __post_init__(self):
        """Calculate dimensions of the image

        >>> Image.from_str("#\\n\\n#..\\n##.\\n.#.").bbox
        (0, 0, 2, 1)
        """
        xs = {x for _, x in self.grid}
        ys = {y for y, _ in self.grid}
        self.bbox = (
            min(ys, default=0),
            min(xs, default=0),
            max(ys, default=0),
            max(xs, default=0),
        )

    @classmethod
    def from_str(cls, text):
        """Create an image from a string"""
        enhancer, grid, *_ = text.split("\n\n")
        return cls(
            enhancer,
            {
                (row, col)
                for row, line in enumerate(grid.split("\n"))
                for col, char in enumerate(line)
                if char == "#"
            },
        )

    @property
    def rows(self):
        """The rows of the image, including one buffer row on each side

        >>> Image.from_str("#\\n\\n#..\\n##.\\n.#.").rows
        range(-1, 4)
        """
        min_y, _, max_y, _ = self.bbox
        return range(min_y - 1, max_y + 2)

    @property
    def cols(self):
        """The columns of the image, including one buffer column on each side

        >>> list(Image.from_str("#\\n\\n#..\\n##.\\n.#.").cols)
        [-1, 0, 1, 2]
        """
        _, min_x, _, max_x = self.bbox
        return range(min_x - 1, max_x + 2)

    def is_enhanced(self, row, col):
        """Find the enhanced pixel at the given row and column"""
        bin = "".join("1" if nb else "0" for nb in self.neighbors(row, col))
        return self.enhancer[int(bin, base=2)] == "#"

    def neighbors(self, row, col):
        """The neighbors of a pixel, in enhancement order

        Handle infinite grid by simulating a light for neighbors
        outside the grid if infinity is lit up.
        """
        min_y, min_x, max_y, max_x = self.bbox
        neighbor_coords = [
            (row - 1, col - 1),
            (row - 1, col),
            (row - 1, col + 1),
            (row, col - 1),
            (row, col),
            (row, col + 1),
            (row + 1, col - 1),
            (row + 1, col),
            (row + 1, col + 1),
        ]

        for y, x in neighbor_coords:
            if not self.infinity_light or (min_y <= y <= max_y and min_x <= x <= max_x):
                yield (y, x) in self.grid
            else:
                yield True

    def enhance(self):
        """Run one step of the enhancement algorithm"""
        new_grid = {
            (row, col)
            for row in self.rows
            for col in self.cols
            if self.is_enhanced(row, col)
        }

        # Handle infinite pixels
        turn_on_infinity = not self.infinity_light and self.enhancer[0] == "#"
        not_turn_off_infinity = self.infinity_light and self.enhancer[-1] == "#"
        infinity_light = turn_on_infinity or not_turn_off_infinity

        # Create new grid
        cls = self.__class__
        return cls(enhancer=self.enhancer, grid=new_grid, infinity_light=infinity_light)

    def __len__(self):
        """Number of lit pixels in the image

        >>> len(Image.from_str("#\\n\\n#..\\n##.\\n.#."))
        4
        """
        return len(self.grid)


def parse_data(puzzle_input):
    """Parse input"""
    return Image.from_str(puzzle_input)


def part1(data):
    """Solve part 1"""
    return len(data.enhance().enhance())


def part2(data):
    """Solve part 2"""
    for _ in range(50):
        data = data.enhance()
    return len(data)


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
