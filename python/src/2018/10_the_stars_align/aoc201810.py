"""AoC 10, 2018: The Stars Align."""

# Standard library imports
import pathlib
import sys

# Third party imports
import parse

POINT_PATTERN = parse.compile("position=<{x:>d},{y:>d}> velocity=<{vx:>d},{vy:>d}>")
ALPHABET = {
    "########\n...#....\n...#....\n...#....\n########": "H",
    "#......#\n########\n#......#": "I",
    ".########.\n#........#\n#........#\n#........#\n#........#\n.#......#.": "C",
    "##########\n#...#....#\n#...#....#\n#...#....#\n#...#....#\n#........#": "E",
    "##########\n....##....\n...#..#...\n..#....#..\n.#......#.\n#........#": "K",
    "##########\n#...#.....\n#...#.....\n#...#.....\n#...#.....\n.###......": "P",
    "##########\n#...#.....\n#...#.....\n#...##....\n#...#.##..\n.###....##": "R",
    "##......##\n..##..##..\n....##....\n....##....\n..##..##..\n##......##": "X",
    "#......###\n#.....#..#\n#....#...#\n#...#....#\n#..#.....#\n###......#": "Z",
}


def parse_data(puzzle_input):
    """Parse input."""
    return [parse_point(line) for line in puzzle_input.split("\n")]


def parse_point(line):
    """Parse one point."""
    point = POINT_PATTERN.parse(line)
    return ((point["x"], point["y"]), (point["vx"], point["vy"]))


def part1(points):
    """Solve part 1."""
    time = binary_search(points)
    stars = draw(tick(points, time), fill="*", empty=" ")
    if "--show" in sys.argv:
        print(stars)
    return convert(stars, fill="*", empty=" ")


def part2(points):
    """Solve part 2."""
    return binary_search(points)


def binary_search(points):
    """Do a binary search for a message in the points.

    Assume that the message appears when the area of the point field is
    minimized. Use the derivative of the area and look for when it's zero.
    """
    lo, hi = 0, overshoot(points)
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if darea(points, mid) >= 0:
            hi = mid
        else:
            lo = mid

    return lo if area(points, lo) < area(points, hi) else hi


def overshoot(points):
    """Give an estimate of a time stamp that definitely overshoots the message."""
    return round(
        max(max(-x / (vx or 1), -y / (vy or 1)) for (x, y), (vx, vy) in points)
    )


def tick(points, time):
    """Move time by the given numbers of ticks"""
    return [((x + vx * time, y + vy * time), (vx, vy)) for (x, y), (vx, vy) in points]


def area(points, time=0):
    """Calculate the area taken up by the points"""
    min_x, min_y, max_x, max_y = boundary(tick(points, time))
    return (max_x - min_x) * (max_y - min_y)


def darea(points, time):
    """Calculate a derivate for the area at time t"""
    return (area(points, time + 1) - area(points, time - 1)) // 2


def boundary(points):
    """Find boundary of the field of points."""
    return (
        min(x for (x, _), _ in points),
        min(y for (_, y), _ in points),
        max(x for (x, _), _ in points),
        max(y for (_, y), _ in points),
    )


def draw(points, fill="#", empty="."):
    """Convert the field of points into a text string"""
    min_x, min_y, max_x, max_y = boundary(points)
    xys = {xy for xy, _ in points}
    return "\n".join(
        "".join(fill if (x, y) in xys else empty for x in range(min_x, max_x + 1))
        for y in range(min_y, max_y + 1)
    )


def convert(stars, fill="#", empty="."):
    """Convert a text string of stars into a string of letters.

    Transpose letters to simplify splitting.
    """
    stars = stars.replace(fill, "#").replace(empty, ".")
    transpose = ["".join(line) for line in zip(*stars.split("\n"))]

    # Split the message into individual letters
    letters = []
    letter = []
    for line in transpose:
        if all(char == "." for char in line):
            if letter:
                letters.append("\n".join(letter))
            letter = []
        else:
            letter.append(line)
    letters.append("\n".join(letter))

    # Convert each letter
    message = []
    for letter in letters:
        try:
            message.append(ALPHABET[letter])
        except KeyError:
            print(f"Unknown letter, please add to ALPHABET:\n{letter}")
            print(repr(letter))
    return "".join(message)


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        if path.startswith("-"):
            continue
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().rstrip())
        print("\n".join(str(solution) for solution in solutions))
