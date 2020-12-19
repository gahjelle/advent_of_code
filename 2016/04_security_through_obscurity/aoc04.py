"""Security Through Obscurity

Advent of Code 2016, day 4
Solution by Geir Arne Hjelle, 2016-12-04
"""
# Standard library imports
import sys


def _parse_string(string):
    checksum = string.strip()[-6:-1]
    messages = string.strip()[:-7].split('-')
    sector_id = int(messages.pop(-1))
    message = ' '.join(messages)

    return message, sector_id, checksum

def check_room(string):
    message, sector_id, checksum = _parse_string(string)
    counter = {c: '{:04d}{}'.format(10000 - message.count(c), c) for c in set(message) if c != ' '}
    actual_checksum = ''.join(sorted(counter, key=lambda c: counter[c]))[:5]

    return sector_id if checksum == actual_checksum else 0


def decrypt_room(string):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    message, sector_id, _ = _parse_string(string)
    decrypted = list()

    for c in message:
        try:
            idx = letters.index(c)
            decrypted.append(letters[(idx + sector_id) % 26])
        except ValueError:
            decrypted.append(' ')

    return ''.join(decrypted), sector_id


def main():
    for filename in sys.argv[1:]:
        print('\n{}:'.format(filename))

        with open(filename, mode='r') as fid:
            messages = [decrypt_room(l) for l in fid if check_room(l)]

        print('\n'.join('{m[0]} ({m[1]})'.format(m=m) for m in messages))
        print('Sum of sector IDs is {}'.format(sum(m[1] for m in messages)))

if __name__ == '__main__':
    main()
