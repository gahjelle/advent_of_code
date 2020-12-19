"""Docking Data

Advent of Code 2020, day 14
Solution by Geir Arne Hjelle, 2020-12-14
"""
# Standard library imports
import pathlib
import sys

# Third party imports
import parse

debug = print if "--debug" in sys.argv else lambda *_: None

_MASK_PATTERN = parse.compile("mask = {mask}")
_MEM_PATTERN = parse.compile("mem[{address:d}] = {value:d}")


def main(args):
    """Solve the problem for all file paths"""
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        solve(file_path)


def apply_mask_to_value(mask, value):
    """Apply the mask to the given value"""
    all_bits = 2 ** len(mask) - 1
    active_mask = {
        2 ** bit: bool(int(onoff))
        for bit, onoff in enumerate(mask[::-1])
        if onoff != "X"
    }

    for bit, onoff in active_mask.items():
        if onoff:
            value |= bit
        else:
            value &= -(bit + 1) & all_bits
    return value


def update_memory_1(memory, address, value, mask):
    """Write a value to a memory address after applying a mask"""
    memory[address] = apply_mask_to_value(mask, value)


def apply_mask_to_address(mask, address):
    """Apply the mask to the given address"""
    num_bits = len(mask)
    bin_address = ("0" * num_bits + bin(address)[2:])[-num_bits:]
    return "".join(
        "X" if m == "X" else str(int(a) | int(m)) for a, m in zip(bin_address, mask)
    )


def create_masks(masks):
    """Convert Xs to 0s AND 1s"""
    if "X" not in masks[0]:
        return masks

    new_masks = []
    for mask in masks:
        idx = mask.find("X")
        new_masks.extend(create_masks([f"{mask[:idx]}0{mask[idx+1:]}"]))
        new_masks.extend(create_masks([f"{mask[:idx]}1{mask[idx+1:]}"]))

    return new_masks


def update_memory_2(memory, address, value, mask):
    """Write a value to addresses constructed by applying a mask"""
    masks = create_masks([apply_mask_to_address(mask, address)])
    for address in [int(m, base=2) for m in masks]:
        memory[address] = value


def solve(file_path):
    """Solve the problem for one file path"""
    print(f"\n{file_path}:")

    memory_1 = {}
    memory_2 = {}
    active_mask = None
    with file_path.open(mode="r") as fid:
        for line in fid:
            if mask := _MASK_PATTERN.parse(line.strip()):
                active_mask = mask["mask"]
                continue

            if mem := _MEM_PATTERN.parse(line.strip()):
                update_memory_1(memory_1, mem["address"], mem["value"], active_mask)
                update_memory_2(memory_2, mem["address"], mem["value"], active_mask)

    # Report part 1
    part_1 = sum(memory_1.values())
    print(f"The sum of the values in memory is {part_1}")

    # Report part 2
    part_2 = sum(memory_2.values())
    print(f"Using the v2 decoder protocol, the sum of the values in memory is {part_2}")


if __name__ == "__main__":
    main(sys.argv[1:])
