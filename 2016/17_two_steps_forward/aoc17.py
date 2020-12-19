"""Two Steps Forward

Advent of Code 2016, day 17
Solution by Geir Arne Hjelle, 2016-12-17
"""
# Standard library imports
import hashlib
import sys

DIRECTION = dict(U=(0, -1), D=(0, 1), L=(-1, 0), R=(1, 0))


def find_path(seed, longest=False):
    states = [('', (0, 0))]
    max_length = None

    while True:
        path, pos = states.pop(0)
        for step in generate_directions(seed + path):
            new_pos = tuple(p + d for p, d in zip(pos, DIRECTION[step]))
            if 0 <= new_pos[0] < 4 and 0 <= new_pos[1] < 4:
                if new_pos == (3, 3):
                    if longest:
                        max_length = len(path + step)
                    else:
                        return path + step
                else:
                    states.append((path + step, new_pos))
        if not states:
            return max_length


def generate_directions(seed):
    md5 = hashlib.md5()
    md5.update(bytes(seed, encoding='utf-8'))
    digest = md5.hexdigest()
    for char, step in zip(digest, 'UDLR'):
        if char in 'bcdef':
            yield step


def main():
    for filename in sys.argv[1:]:
        print('\n{}:'.format(filename))
        with open(filename, mode='r') as fid:
            for line in fid:
                passcode = line.strip()
                print('Passcode: {}'.format(passcode))
                print('  The shortest path is {}'.format(find_path(line.strip())))
                print('  The longest path is {} steps'.format(find_path(line.strip(), longest=True)))


if __name__ == '__main__':
    main()
