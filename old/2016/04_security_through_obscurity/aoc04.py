"""Security Through Obscurity

Advent of Code 2016, day 4
Solution by Geir Arne Hjelle, 2016-12-04
"""
# Standard library imports
import pathlib
import sys

debug = print if "--debug" in sys.argv else lambda *_: None


def _parse_string(string):
    checksum = string.strip()[-6:-1]
    messages = string.strip()[:-7].split("-")
    sector_id = int(messages.pop(-1))
    message = " ".join(messages)

    return message, sector_id, checksum


def check_room(string):
    message, sector_id, checksum = _parse_string(string)
    counter = {
        c: f"{10000 - message.count(c):04d}{c}" for c in set(message) if c != " "
    }
    actual_checksum = "".join(sorted(counter, key=lambda c: counter[c]))[:5]

    return sector_id if checksum == actual_checksum else 0


def decrypt_room(string):
    letters = "abcdefghijklmnopqrstuvwxyz"
    message, sector_id, _ = _parse_string(string)
    decrypted = list()

    for c in message:
        try:
            idx = letters.index(c)
            decrypted.append(letters[(idx + sector_id) % 26])
        except ValueError:
            decrypted.append(" ")

    return sector_id, "".join(decrypted)


def main(args):
    """Solve the problem for all file paths"""
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        solve(file_path)


def solve(file_path):
    """Solve the problem for one file path"""
    print(f"\n{file_path}:")

    with open(file_path, mode="r") as fid:
        messages = [decrypt_room(ln) for ln in fid if check_room(ln)]
    debug("\n".join(f"{m[0]}: {m[1]}" for m in sorted(messages)))

    print(f"Sum of sector IDs is {sum(m[0] for m in messages)}")
    print("\n".join(f"{m[1]} ({m[0]})" for m in messages if "northpole" in m[1]))


if __name__ == "__main__":
    main(sys.argv[1:])
