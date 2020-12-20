"""Leonardo's Monorail

Advent of Code 2016, day 12
Solution by Geir Arne Hjelle, 2016-12-12
"""

# Standard library imports
import pathlib
import sys


def precompile(instructions):
    compiled_instructions = list()
    for instruction, *params in instructions:
        if instruction == "cpy":
            if params[0].isnumeric():
                compiled_instructions.append(("set", params[1], "z", int(params[0])))
            else:
                compiled_instructions.append(("set", params[1], params[0], 0))
        elif instruction == "inc":
            compiled_instructions.append(("set", params[0], params[0], 1))
        elif instruction == "dec":
            compiled_instructions.append(("set", params[0], params[0], -1))
        elif instruction == "jnz":
            compiled_instructions.append(("jnz", params[0], int(params[1])))

    return compiled_instructions


def run_code(instructions, initial_registers=None):
    registers = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "z": 0,  # z is dummy register, always zero
    }
    pointer = 0
    num_instructions = len(instructions)
    if initial_registers is not None:
        registers.update(initial_registers)

    while pointer < num_instructions:
        instruction, *params = instructions[pointer]
        if instruction == "set":
            registers[params[0]] = registers[params[1]] + params[2]
            pointer += 1
        elif instruction == "jnz":
            value = registers[params[0]] if params[0] in registers else int(params[0])
            pointer += params[1] if value else 1

    return registers


def main(args):
    """Solve the problem for all file paths"""
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        solve(file_path)


def solve(file_path):
    """Solve the problem for one file path"""
    print(f"\n{file_path}:")
    with file_path.open(mode="r") as fid:
        instructions = precompile(line.strip().split() for line in fid)

    registers = run_code(instructions)
    print(f"The value of a is {registers['a']} after running the assembunny code")

    registers = run_code(instructions, initial_registers={"c": 1})
    print(f"Initializing c to 1 gives a value of {registers['a']} for a")


if __name__ == "__main__":
    main(sys.argv[1:])
