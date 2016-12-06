"""All in a Single Night

Advent of Code 2015, day 9
Solution by Geir Arne Hjelle, 2016-12-06
"""
import sys
import itertools


def read_distances(filename):
    distances = dict()
    with open(filename, mode='r') as fid:
        for line in fid:
            places, distance = line.split('=')
            place_a, place_b = [p.strip() for p in places.split('to')]
            distances.setdefault(place_a, dict())[place_b] = int(distance)
            distances.setdefault(place_b, dict())[place_a] = int(distance)
    return distances


def find_route_distances(distances):
    routes = dict()
    for route in itertools.permutations(distances.keys()):
        routes[', '.join(route)] = sum(distances[f][t] for f, t in zip(route[:-1], route[1:]))
    return routes


def main():
    for filename in sys.argv[1:]:
        print('\n{}:'.format(filename))
        distances = read_distances(filename)
        routes = find_route_distances(distances)
        sorted_routes = sorted(routes.items(), key=lambda t: t[1])

        print('Shortest route is {t[1]}:\n  {t[0]}'.format(t=sorted_routes[0]))
        print('Longest route is {t[1]}:\n  {t[0]}'.format(t=sorted_routes[-1]))

if __name__ == '__main__':
    main()
