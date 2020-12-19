"""An elephant named Joseph

Advent of Code 2016, day 19
Solution by Geir Arne Hjelle, 2017-05-28
"""
# Standard library imports
import sys
from collections import deque


def steal_left(num_elves):
    elves = deque(idx + 1 for idx in range(num_elves))

    while num_elves > 1:
        elves.append(elves.popleft())
        elves.popleft()
        num_elves -= 1

    return elves[0]


def steal_across(num_elves):
    stealers = deque(idx + 1 for idx in range(num_elves // 2))
    stealees = deque(idx + 1 for idx in range(num_elves // 2, num_elves))
    move = len(stealees) > len(stealers)

    while stealers:
        stealees.append(stealers.popleft())
        stealees.popleft()
        if move:
            stealers.append(stealees.popleft())
        move = not move

    return stealees[0]


def main():
    for filename in sys.argv[1:]:
        print('\n{}:'.format(filename))
        with open(filename, mode='r') as fid:
            for line in fid:
                print('Elf {} steals all the presents'.format(steal_left(int(line.strip()))))
                print('Elf {} steals all the presents'.format(steal_across(int(line.strip()))))


if __name__ == '__main__':
    main()
