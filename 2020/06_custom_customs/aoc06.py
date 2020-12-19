"""Custom Customs

Advent of Code 2020, day 6
Solution by Geir Arne Hjelle, 2020-12-06
"""
# Standard library imports
import pathlib
import sys

debug = print if "--debug" in sys.argv else lambda *_: None


def count_any(group):
    """Count number of questions anyone in the group answered yes to"""
    return len(set.union(*[set(p) for p in group.split()]))


def count_all(group):
    """Count number of questions everyone in the group answered yes to"""
    return len(set.intersection(*[set(p) for p in group.split()]))


def main(args):
    """Solve the problem for all input files"""
    for file_path in (pathlib.Path(p) for p in args if not p.startswith("-")):
        solve(file_path)


def solve(file_path):
    """Solve the problem for one input file"""
    print(f"\n{file_path}:")
    groups = file_path.read_text().split("\n\n")

    # Part 1
    num_yes_any = sum(count_any(g) for g in groups)
    print(f"Anyone answered yes: {num_yes_any}")

    # Part 2
    num_yes_all = sum(count_all(g) for g in groups)
    print(f"Everyone answered yes: {num_yes_all}")


if __name__ == "__main__":
    main(sys.argv[1:])
