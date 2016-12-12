"""Leonardo's Monorail

Advent of Code 2016, day 12
Solution by Geir Arne Hjelle, 2016-12-12
"""
import sys


def run_code(instructions, initial_registers=None):
    registers = dict(a=0, b=0, c=0, d=0)
    pointer = 0
    if initial_registers is not None:
        registers.update(initial_registers)

    while pointer < len(instructions):
        instruction, *params = instructions[pointer]
        pointer += globals()[instruction](registers, *params)

    return registers


def cpy(registers, value, register):
    value = registers.get(value, safe_int(value))
    registers[register] = value
    return 1


def inc(registers, register):
    registers[register] += 1
    return 1


def dec(registers, register):
    registers[register] -= 1
    return 1


def jnz(registers, value, ptr_offset):
    value = registers.get(value, safe_int(value))
    return int(ptr_offset) if value else 1


def safe_int(string):
    try:
        return int(string)
    except ValueError:
        pass


def main():
    for filename in sys.argv[1:]:
        print('\n{}:'.format(filename))
        with open(filename, mode='r') as fid:
            instructions = [line.strip().split() for line in fid]

        registers = run_code(instructions)
        print('The value of a is {} after running the assembunny code'.format(registers['a']))

        registers = run_code(instructions, initial_registers=dict(c=1))
        print('Initializing c to 1 gives a value of {} for a'.format(registers['a']))


if __name__ == '__main__':
    main()
