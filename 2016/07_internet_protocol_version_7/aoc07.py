"""Internet Protocol Version 7

Advent of Code 2016, day 7
Solution by Geir Arne Hjelle, 2016-12-07
"""
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
    good, bad = '---'.join(tokens[::2]), '---'.join(tokens[1::2])
    return any(bab in bad for bab in find_aba(good))


def find_aba(string):
    for t in zip(string[:-2], string[1:-1], string[2:]):
        if t[0] == t[2] and t[0] != t[1]:
            yield t[1] + t[0] + t[1]


def main():
    for filename in sys.argv[1:]:
        print('\n{}:'.format(filename))
        with open(filename, mode='r') as fid:
            tokens = [l.strip().replace('[', ' ').replace(']', ' ').split() for l in fid]

        print('{} IPs support TLS'.format(sum(supports_tls(t) for t in tokens)))
        print('{} IPs support SSL'.format(sum(supports_ssl(t) for t in tokens)))

if __name__ == '__main__':
    main()
