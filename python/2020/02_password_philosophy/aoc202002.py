"""AoC 2, 2020: Password Philosophy"""

# Standard library imports
import pathlib
import sys
from dataclasses import dataclass

# Third party imports
import parse

PASSWORD_PATTERN = parse.compile("{first:d}-{second:d} {char}: {password}")


@dataclass
class PasswordPolicy:
    first: int
    second: int
    char: str
    password: str

    @classmethod
    def from_str(cls, line):
        """Parse one line into a PasswordPolicy

        >>> PasswordPolicy.from_str("4-6 e: adventofcode")
        PasswordPolicy(first=4, second=6, char='e', password='adventofcode')
        """
        return cls(**PASSWORD_PATTERN.parse(line).named)

    def is_valid_count(self):
        """Check if the password follows the count requirements

        ## Examples:

        >>> PasswordPolicy.from_str("4-6 e: adventofcode").is_valid_count()
        False

        >>> PasswordPolicy.from_str("1-3 o: passwordphilosophy").is_valid_count()
        True
        """
        return self.first <= self.password.count(self.char) <= self.second

    def is_valid_position(self):
        """Check if the password follows the position requirements

        ## Examples:

        >>> PasswordPolicy.from_str("4-6 e: adventofcode").is_valid_position()
        True

        >>> PasswordPolicy.from_str("1-3 o: passwordphilosophy").is_valid_position()
        False
        """
        return self._has_char(self.first) != self._has_char(self.second)

    def _has_char(self, pos):
        """Check if password has the character in the given position"""
        return self.password[pos - 1] == self.char


def parse(puzzle_input):
    """Parse input"""
    return [PasswordPolicy.from_str(line) for line in puzzle_input.split("\n")]


def part1(data):
    """Solve part 1"""
    return sum(policy.is_valid_count() for policy in data)


def part2(data):
    """Solve part 2"""
    return sum(policy.is_valid_position() for policy in data)


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
