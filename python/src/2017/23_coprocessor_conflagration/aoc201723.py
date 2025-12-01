"""AoC 23, 2017: Coprocessor Conflagration."""

# Standard library imports
import collections
import math
import pathlib
import sys
from dataclasses import dataclass


def parse_data(puzzle_input):
    """Parse input."""
    return [parse_instruction(line) for line in puzzle_input.split("\n")]


def parse_instruction(line):
    """Parse one instruction.

    ## Examples:

    >>> parse_instruction("snd g")
    ('snd', 'g')
    >>> parse_instruction("set g 45")
    ('set', 'g', 45)
    >>> parse_instruction("mul z a")
    ('mul', 'z', 'a')
    """
    instruction, register, *args = line.split()
    return instruction, try_int(register), *[try_int(arg) for arg in args]


def try_int(maybe_number):
    """Convert to int if possible.

    ## Examples:

    >>> try_int("42")
    42
    >>> try_int("g")
    'g'
    """
    try:
        return int(maybe_number)
    except ValueError:
        return maybe_number


def part1(instructions):
    """Solve part 1."""
    program = Program(instructions, debug=True)
    program.run()
    return program.num_multiplications


def part2(instructions):
    """Solve part 2.

    The given program calculates the number of non-primes in a given range. Find
    the range, then calculate the non-primes with a more effective sieve.
    """
    step = -instructions[30][2]

    # Run set up to find start and end values, then jump out of program
    instructions[8] = ("jnz", 1, len(instructions))
    program = Program(instructions, debug=False)
    program.run()
    start, end = program.registers["b"], program.registers["c"]

    # Calculate non-primes
    return non_primes(start, end, step)


def non_primes(start, end, step):
    """Find the number of non-primes in the given interval.

    ## Example:

        20, 26, 32, 35, 38, 44, 50, 56, 62, 65, 68, 74, 77, 80, 86, 92, 95, 98

    >>> non_primes(20, 100, 3)
    18
    """
    divisors = primes(math.isqrt(end) + 1)

    num_non_primes = 0
    for num in range(start, end + 1, step):
        for divisor in divisors:
            if num % divisor == 0:
                num_non_primes += 1
                break
    return num_non_primes


def primes(end):
    """Find the primes up to end.

    ## Example:

    >>> primes(50)
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    """
    divisors = [2, 3]
    for num in range(5, end + 1):
        for divisor in divisors:
            if num % divisor == 0:
                break
        else:
            divisors.append(num)
    return divisors


class Registers(collections.UserDict):
    """Dictionary with special handling of missing keys."""

    def __missing__(self, key):
        """Pass through integer keys. Otherwise default to 0.

        ## Examples:

        >>> Registers({"a": 1})["a"]
        1
        >>> Registers({"a": 1})["b"]
        0
        >>> Registers({"a": 1})[14]
        14
        """
        if isinstance(key, int):
            return key

        self.data[key] = 0
        return 0


@dataclass
class Program:
    """A program that can be run."""

    instructions: list[tuple[str, str, int]]
    num_multiplications: int = 0
    debug: bool = False

    def __post_init__(self):
        """Set up registers."""
        self.num_instructions = len(self.instructions)
        self.registers = Registers({"a": 0 if self.debug else 1})

    def run(self):
        """Run program to termination."""
        pointer = 0
        while 0 <= pointer < self.num_instructions:
            instruction, register, *args = self.instructions[pointer]
            value = self.registers[args[0]] if args else 0

            if instruction == "set":
                self.registers[register] = value
            elif instruction == "sub":
                self.registers[register] -= value
            elif instruction == "mul":
                self.registers[register] *= value
                self.num_multiplications += 1
            elif instruction == "jnz" and self.registers[register] != 0:
                pointer += value - 1

            pointer += 1


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
