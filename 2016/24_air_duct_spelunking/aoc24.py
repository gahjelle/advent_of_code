"""Air Duct Spelunking

Advent of Code 2016, day 24
Solution by Geir Arne Hjelle, 2021-01-05
"""

# Standard library imports
import enum
import heapq
import pathlib
import sys
from collections import deque

# Third party imports
import colorama
import numpy as np
from colorama import Cursor, Fore

colorama.init(autoreset=True)
debug = print if "--debug" in sys.argv else lambda *_: None


class Block(enum.IntEnum):
    WALL = 99
    SPACE = 100
    START = 0
    VISITED = 101


STR2BLOCK = {"#": Block.WALL, ".": Block.SPACE, "0": Block.START}
BLOCK2DRAW = {
    Block.WALL: f"{Fore.LIGHTBLACK_EX}█",
    Block.SPACE: " ",
    Block.START: f"{Fore.GREEN}▪",
    Block.VISITED: f"{Fore.RED}▣",
}


def parse_maze(lines):
    return np.array([[STR2BLOCK.get(b, ord(b) - 48) for b in line] for line in lines])


def draw(maze):
    print(
        Cursor.POS(1, 5)
        + "\n".join(
            "".join(BLOCK2DRAW.get(b, f"{Fore.YELLOW}{chr(b + 48)}") for b in row)
            for row in maze
        )
    )


def set_up_pois(maze):
    """Calculate distances between all Points of Interest"""
    pois = [b for b in maze.flatten() if b < Block.WALL]

    distances = {}
    for poi in pois:
        distances[poi] = shortest_paths(
            maze, start=poi, targets=[p for p in pois if p != poi]
        )

    return distances


def shortest_paths(maze, start, targets):
    """Find the shortest path from the start block to all other target blocks"""
    start_idx = tuple(i[0] for i in np.where(maze == start))

    # Initialize distances with a representative of infinity
    distances = np.full(maze.shape, np.prod(maze.shape))
    target_distances = {}

    # Represent each block as an index-distance tuple
    queue = deque([(start_idx, 0)])
    while queue:
        idx, distance = queue.popleft()
        if distance >= distances[idx]:
            continue

        # We found one of the targets, do we have them all?
        if maze[idx] in targets:
            target_distances[maze[idx]] = distance
            if len(target_distances) == len(targets):
                return target_distances

        # Queue up allowed moves from here
        distances[idx] = distance
        for move in ((-1, 0), (0, -1), (1, 0), (0, 1)):
            next_idx = (idx[0] + move[0], idx[1] + move[1])
            if maze[next_idx] != Block.WALL:
                queue.append((next_idx, distance + 1))


def visit_pois(distances, start, return_to_start):
    """Visit all Points of Interest"""
    num_pois = len(distances)
    if return_to_start:
        path_heads = [(d, (p,)) for p, d in distances[start].items()]
        heapq.heapify(path_heads)
    else:
        path_heads = [(0, (start,))]

    while path_heads:
        distance, (*head, current_poi) = heapq.heappop(path_heads)
        if len(head) + 1 == num_pois:
            return distance, (*head, current_poi)

        for next_poi, distance_to_next in distances[current_poi].items():
            if next_poi not in head and (
                next_poi != start or len(head) + 2 == num_pois  # Force start to be last
            ):
                heapq.heappush(
                    path_heads,
                    (distance + distance_to_next, (*head, current_poi, next_poi)),
                )


def main(args):
    """Solve the problem for all file paths"""
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        solve(file_path)


def solve(file_path):
    """Solve the problem for one file path"""
    print(f"\n{file_path}:")
    maze = parse_maze(file_path.read_text().strip().split("\n"))
    poi_distances = set_up_pois(maze)

    if "--draw" in sys.argv:
        draw(maze)

    # Part 1
    distance, path = visit_pois(poi_distances, start=0, return_to_start=False)
    print(f"The shortest path is {'-'.join(str(p) for p in path)} ({distance} steps)")

    # Part 2
    distance, path = visit_pois(poi_distances, start=0, return_to_start=True)
    print(f"The shortest path is 0-{'-'.join(str(p) for p in path)} ({distance} steps)")


if __name__ == "__main__":
    main(sys.argv[1:])
