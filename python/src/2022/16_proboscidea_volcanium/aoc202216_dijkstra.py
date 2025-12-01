"""AoC 16, 2022: Proboscidea Volcanium."""

# Standard library imports
import collections
import heapq
import pathlib
import sys

# Third party imports
import parse

PATTERNS = [
    parse.compile(
        "Valve {valve} has flow rate={rate:d}; tunnel leads to valve {valves}"
    ),
    parse.compile(
        "Valve {valve} has flow rate={rate:d}; tunnels lead to valves {valves}"
    ),
]


def parse_data(puzzle_input):
    """Parse input."""
    return prune_graph(dict(parse_valve(line) for line in puzzle_input.split("\n")))


def parse_valve(line):
    """Parse one line of input describing one valve.

    ## Examples:

    >>> parse_valve("Valve PT has flow rate=18; tunnel leads to valve GS")
    ('PT', (18, ['GS']))
    >>> parse_valve("Valve KE has flow rate=21; tunnels lead to valves ES, SQ, FS")
    ('KE', (21, ['ES', 'SQ', 'FS']))
    """
    if not any((match := pattern.parse(line)) for pattern in PATTERNS):
        raise ValueError(f"bad input: {line}")
    return match["valve"], (match["rate"], match["valves"].split(", "))


def prune_graph(valves):
    """Prune the graph to only keep the functioning valves.

    The AA valve is also kept since it's the starting point.

    ## Example:

    >>> valves = {"AA": (0, ["B", "C"]), "B": (3, ["AA", "D"]), "C": (5, ["AA"]), "D": (0, ["B", "E"]), "E": (7, ["D"])}
    >>> prune_graph(valves)
    {'AA': (0, {'B': 1, 'C': 1, 'E': 3}), 'B': (3, {'C': 2, 'E': 2}), 'C': (5, {'B': 2, 'E': 4}), 'E': (7, {'B': 2, 'C': 4})}
    """
    operational = [valve for valve, (rate, _) in valves.items() if rate > 0]
    paths = {
        node: bfs({valve: tunnels for valve, (_, tunnels) in valves.items()}, node)
        for node in valves
    }
    return {
        valve: (
            rate,
            {tunnel: paths[valve][tunnel] for tunnel in operational if tunnel != valve},
        )
        for valve, (rate, _) in valves.items()
        if rate != 0 or valve == "AA"
    }


def bfs(graph, start):
    """Find the shortest paths from the start node in a small graph."""
    queue = collections.deque([(0, start)])
    paths = {}
    while queue:
        distance, node = queue.popleft()
        if node in paths:
            continue
        paths[node] = distance
        for neighbor in graph[node]:
            queue.append((distance + 1, neighbor))
    return paths


def part1(graph):
    """Solve part 1."""
    queue = collections.deque([(0, 0, "AA", set())])
    max_flow = 0

    while queue:
        minute, flow, current, open = queue.popleft()
        _, neighbors = graph[current]

        for neighbor in set(neighbors) - open:
            if neighbors[neighbor] < 30 - minute:
                new_flow = flow + graph[neighbor][0] * (
                    29 - minute - neighbors[neighbor]
                )
                if new_flow > max_flow:
                    max_flow = new_flow
                queue.append(
                    (
                        minute + 1 + neighbors[neighbor],
                        new_flow,
                        neighbor,
                        open | {neighbor},
                    )
                )
    return max_flow


def part2(graph):
    """Solve part 2."""
    queue = [(0, 4, 4, "AA", "AA", set())]
    heapq.heapify(queue)
    max_flow = 0

    while queue:
        neg_flow, my_minute, elephant_minute, me, elephant, open = heapq.heappop(queue)

        _, neighbors = graph[me]
        for neighbor in set(neighbors) - open:
            if neighbors[neighbor] < 30 - my_minute:
                new_flow = neg_flow - graph[neighbor][0] * (
                    29 - my_minute - neighbors[neighbor]
                )
                if new_flow < max_flow:
                    print(-new_flow)
                    max_flow = new_flow
                heapq.heappush(
                    queue,
                    (
                        (
                            new_flow,
                            my_minute + 1 + neighbors[neighbor],
                            elephant_minute,
                            neighbor,
                            elephant,
                            open | {neighbor},
                        )
                    ),
                )
        _, neighbors = graph[elephant]
        for neighbor in set(neighbors) - open:
            if neighbors[neighbor] < 30 - elephant_minute:
                new_flow = neg_flow - graph[neighbor][0] * (
                    29 - elephant_minute - neighbors[neighbor]
                )
                if new_flow < max_flow:
                    print(-new_flow)
                    max_flow = new_flow
                heapq.heappush(
                    queue,
                    (
                        (
                            new_flow,
                            my_minute,
                            elephant_minute + 1 + neighbors[neighbor],
                            me,
                            neighbor,
                            open | {neighbor},
                        )
                    ),
                )
    return -max_flow


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().rstrip())
        print("\n".join(str(solution) for solution in solutions))
