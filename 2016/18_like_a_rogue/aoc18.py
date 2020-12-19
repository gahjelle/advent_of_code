"""Like a rogue

Advent of Code 2016, day 18
Solution by Geir Arne Hjelle, 2017-05-28
"""
# Standard library imports
import sys

TRAPS = {'^^.', '.^^', '^..', '..^'}


def next_row(row):
    new_tiles = list()
    for tiles in zip('.' + row, row, row[1:] + '.'):
        new_tiles.append('^' if ''.join(tiles) in TRAPS else '.')

    return ''.join(new_tiles)


def map_room(first_row, num_rows):
    rows = [first_row]
    while len(rows) < num_rows:
        rows.append(next_row(rows[-1]))

    if num_rows < 100:
        print('\n'.join(rows))
    print('{} safe tiles in {} rows'.format(sum(r.count('.') for r in rows), num_rows))


def main():
    for filename in sys.argv[1:]:
        print('\n{}:'.format(filename))
        with open(filename, mode='r') as fid:
            for line in fid:
                num_rows, first_row = line.strip().split()
                map_room(first_row, int(num_rows))


if __name__ == '__main__':
    main()
