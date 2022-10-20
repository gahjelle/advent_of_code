"""AoC 14, 2020: Docking Data"""

# Standard library imports
import pathlib
import sys

# Third party imports
import parse

MASK_PATTERN = parse.compile("mask = {mask}")
MEMORY_PATTERN = parse.compile("mem[{address:d}] = {value:d}")


def parse(puzzle_input):
    """Parse input"""
    program = []
    for line in puzzle_input.split("\n"):
        if match := MASK_PATTERN.parse(line):
            active_mask = match["mask"]
        if match := MEMORY_PATTERN.parse(line):
            program.append((active_mask, match["address"], match["value"]))
    return program


def part1(data):
    """Solve part 1"""
    memory = {
        address: apply_mask_to_value(mask, value) for mask, address, value in data
    }
    return sum(memory.values())


def part2(data):
    """Solve part 2"""
    memory = {
        address: value
        for mask, address_seed, value in data
        for address in construct_masks(update_mask_with_address(mask, address_seed))
    }
    return sum(memory.values())


def apply_mask_to_value(mask, value):
    """Apply mask to value.

    The current bitmask is applied to values immediately before they are written
    to memory: a 0 or 1 overwrites the corresponding bit in the value, while an
    X leaves the bit in the value unchanged.

    ## Examples:

    >>> apply_mask_to_value("XXXXXXXXXXX10XXXX1",  42)
    75
    """
    num_bits = len(mask)
    value_str = ("0" * num_bits + bin(value)[2:])[-num_bits:]
    return int(
        "".join(
            onoff if mask_char == "X" else mask_char
            for onoff, mask_char in zip(value_str, mask)
        ),
        base=2,
    )


def construct_masks(mask):
    """Find all possible masks by resolving floating bits

    If the bitmask bit is X, the corresponding memory address bit is floating.

    A floating bit is not connected to anything and instead fluctuates
    unpredictably. In practice, this means the floating bits will take on all
    possible values, potentially causing many memory addresses to be written all at
    once!

    ## Example:

    >>> list(construct_masks("00X1X"))
    ['00010', '00011', '00110', '00111']
    """
    idx = mask.find("X")
    if idx == -1:
        yield mask
    else:
        yield from construct_masks(f"{mask[:idx]}0{mask[idx + 1:]}")
        yield from construct_masks(f"{mask[:idx]}1{mask[idx + 1:]}")


def update_mask_with_address(mask, address):
    """Apply mask to address

    ## Example:

    >>> update_mask_with_address("0X0X100X", 42)
    '0X1X101X'
    """
    num_bits = len(mask)
    address_str = ("0" * num_bits + bin(address)[2:])[-num_bits:]
    return "".join(
        mask_char if mask_char in {"X", "1"} else onoff
        for onoff, mask_char in zip(address_str, mask)
    )


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
