"""A maze of twisty little cubicles

Advent of Code 2016, day 13
Solution by Geir Arne Hjelle, 2017-05-28
"""
# Standard library imports
import itertools
import sys

DIRECTIONS = ((1, 0), (-1, 0), (0, 1), (0, -1))


def is_wall(puzzle_id, x, y):
    if x < 0 or y < 0:
        return True

    xy_sum = puzzle_id + x*x + 3*x + 2*x*y + y + y*y
    return '{:b}'.format(xy_sum).count('1') % 2 == 1


def find_path(puzzle_id, start, goal):
    locations = {start}
    paths = [(start, {start})]
    for step in itertools.count(1):
        new_paths = list()
        for path in paths:
            head, visited = path
            for direction in DIRECTIONS:
                next_head = head[0] + direction[0], head[1] + direction[1]
                if next_head in visited or is_wall(puzzle_id, *next_head):
                    continue
                new_paths.append((next_head, visited | {next_head}))
                locations.add(next_head)

                if next_head == goal:
                    return visited | {next_head}

        paths = new_paths
        if step == 50:
            print('Step {:3d}: {:8d} locations'.format(step, len(locations)))


def plot_house(puzzle_id, path):
    max_x = max(p[0] for p in path) + 2
    max_y = max(p[1] for p in path) + 2

    for y in range(max_y):
        for x in range(max_x):
            if is_wall(puzzle_id, x, y):
                print('#', end='')
            else:
                if (x, y) in path:
                    print('O', end='')
                else:
                    print('.', end='')
        print('\n', end='')


def main():
    for filename in sys.argv[1:]:
        print('\n{}:'.format(filename))
        with open(filename, mode='r') as fid:
            for line in fid:
                puzzle_id, goal_x, goal_y = [int(f) for f in line.split()]
                path = find_path(puzzle_id, (1, 1), (goal_x, goal_y))
                plot_house(puzzle_id, path)
                print('{} steps'.format(len(path - {(1, 1)})))


if __name__ == '__main__':
    main()
