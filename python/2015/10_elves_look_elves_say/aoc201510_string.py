"""AoC 10, 2015: Elves Look, Elves Say"""

# Standard library imports
import pathlib
import sys


def parse(puzzle_input):
    """Parse input"""
    return puzzle_input


def part1(data, num_steps=40):
    """Solve part 1"""
    for _ in range(num_steps):
        data = look_and_say(data)
    return len(data)


def part2(data, num_steps=50):
    """Solve part 2"""
    for _ in range(num_steps):
        data = look_and_say(data)
    return len(data)


def look_and_say(digits):
    """Calculate the next look-and-say number.

    ## Examples:

    >>> look_and_say("1")
    '11'
    >>> look_and_say("11")
    '21'
    >>> look_and_say("21")
    '1211'
    >>> look_and_say("333")
    '33'
    >>> look_and_say("77777777777711")
    '12721'
    """
    next_sequence = []
    count = 1
    for prev, current in zip(digits, f"{digits}X"[1:]):
        if prev == current:
            count += 1
        else:
            next_sequence.append(f"{count}{prev}")
            count = 1
    return "".join(next_sequence)


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
