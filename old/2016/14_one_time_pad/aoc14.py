"""One-Time Pad

Advent of Code 2016, day 14
Solution by Geir Arne Hjelle, 2016-12-14
"""
# Standard library imports
import hashlib
import itertools
import pathlib
import sys


def generate_md5_numbers(salt, stretch=0):
    for counter in itertools.count(start=0, step=1):
        if not counter % 1000:
            print(".", end="", flush=True)
        md5 = hashlib.md5()
        md5.update(bytes(salt + str(counter), encoding="utf-8"))

        for _ in range(stretch):
            digest = md5.hexdigest()
            md5 = hashlib.md5()
            md5.update(bytes(digest, encoding="utf-8"))

        digest = md5.hexdigest()
        counts = [(c, len(list(g))) for c, g in itertools.groupby(digest)]
        for c, lg in [(c, lg) for c, lg in counts if lg >= 5]:
            yield counter, c, lg
            break
        for c, lg in [(c, lg) for c, lg in counts if lg >= 3]:
            yield counter, c, lg
            break


def find_onetime_pads(salt, stretch=0):
    candidates = dict()
    onetime_pads = set()
    gen_nums = iter(generate_md5_numbers(salt, stretch))
    counter = 0

    while len(onetime_pads) < 64 or counter < sorted(onetime_pads)[63] + 1000:
        counter, char, count = next(gen_nums)
        if char in candidates:
            candidates[char] = [
                idx for idx in candidates[char] if counter - 1000 <= idx < counter
            ]
        if count >= 5:
            [onetime_pads.add(candidate) for candidate in candidates[char]]
        candidates.setdefault(char, list()).append(counter)

    return max(sorted(onetime_pads)[:64])


def main(args):
    """Solve the problem for all file paths"""
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        solve(file_path)


def solve(file_path):
    """Solve the problem for one file path"""
    print(f"\n{file_path}:")
    with file_path.open(mode="r") as fid:
        for line in fid:
            salt = line.strip()
            print(f" Index {find_onetime_pads(salt)} gives the 64th key")
            print(
                f" Index {find_onetime_pads(salt, 2016)} gives the stretched 64th key"
            )


if __name__ == "__main__":
    main(sys.argv[1:])
