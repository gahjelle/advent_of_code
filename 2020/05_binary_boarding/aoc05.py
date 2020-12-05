"""Binary Boarding

Advent of Code 2020, day 5
Solution by Geir Arne Hjelle, 2020-12-05
"""
import pathlib
import sys

debug = print if "--debug" in sys.argv else lambda *_: None

PASS2BIN = {"F": "0", "B": "1", "L": "0", "R": "1"}


def decode_seat_id(boarding_pass):
    """Decode a boarding pass string as a seat id"""
    return int("".join(PASS2BIN[c] for c in boarding_pass), 2)


def find_missing(seat_ids):
    """Find the missing seat_ids in a list of nearby seat IDs"""
    all_ids = set(range(min(seat_ids), max(seat_ids) + 1))
    return [str(id) for id in all_ids - set(seat_ids)]


def main(args):
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        print(f"\n{file_path}:")
        seat_ids = [decode_seat_id(bp.strip()) for bp in file_path.open()]

        # Part 1
        print(f"The highest seat ID is {max(seat_ids)}")

        # Part 2
        print(f"The missing seat ID is {', '.join(find_missing(seat_ids))}")


if __name__ == "__main__":
    main(sys.argv[1:])
