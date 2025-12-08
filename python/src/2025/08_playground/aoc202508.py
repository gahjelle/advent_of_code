"""AoC day 8, 2025: Playground."""

import collections
import math
from collections.abc import Generator

type Coordinate = tuple[int, int, int]
type DistanceMatrix = list[tuple[int, int, int]]


def parse_data(puzzle_input: str) -> tuple[list[Coordinate], DistanceMatrix]:
    """Parse puzzle input."""
    junctions = [
        (int(x), int(y), int(z))
        for line in puzzle_input.splitlines()
        for x, y, z in [line.split(",")]
    ]
    distances = sorted(
        ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2, first, second)
        for first, (x1, y1, z1) in enumerate(junctions)
        for second, (x2, y2, z2) in enumerate(junctions)
        if first < second
    )
    return junctions, distances


def part1(data: tuple[list[Coordinate], DistanceMatrix]) -> int:
    """Solve part 1."""
    junctions, distances = data
    num = 1000 if len(junctions) > 20 else 10  # Handle main and example input

    circuits = {}
    for connection, *_ in add_to_circuit(distances[:num]):
        circuits |= connection

    counts = collections.Counter(circuits.values())
    return math.prod(count for _, count in counts.most_common(3))


def part2(data: tuple[list[Coordinate], DistanceMatrix]) -> int:
    """Solve part 2."""
    junctions, distances = data

    circuits = {idx: None for idx, _ in enumerate(junctions)}
    for connection, first, second in add_to_circuit(distances):
        circuits |= connection
        if len(set(circuits.values())) == 1:
            (x1, _, _), (x2, _, _) = junctions[first], junctions[second]
            return x1 * x2
    return 0


def add_to_circuit(
    distances: DistanceMatrix,
) -> Generator[tuple[dict[int, int], int, int]]:
    """Add junction boxes to circuits, one pair at a time."""
    circuits: dict[int, int] = {}
    for _, first, second in distances:
        circuit_1 = circuits.get(first)
        circuit_2 = circuits.get(second)
        match (circuit_1, circuit_2):
            case (None, None):
                new_circuit = max(circuits.values(), default=0) + 1
                yield (
                    (connection := {first: new_circuit, second: new_circuit}),
                    first,
                    second,
                )
            case (first_circuit, None):
                yield (connection := {second: first_circuit}), first, second
            case (None, second_circuit):
                yield (connection := {first: second_circuit}), first, second
            case (first_circuit, second_circuit):
                yield (
                    (
                        connection := {
                            idx: first_circuit
                            for idx, circuit in circuits.items()
                            if circuit == second_circuit
                        }
                    ),
                    first,
                    second,
                )
        circuits |= connection
