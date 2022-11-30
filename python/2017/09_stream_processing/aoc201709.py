"""AoC 9, 2017: Stream Processing"""

# Standard library imports
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input"""
    return separate_stream(puzzle_input)


def separate_stream(stream):
    """Separate garbage from stream

    Garbage is delimited by < and >. ! is used as an escape character.

    >>> separate_stream("{<aoc!>,{},<!aoc>, {}}")
    ('{, {}}', 'aoc,{},<oc')
    """
    len_stream = len(stream)
    cleaned, garbage = [], []
    currently_garbage = False

    pointer = 0
    while pointer < len_stream:
        current_char = stream[pointer]
        pointer += 1
        match current_char:
            case "!":
                pointer += 1  # Ignore next character
            case "<" if not currently_garbage:
                currently_garbage = True
            case ">":
                currently_garbage = False
            case _:
                (garbage if currently_garbage else cleaned).append(current_char)

    return "".join(cleaned), "".join(garbage)


def part1(data):
    """Solve part 1"""
    stream, _ = data
    return sum(count_levels(stream))


def part2(data):
    """Solve part 2"""
    _, garbage = data
    return len(garbage)


def count_levels(stream):
    """Count levels in stream

    >>> list(count_levels("{{{},{{}}},{}}"))
    [1, 2, 3, 3, 4, 2]
    """
    current_level = 0
    for char in stream:
        if char == "{":
            current_level += 1
            yield current_level
        elif char == "}":
            current_level -= 1


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
