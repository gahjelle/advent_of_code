"""Explosives in Cyberspace

Advent of Code 2016, day 9
Solution by Geir Arne Hjelle, 2016-12-09
"""
import sys


def find_tokens(string, iterate):
    tokens = list()
    uncompressed = list()
    s_iter = iter(string.strip())
    for c in s_iter:
        if c != '(':
            uncompressed.append(c)
            continue

        marker = list()
        while c != ')':
            c = next(s_iter)
            marker.append(c)
        num_chars, repeat = [int(n) for n in ''.join(marker[:-1]).split('x')]

        data = ''.join(next(s_iter) for i in range(num_chars))
        if '(' in data and iterate:
            tokens.append((repeat, find_tokens(data, True)))
        else:
            tokens.append(repeat * len(data))

    return tokens + [(1 * len(uncompressed))]


def unwrap_tokens(tokens):
    if not any(isinstance(e, tuple) for e in tokens):
        return sum(tokens)

    return unwrap_tokens([e[0] * unwrap_tokens(e[1]) if isinstance(e, tuple) else e for e in tokens])


def main():
    for filename in sys.argv[1:]:
        print('\n{}:'.format(filename))
        with open(filename, mode='r') as fid:
            for line in fid:
                tokens = find_tokens(line.strip(), False)
                print('{:<40s} - Method one: {}'.format(line.strip()[:40], unwrap_tokens(tokens)))
                tokens = find_tokens(line.strip(), True)
                print('{:<40s} - Method two: {}'.format(line.strip()[:40], unwrap_tokens(tokens)))


if __name__ == '__main__':
    main()
