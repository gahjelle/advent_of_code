"""Secure Container

Advent of Code 2019, day 4
Solution by Geir Arne Hjelle, 2019-12-04
"""
from collections import Counter
import pathlib
import re
import sys

import pyplugs

PLUGINS = pyplugs._plugins._PLUGINS  # TODO: Fix bug


def check(password, rules):
    for idx, rule in enumerate(rules, start=1):
        if not rule(password):
            return idx

    return 0


@pyplugs.register
def increasing(password):
    return password == "".join(sorted(password))


@pyplugs.register
def has_doubles(password):
    for digit1, digit2 in zip(password, password[1:]):
        if digit1 == digit2:
            return True

    return False


@pyplugs.register
def has_simple_doubles(password):
    xtended_pw = f"x{password}x"
    for digit in set(password):
        pattern = rf"[^{digit}]{digit}{digit}[^{digit}]"
        if re.search(pattern, xtended_pw):
            return True

    return False


def main():
    rules = [p.func for p in PLUGINS[""][__name__].values()]
    for file_path in [pathlib.Path(p) for p in sys.argv[1:] if not p.startswith("-")]:
        print(f"\n{file_path}:")
        text = file_path.read_text()
        num_min, num_max = [int(n) for n in text.split("-")]
        pw_range = range(num_min, num_max + 1)
        failed_rule = Counter(check(str(pw), rules) for pw in pw_range)

        # Part 1
        num_valid_1 = sum(v for k, v in failed_rule.items() if k not in {1, 2})
        print(f"Found {num_valid_1} level-1 passwords between {num_min} and {num_max}")

        # Part 2
        num_valid_2 = sum(v for k, v in failed_rule.items() if k not in {1, 2, 3})
        print(f"Found {num_valid_2} level-2 passwords between {num_min} and {num_max}")


if __name__ == "__main__":
    debug = print if "--debug" in sys.argv else lambda *_: None
    main()
