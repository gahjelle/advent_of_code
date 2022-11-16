"""Scrambled Letters and Hash

Advent of Code 2016, day 21
Solution by Geir Arne Hjelle, 2021-01-01
"""

# Standard library imports
import pathlib
import sys

# Third party imports
import parse

debug = print if "--debug" in sys.argv else lambda *_: None

OPERATIONS = {}


def register(format):
    """Decorator registering operations"""

    def _decorator(func):
        key = func.__name__.replace("_", " ")
        parser = parse.compile(format)
        OPERATIONS[key] = (parser, func)

        return func

    return _decorator


@register("swap position {pos_1:d} with position {pos_2:d}")
def swap_position(password, pos_1, pos_2, scramble=True):
    """The letters at indexes X and Y (counting from 0) should be swapped"""
    password[pos_1], password[pos_2] = password[pos_2], password[pos_1]


@register("swap letter {letter_1} with letter {letter_2}")
def swap_letter(password, letter_1, letter_2, scramble=True):
    """The letters X and Y should be swapped (regardless of where they appear
    in the string)"""
    pos_1 = password.index(letter_1)
    pos_2 = password.index(letter_2)
    password[pos_1], password[pos_2] = password[pos_2], password[pos_1]


@register("rotate left {steps:d} ste{ps}")
def rotate_left(password, steps, scramble=True, **_):
    """The whole string should be rotated; for example, one left rotation would
    turn abcd into bcda"""
    if scramble:
        for _ in range(steps):
            password.append(password.pop(0))
    else:
        for _ in range(steps):
            password.insert(0, password.pop())


@register("rotate right {steps:d} ste{ps}")
def rotate_right(password, steps, scramble=True, **_):
    """The whole string should be rotated; for example, one right rotation
    would turn abcd into dabc"""
    if scramble:
        for _ in range(steps):
            password.insert(0, password.pop())
    else:
        for _ in range(steps):
            password.append(password.pop(0))


@register("rotate based on position of letter {letter}")
def rotate_based(password, letter, scramble=True):
    """The whole string should be rotated to the right

    Based on the index of letter X (counting from 0) as determined before this
    instruction does any rotations. Once the index is determined, rotate the
    string to the right one time, plus a number of times equal to that index,
    plus one additional time if the index was at least 4"""
    pos = password.index(letter)
    if scramble:
        rot = 1 + pos + (pos >= 4)
        for _ in range(rot):
            password.insert(0, password.pop())
    else:
        rot = {0: 7, 1: 7, 2: 2, 3: 6, 4: 1, 5: 5, 6: 0, 7: 4}[pos]
        for _ in range(rot):
            password.insert(0, password.pop())


@register("reverse positions {pos_1:d} through {pos_2:d}")
def reverse_positions(password, pos_1, pos_2, scramble=True):
    """The span of letters at indexes X through Y (including the letters at X
    and Y) should be reversed in order"""
    sub = slice(pos_1, pos_2 + 1)
    password[sub] = password[sub][::-1]


@register("move position {pos_1:d} to position {pos_2:d}")
def move_position(password, pos_1, pos_2, scramble=True):
    """The letter which is at index X should be removed from the string, then
    inserted such that it ends up at index Y"""
    if scramble:
        password.insert(pos_2, password.pop(pos_1))
    else:
        password.insert(pos_1, password.pop(pos_2))


def scramble(password, operations, scramble=True):
    """Scramble the password using the operations"""
    pw_list = list(password)

    for operation in operations:
        key = " ".join(operation.split()[:2])
        parser, func = OPERATIONS[key]
        func(pw_list, **parser.parse(operation).named, scramble=scramble)
        debug(f"{operation} => {''.join(pw_list)!r}")

    return "".join(pw_list)


def unscramble(password, operations):
    """Unscramble the password using the operations"""
    return scramble(password, operations[::-1], scramble=False)


def main(args):
    """Solve the problem for all file paths"""
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        solve(file_path)


def solve(file_path):
    """Solve the problem for one file path"""
    print(f"\n{file_path}:")
    operations = file_path.read_text().strip().split("\n")

    # Part 1
    part_1 = scramble("abcdefgh", operations)
    print(f"The scrambled password is {part_1}")

    # Part 2
    part_2 = unscramble("fbgdceah", operations)
    print(f"The unscrambled password is {part_2}")


if __name__ == "__main__":
    main(sys.argv[1:])
