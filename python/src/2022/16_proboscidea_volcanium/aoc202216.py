"""AoC 16, 2022: Proboscidea Volcanium."""

# Standard library imports
import collections
import itertools
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
    data = prune_graph(dict(parse_valve(line) for line in puzzle_input.split("\n")))
    return (
        {valve: tunnels for valve, (_, tunnels) in data.items()},
        {valve: flow_rate for valve, (flow_rate, _) in data.items()},
    )


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


def part1(data):
    """Solve part 1."""
    return best_flow(*data, 30)


def part2(data):
    """Solve part 2."""
    graph, flows = data

    return max(
        best_flow_subgraph(graph, flows, minutes=26, valves=me)
        + best_flow_subgraph(graph, flows, minutes=26, valves=elephant)
        for me, elephant in split_valves(graph.keys())
    )


def split_valves(valves):
    """Split responsibility for the valves in two.

    ## Example:

    >>> [(me, sorted(elephant)) for me, elephant in split_valves(["A", "B", "C"])]
    [({'A'}, ['B', 'C']), ({'B'}, ['A', 'C']), ({'C'}, ['A', 'B'])]
    """
    rooms = {valve for valve in valves if valve != "AA"}

    size = len(rooms) // 2
    for me in itertools.combinations(sorted(rooms), size):
        yield set(me), rooms - set(me)


def best_flow_subgraph(graph, flows, minutes, valves):
    """Calculate the best flow in a subgraph for the given valves."""
    subgraph = {
        v: {t: d for t, d in ts.items() if t in valves}
        for v, ts in graph.items()
        if v in valves or v == "AA"
    }
    subflows = {v: fr for v, fr in flows.items() if v in valves} | {"AA": 0}
    return best_flow(subgraph, subflows, minutes)


def best_flow(graph, flows, minutes):
    """Calculate the best flow that can be achieved in the given number of minutes."""
    max_flow = 0

    queue = collections.deque([(0, 0, "AA", set(graph) - {"AA"})])
    while queue:
        minute, flow, current, closed = queue.popleft()
        steps = graph[current]

        for step in closed:
            if steps[step] >= minutes - minute:
                continue
            new_flow = flow + flows[step] * (minutes - minute - steps[step] - 1)
            queue.append((minute + 1 + steps[step], new_flow, step, closed - {step}))
            if new_flow > max_flow:
                max_flow = new_flow
    return max_flow


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
