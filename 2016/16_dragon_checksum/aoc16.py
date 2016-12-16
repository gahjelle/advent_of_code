"""Dragon Checksum

Advent of Code 2016, day 16
Solution by Geir Arne Hjelle, 2016-12-16
"""
import sys


def update_security_system(length, initial_state):
    string = generate_string(length, initial_state)
    return calculate_checksum(string)


def generate_string(length, initial_state):
    string = [int(c) for c in initial_state]
    while len(string) < length:
        string += [0] + [1 - c for c in string[::-1]]

    return string[:length]


def calculate_checksum(string):
    while not len(string) % 2:
        checksum = list()
        for c1, c2 in zip(string[::2], string[1::2]):
            if c1 == c2:
                checksum.append(1)
            else:
                checksum.append(0)
        string = checksum
    return ''.join(str(c) for c in string)


def main():
    for filename in sys.argv[1:]:
        print('\n{}:'.format(filename))
        with open(filename, mode='r') as fid:
            for line in fid:
                length, initial_state = line.strip().split()
                checksum = update_security_system(int(length), initial_state)
                print('The checksum of the disk with length {} is {}'.format(length, checksum))


if __name__ == '__main__':
    main()
