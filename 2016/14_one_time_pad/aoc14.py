"""One-Time Pad

Advent of Code 2016, day 14
Solution by Geir Arne Hjelle, 2016-12-14
"""
import hashlib
import itertools
import sys


def generate_md5_numbers(salt, stretch=0):
    for counter in itertools.count(start=0, step=1):
        if not counter % 1000:
            print('.', end='', flush=True)
        md5 = hashlib.md5()
        md5.update(bytes(salt + str(counter), encoding='utf-8'))

        for i in range(stretch):
            digest = md5.hexdigest()
            md5 = hashlib.md5()
            md5.update(bytes(digest, encoding='utf-8'))

        digest = md5.hexdigest()
        counts = [(c, len(list(g))) for c, g in itertools.groupby(digest)]
        for c, lg in [(c, lg) for c, lg in counts if lg >= 5]:
            yield counter, c, lg
            break
        for c, lg in [(c, lg) for c, lg in counts if lg >= 3]:
#            print(counter, digest, c, lg)
            yield counter, c, lg
            break

def find_onetime_pads(salt, stretch=0):
    candidates = dict()
    onetime_pads = set()
    gen_nums = iter(generate_md5_numbers(salt, stretch))

    while len(onetime_pads) < 64 or counter < sorted(onetime_pads)[63] + 1000:
        counter, char, count = next(gen_nums)
        if char in candidates:
            candidates[char] = [idx for idx in candidates[char] if counter - 1000 <= idx < counter]
        if count >= 5:
            [onetime_pads.add(candidate) for candidate in candidates[char]]
        candidates.setdefault(char, list()).append(counter)

    return max(sorted(onetime_pads)[:64])


def main():
    for filename in sys.argv[1:]:
        print('\n{}:'.format(filename))
        with open(filename, mode='r') as fid:
            for line in fid:
                print('   Index {} gives the 64th key'.format(find_onetime_pads(line.strip())))
                print('   Index {} gives the 64th key with stretching'.format(find_onetime_pads(line.strip(), 2016)))


if __name__ == '__main__':
    main()
