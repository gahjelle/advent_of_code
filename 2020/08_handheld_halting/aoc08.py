"""Handheld Halting

Advent of Code 2020, day 8
Solution by Geir Arne Hjelle, 2020-12-08
"""
import pathlib
import sys
import parse

debug = print if "--debug" in sys.argv else lambda *_: None

INSTRUCTION = parse.compile("{operation} {argument:d}")


def acc(argument):
    """Change accumulator

    acc increases or decreases a single global value called the accumulator by
    the value given in the argument. For example, acc +7 would increase the
    accumulator by 7. The accumulator starts at 0. After an acc instruction,
    the instruction immediately below it is executed next.
    """
    return 1, argument


def nop(argument):
    """Do nothing

    nop stands for No OPeration - it does nothing. The instruction immediately
    below it is executed next.
    """
    return 1, 0


def jmp(argument):
    """Jump to a new instruction

    jmp jumps to a new instruction relative to itself. The next instruction to
    execute is found using the argument as an offset from the jmp instruction;
    for example, jmp +2 would skip the next instruction, jmp +1 would continue
    to the instruction immediately below it, and jmp -20 would cause the
    instruction 20 lines above to be executed next.
    """
    return argument, 0


INSTRUCTIONS = {"acc": acc, "nop": nop, "jmp": jmp}


def run_code(code):
    """Run the given code until a loop is detected"""
    pointer, accumulator = 0, 0
    visited = [False] * len(code) + [True]

    while not visited[pointer]:
        visited[pointer] = True
        instruction = INSTRUCTION.parse(code[pointer])

        dptr, dacc = INSTRUCTIONS[instruction["operation"]](instruction["argument"])
        pointer += dptr
        accumulator += dacc

    return accumulator, pointer == len(code)


def create_mutant(code, line_num):
    """Create a mutant by changing the given line num"""
    instruction = INSTRUCTION.parse(code[line_num])
    if instruction["operation"] == "acc":
        return code, False

    mutant = code.copy()
    op = "nop" if instruction["operation"] == "jmp" else "jmp"
    mutant[line_num] = f"{op} {instruction['argument']}"
    debug(f"{line_num:3d} {code[line_num]} -> {mutant[line_num]}")

    return mutant, True


def main(args):
    """Solve the problem for all file paths"""
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        solve(file_path)


def solve(file_path):
    """Solve the problem for one file path"""
    print(f"\n{file_path}:")
    code = file_path.read_text().strip().split("\n")

    # Part 1
    accumulator, _ = run_code(code)
    print(f"The original code accumulates {accumulator}")

    # Part 2
    for line_num in range(len(code)):
        mutant, changed = create_mutant(code, line_num)
        if not changed:
            continue

        accumulator, ended = run_code(mutant)
        if ended:
            print(f"The fixed code accumulates {accumulator}")
            break


if __name__ == "__main__":
    main(sys.argv[1:])
