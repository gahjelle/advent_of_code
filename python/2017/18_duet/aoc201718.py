"""AoC 18, 2017: Duet."""

# Standard library imports
import collections
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
    program = Program(instructions, play_sound=True)

    while True:
        status = program.step()
        if status != "running":
            return program.last_sound_played


def part2(instructions):
    """Solve part 2."""
    queue_0, queue_1 = collections.deque(), collections.deque()
    program_0 = Program(instructions, program_id=0, queue=queue_0, other=queue_1)
    program_1 = Program(instructions, program_id=1, queue=queue_1, other=queue_0)

    while True:
        status_0, status_1 = program_0.step(), program_1.step()
        if status_0 != "running" and status_1 != "running":
            return program_1.num_messages_sent


class Registers(collections.UserDict):
    """Dictionary with special handling of missing keys."""

    def __missing__(self, key):
        """Pass through integer keys. Otherwise default to 0.

        ## Examples:

        >>> Registers({"p": 1})["p"]
        1
        >>> Registers({"p": 1})["q"]
        0
        >>> Registers({"p": 1})[14]
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
    program_id: int = 0
    queue: collections.deque = None
    other: collections.deque = None
    play_sound: bool = False
    pointer: int = 0
    num_messages_sent: int = 0
    last_sound_played: int = 0

    def __post_init__(self):
        """Set up registers."""
        self.num_instructions = len(self.instructions)
        self.registers = Registers({"p": self.program_id})

    def step(self):
        """Run one step of the program."""
        if self.pointer < 0 or self.pointer >= self.num_instructions:
            return "terminated"

        instruction, register, *args = self.instructions[self.pointer]
        value = self.registers[args[0]] if args else 0

        if instruction == "snd" and self.play_sound:
            self.last_sound_played = self.registers[register]
        elif instruction == "snd":
            self.num_messages_sent += 1
            self.other.append(self.registers[register])
        elif instruction == "set":
            self.registers[register] = value
        elif instruction == "add":
            self.registers[register] += value
        elif instruction == "mul":
            self.registers[register] *= value
        elif instruction == "mod":
            self.registers[register] %= value
        elif instruction == "rcv" and self.play_sound:
            return "terminated"
        elif instruction == "rcv":
            if self.queue:
                self.registers[register] = self.queue.popleft()
            else:
                return "waiting"
        elif instruction == "jgz" and self.registers[register] > 0:
            self.pointer += value - 1
        self.pointer += 1
        return "running"


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
