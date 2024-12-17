"""AoC 17, 2024: Chronospatial Computer."""

# Standard library imports
import collections
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    memory, program = puzzle_input.split("\n\n")
    return (
        [
            int(line[2:])
            for line in memory.replace("Register ", "").replace(":", "").split("\n")
        ],
        [int(opcode) for opcode in program.replace("Program: ", "").split(",")],
    )


def part1(data):
    """Solve part 1."""
    (a, b, c), program = data
    return ",".join(str(out) for out in run_program(program, a, b, c))


def part2(data):
    """Solve part 2.

    Observations about my input:

    Each loop through the program, it writes one output and divides A by 8
    (truncated). So, for a program to terminate with 16 outputs, A needs to
    start with a value between 8**15 and 8**16-1.

    There's a pattern to when we get a match of the last n outputs in the
    program. If we match the last n outputs for A = a, then we do the same for A
    = 8a, 8a+1, ..., 8a+7. Use this to do a breadth-first search through the
    possible values for A.
    """
    (_, b, c), program = data
    queue = collections.deque([(len(program) - 1, range(8))])
    while queue:
        idx, aa = queue.popleft()
        for a in aa:
            output = run_program(program, a, b, c)
            if output == program[idx:]:
                if idx == 0:
                    return a
                else:
                    queue.append((idx - 1, range(a * 8, (a + 1) * 8)))


def run_program(program, a, b, c):
    convert = {0: 0, 1: 1, 2: 2, 3: 3}
    pointer, step = 0, 2
    output = []
    while pointer < len(program):
        convert |= {4: a, 5: b, 6: c}
        match program[pointer : pointer + 2]:
            case [0, combo]:
                a >>= convert[combo]
            case [1, literal]:
                b ^= literal
            case [2, combo]:
                b = convert[combo] & 7
            case [3, literal]:
                if a:
                    pointer = literal - step
            case [4, _]:
                b ^= c
            case [5, combo]:
                output.append(convert[combo] & 7)
            case [6, combo]:
                b = a >> convert[combo]
            case [7, combo]:
                c = a >> convert[combo]
            case _:
                print(f"Unknown statement: {program[pointer:pointer+2]}")
        pointer += step
    return output


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
