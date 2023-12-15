"""AoC 15, 2023: Lens Library."""

# Standard library imports
import collections
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    return puzzle_input.split(",")


def part1(words):
    """Solve part 1."""
    return sum(hash(word) for word in words)


def part2(words):
    """Solve part 2."""
    boxes = organize_to_boxes(words)
    return sum(
        (box_id + 1) * slot * value
        for box_id, box in boxes.items()
        for slot, (_, value) in enumerate(box, start=1)
    )


def hash(text):
    """Hash the given text

    Start with a current value of 0. Then, for each character in the string
    starting from the beginning:

    - Determine the ASCII code for the current character of the string.
    - Increase the current value by the ASCII code you just determined.
    - Set the current value to itself multiplied by 17.
    - Set the current value to the remainder of dividing itself by 256.

    >>> hash("HASH")
    52
    """
    value = 0
    for char in text:
        value = (17 * (value + ord(char))) % 256
    return value


def organize_to_boxes(words):
    """Organize the words into boxes based on HASHMAP."""
    boxes = collections.defaultdict(list)
    for word in words:
        if word.endswith("-"):
            name = word[:-1]
            box_num = hash(name)
            box = boxes[box_num]

            if name in (names := [n for n, _ in box]):
                box.pop(names.index(name))
        else:
            name, value = word[:-2], int(word[-1])
            box_num = hash(name)
            box = boxes[box_num]

            if name not in (names := [n for n, _ in box]):
                box.append((name, value))
            else:
                index = names.index(name)
                box[index] = (name, value)
    return boxes


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
