"""Like a Rogue

Advent of Code 2016, day 18
Solution by Geir Arne Hjelle, 2017-05-28
"""

# Standard library imports
import pathlib
import sys

TRAPS = {"^^.", ".^^", "^..", "..^"}


def next_row(row):
    new_tiles = list()
    for tiles in zip("." + row, row, row[1:] + "."):
        new_tiles.append("^" if "".join(tiles) in TRAPS else ".")

    return "".join(new_tiles)


def map_room(first_row, num_rows):
    rows = [first_row]
    while len(rows) < num_rows:
        rows.append(next_row(rows[-1]))

    if "--draw" in sys.argv and num_rows < 1000:
        print("\n".join(rows))

    return rows


def main(args):
    """Solve the problem for all file paths"""
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        solve(file_path)


def solve(file_path):
    """Solve the problem for one file path"""
    print(f"\n{file_path}:")
    with file_path.open(mode="r") as fid:
        for line in fid:
            num_rows, first_row = line.strip().split()
            rows = map_room(first_row, int(num_rows))
            num_safe = sum(r.count(".") for r in rows)
            print(f"{num_safe} safe tiles in {num_rows} rows")


if __name__ == "__main__":
    main(sys.argv[1:])
