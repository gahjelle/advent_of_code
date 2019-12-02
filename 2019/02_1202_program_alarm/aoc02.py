"""1202 Program Alarm

Advent of Code 2019, day 2
Solution by Geir Arne Hjelle, 2019-12-02
"""
import sys
import itertools

OP = {1: "+", 2: "*"}
GOAL = 19690720


def run_program(program, noun=12, verb=2):
    codes = program.copy()
    codes[1], codes[2] = noun, verb

    pointer = 0
    while True:
        if codes[pointer] == 99:
            return codes[0]

        opcode, pos_1, pos_2, pos_res = codes[pointer : pointer + 4]
        if max((pos_1, pos_2, pos_res)) >= len(codes):
            debug(f"Index out of range: {pos_1}, {pos_2}, {pos_res} ({len(codes)})")
            return None

        if opcode == 1:
            codes[pos_res] = codes[pos_1] + codes[pos_2]
        elif opcode == 2:
            codes[pos_res] = codes[pos_1] * codes[pos_2]
        else:
            debug(f"Unknown opcode {opcode} at index {pointer}")
            return None

        debug(
            f"=> {opcode}: {pos_1} {pos_2} {pos_res} --> "
            f"{codes[pos_1]} {OP[opcode]} {codes[pos_2]} = {codes[pos_res]}"
        )

        pointer += 4


def main():
    for filename in sys.argv[1:]:
        if filename.startswith("--"):
            continue

        print(f"\n{filename}:")
        with open(filename, mode="r") as fid:
            line = next(fid)
            program = [int(c) for c in line.split(",")]

            # Part 1
            print(f"Program 1202 ended at {run_program(program)}")

            # Part 2: Attempt to calculate noun and verb
            base = run_program(program, 0, 0)
            dn = run_program(program, 1, 0) - base
            dv = run_program(program, 0, 1) - base

            if dn >= 1 and dv >= 1:
                noun = (GOAL - base) // dn
                verb = (GOAL - base) % dn // dv
                if (result := run_program(program, noun, verb)) == GOAL:
                    print(f"{noun:02d}{verb:02d} -> {result}")
                    continue

            # Part 2: Brute force
            for noun, verb in itertools.product(range(100), range(100)):
                result = run_program(program, noun, verb)
                if result == GOAL:
                    print(f"{noun:02d}{verb:02d} -> {result}")
                    break
            else:
                print(f"Did not find a valid noun and verb")

if __name__ == "__main__":
    debug = print if "--debug" in sys.argv else lambda *_: None
    main()
