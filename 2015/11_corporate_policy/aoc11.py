"""Corporate Policy

Advent of Code 2015, day 11
Solution by Geir Arne Hjelle, 2016-12-10
"""
import itertools
import sys


def increment_password(password):
    if password.endswith('z'):
        return increment_password(password[:-1]) + 'a'
    return password[:-1] + chr(ord(password[-1]) + 1)


def generate_passwords(password):
    while True:
        password = increment_password(password)
        yield password


def next_password(seed):
    return next(itertools.dropwhile(lambda p: not is_valid(p), generate_passwords(seed)))


def is_valid(password):
    return not contains_iol(password) and contains_straight(password) and contains_pairs(password)


def contains_straight(password):
    for c1, c2, c3 in zip(password[:-2], password[1:-1], password[2:]):
        if ord(c2) == ord(c1) + 1 and ord(c3) == ord(c2) + 1:
            return True
    return False


def contains_iol(password):
    return any(c in password for c in 'iol')


def contains_pairs(password):
    pair_idx = list()
    for idx, (c1, c2) in enumerate(zip(password[:-1], password[1:])):
        if c1 == c2:
            pair_idx.append(idx)

    return pair_idx and max(pair_idx) - min(pair_idx) >= 2


def main():
    for filename in sys.argv[1:]:
        print('\n{}:'.format(filename))
        with open(filename, mode='r') as fid:
            for line in fid:
                password = line.strip()

                print("Santa's current password is {}".format(password))
                for _ in range(2):
                    password = next_password(password)
                    print("   Santa's next password is {}".format(password))


if __name__ == '__main__':
    main()
