"""No time for a Taxi Cab

Advent of Code 2016, day 1
Solution by Geir Arne Hjelle, 2016-12-03
"""
import sys

TURNS = {'N': {'R': 'E', 'L': 'W'},
         'E': {'R': 'S', 'L': 'N'},
         'S': {'R': 'W', 'L': 'E'},
         'W': {'R': 'N', 'L': 'S'},
         }

MOVES = {'N': lambda p, d: (p[0], p[1] + d),
         'E': lambda p, d: (p[0] + d, p[1]),
         'S': lambda p, d: (p[0], p[1] - d),
         'W': lambda p, d: (p[0] - d, p[1]),
         }

VISITED = set()


def find_distance(instructions):
    position = (0, 0)
    direction = 'N'
    for instruction in instructions:
        turn = instruction[0]
        distance = int(instruction[1:])
        direction = TURNS[direction][turn]
        position = visit(position, direction, distance)

#        print(instruction, turn, distance, direction, position)
    print('Ended at {} which is {} blocks away'.format(position, sum(abs(c) for c in position)))


def visit(position, direction, distance):
    for counter in range(distance):
        position = MOVES[direction](position, 1)
        if position in VISITED:
            print('Already visited {} which is {} blocks away'.format(position, sum(abs(c) for c in position)))
        VISITED.add(position)

    return position


def main():
    for filename in sys.argv[1:]:
        with open(filename, mode='r') as fid:
            for line in fid:
                find_distance(i.strip() for i in line.split(','))


if __name__ == '__main__':
    main()
