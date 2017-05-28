"""Firewall rules

Advent of Code 2016, day 20
Solution by Geir Arne Hjelle, 2017-05-28
"""
import sys


def read_blacklist(fid):
    return sorted((int(first), int(last)) for first, last in [line.strip().split('-') for line in fid])


def find_lowest(blacklist):
    lowest = 0

    for first, last in blacklist:
        if first > lowest:
            return lowest
        if last >= lowest:
            lowest = last + 1

    return lowest


def count_allowed(blacklist):
    count = 0
    lowest = 0

    for first, last in blacklist:
        if first > lowest:
            count += first - lowest
        if last >= lowest:
            lowest = last + 1

    return count, lowest - 1   # Does not account for any IPs at the end of the interval


def main():
    for filename in sys.argv[1:]:
        print('\n{}:'.format(filename))
        with open(filename, mode='r') as fid:
            blacklist = read_blacklist(fid)
            print('Lowest available IP: {}'.format(find_lowest(blacklist)))
            print('Number of available IPs: {} (up to {})'.format(*count_allowed(blacklist)))

if __name__ == '__main__':
    main()
