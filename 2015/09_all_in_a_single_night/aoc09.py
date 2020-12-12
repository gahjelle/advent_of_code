"""All in a Single Night

Advent of Code 2015, day 9
Solution by Geir Arne Hjelle, 2016-12-06
"""
import pathlib
import sys
import itertools


def read_distances(file_path):
    distances = {}
    with open(file_path, mode="r") as fid:
        for line in fid:
            places, distance = line.split("=")
            place_a, place_b = [p.strip() for p in places.split("to")]
            distances.setdefault(place_a, {})[place_b] = int(distance)
            distances.setdefault(place_b, {})[place_a] = int(distance)
    return distances


def find_route_distances(distances):
    routes = {}
    for route in itertools.permutations(distances.keys()):
        routes[", ".join(route)] = sum(
            distances[f][t] for f, t in zip(route[:-1], route[1:])
        )
    return routes


def main(args):
    """Solve the problem for all file paths"""
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        solve(file_path)


def solve(file_path):
    """Solve the problem for one file path"""
    print(f"\n{file_path}:")
    distances = read_distances(file_path)
    routes = find_route_distances(distances)
    sorted_routes = sorted(routes.items(), key=lambda t: t[1])

    print("Shortest route is {t[1]}:\n  {t[0]}".format(t=sorted_routes[0]))
    print("Longest route is {t[1]}:\n  {t[0]}".format(t=sorted_routes[-1]))


if __name__ == "__main__":
    main(sys.argv[1:])
