"""Operation Order

Advent of Code 2020, day 18
Solution by Geir Arne Hjelle, 2020-12-18
"""
import pathlib
import re
import sys

debug = print if "--debug" in sys.argv else lambda *_: None


class EvaluatingInt(int):
    """Integers that can evaluate expressions"""

    @classmethod
    def evaluate(cls, expression):
        """Evaluate expression"""

        def wrap_class(match):
            """Wrap a regex match in a class constructor"""
            return f"{cls.__name__}({match.group()})"

        return eval(re.sub(r"\d+", wrap_class, expression.translate(cls.ops)))


class LeftRightInt(EvaluatingInt):
    """Integers that add and multiply left to right

    Use - for multiplication, so addition and multiplication have the same
    precedence
    """

    ops = str.maketrans({"+": "+", "*": "-"})

    def __add__(self, other):
        return self.__class__(super().__add__(other))

    def __sub__(self, other):
        return self.__class__(super().__mul__(other))


class PlusFirstInt(EvaluatingInt):
    """Integers where addition have precedence over multiplication

    Use * for addition and + for multiplication to flip precedence
    """

    ops = str.maketrans({"+": "*", "*": "+"})

    def __mul__(self, other):
        return self.__class__(super().__add__(other))

    def __add__(self, other):
        return self.__class__(super().__mul__(other))


def main(args):
    """Solve the problem for all file paths"""
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        solve(file_path)


def solve(file_path):
    """Solve the problem for one file path"""
    print(f"\n{file_path}:")
    expressions = file_path.read_text().strip().split("\n")

    # Part 1
    results = [LeftRightInt.evaluate(e) for e in expressions]
    print(f"The total sum is {sum(results)}")

    # Part 2
    results = [PlusFirstInt.evaluate(e) for e in expressions]
    print(f"The total sum is {sum(results)}")


if __name__ == "__main__":
    main(sys.argv[1:])
