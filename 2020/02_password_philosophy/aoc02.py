"""Password Philosophy

Advent of Code 2020, day 2
Solution by Geir Arne Hjelle, 2020-12-02
"""
import pathlib
import sys
from dataclasses import dataclass
import parse

debug = print if "--debug" in sys.argv else lambda *_: None
PATTERN = parse.compile("{n1:d}-{n2:d} {char}: {word}")


@dataclass
class Password:
    word: str
    char: str
    num_1: int
    num_2: int

    @classmethod
    def from_str(cls, text):
        """Parse password and policy from string"""
        pw = PATTERN.parse(text)
        return cls(
            word=pw["word"],
            char=pw["char"],
            num_1=pw["n1"],
            num_2=pw["n2"],
        )

    def is_valid_first(self):
        """Check if password is valid according to the first policy"""
        return self.num_1 <= self.count_char() <= self.num_2

    def is_valid_second(self):
        """Check if password is valid according to the second policy

        != works as XOR: only one position can contain the given character
        """
        return self.has_char(self.num_1) != self.has_char(self.num_2)

    def count_char(self):
        """Count how many times char appears in password"""
        return self.word.count(self.char)

    def has_char(self, idx):
        """Check if word has char at given index, counting from 1"""
        return self.word[idx - 1] == self.char


def main(args):
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        print(f"\n{file_path}:")
        passwords = [Password.from_str(p.strip()) for p in file_path.open()]

        # Part 1
        valid_first = [p for p in passwords if p.is_valid_first()]
        debug("\n".join(str(p) for p in valid_first))
        print(f"{len(valid_first)} passwords are valid according to first policy")

        # Part 2
        valid_second = [p for p in passwords if p.is_valid_second()]
        debug("\n".join(str(p) for p in valid_second))
        print(f"{len(valid_second)} passwords are valid according to second policy")


if __name__ == "__main__":
    main(sys.argv[1:])
