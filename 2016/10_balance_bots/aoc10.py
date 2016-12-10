"""Balance Bots

Advent of Code 2016, day 10
Solution by Geir Arne Hjelle, 2016-12-10
"""
from pprint import pprint
import sys

MICROCHIPS = dict(bot=dict(), output=dict())


def add(value, target, name):
    if target == 'bot':
        add_to_bot(name, value)
    else:
        MICROCHIPS['output'].setdefault(name, list()).append(value)


def add_to_bot(bot, value):
    MICROCHIPS['bot'].setdefault(bot, dict()).setdefault('all', list()).append(value)
    if len(MICROCHIPS['bot'][bot]['all']) >= 2:
        MICROCHIPS['bot'][bot]['low'] = min(MICROCHIPS['bot'][bot]['all'])
        MICROCHIPS['bot'][bot]['high'] = max(MICROCHIPS['bot'][bot]['all'])


def give_microchips(instructions):
    for bot, (low, high) in instructions.copy().items():
        if bot in MICROCHIPS['bot'] and 'low' in MICROCHIPS['bot'][bot]:
            print('Bot {b:3d} gives value-{v[low]} chip to {low} and value-{v[high]} chip to {high}'
                  ''.format(b=bot, v=MICROCHIPS['bot'][bot], low='{:6s} {:3d}'.format(*low),
                            high='{:6s} {:3d}'.format(*high)))
            add(MICROCHIPS['bot'][bot]['low'], *low)
            add(MICROCHIPS['bot'][bot]['high'], *high)
            del instructions[bot]


def parse_instructions(instructions):
    give_instructions = dict()
    for instruction in instructions:
        tokens = instruction.split()
        if instruction.startswith('value'):
            value, bot = int(tokens[1]), int(tokens[5])
            add_to_bot(bot, value)
        else:
            give_instructions[int(tokens[1])] = (tokens[5], int(tokens[6])), (tokens[10], int(tokens[11]))

    return give_instructions


def main():
    filename = sys.argv[1]
    print('\n{}:'.format(filename))
    with open(filename, mode='r') as fid:
        instructions = parse_instructions(i.strip() for i in fid)

    while instructions:
        give_microchips(instructions)

    outputs = [v[0] for k, v in sorted(MICROCHIPS['output'].items())]
    print('The first three outputs are {o[0]}, {o[1]} and {o[2]}. Their product is {p}'
          ''.format(o=outputs, p=outputs[0] * outputs[1] * outputs[2]))


if __name__ == '__main__':
    main()
