"""Internet Protocol Version 7

Advent of Code 2016, day 7
Solution by Geir Arne Hjelle, 2016-12-07
"""

# Standard library imports
import pathlib
import sys


def supports_tls(tokens):
    good, bad = tokens[::2], tokens[1::2]
    return any(has_abba(t) for t in good) and not any(has_abba(t) for t in bad)


def has_abba(string):
    for t in zip(string[:-3], string[1:-2], string[2:-1], string[3:]):
        if t[0] == t[3] and t[1] == t[2] and t[0] != t[1]:
            return True
    return False


def supports_ssl(tokens):
    good, bad = "---".join(tokens[::2]), "---".join(tokens[1::2])
    return any(bab in bad for bab in find_aba(good))


def find_aba(string):
    for t in zip(string[:-2], string[1:-1], string[2:]):
        if t[0] == t[2] and t[0] != t[1]:
            yield t[1] + t[0] + t[1]


def main(args):
    """Solve the problem for all file paths"""
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        solve(file_path)


def solve(file_path):
    """Solve the problem for one file path"""
    print(f"\n{file_path}:")
    with file_path.open(mode="r") as fid:
        tokens = [ln.strip().replace("[", " ").replace("]", " ").split() for ln in fid]

    print(f"{sum(supports_tls(t) for t in tokens)} IPs support TLS")
    print(f"{sum(supports_ssl(t) for t in tokens)} IPs support SSL")


if __name__ == "__main__":
    main(sys.argv[1:])
