"""Advent of Code day 11, 2025: Reactor."""

import functools


def parse_data(puzzle_input: str) -> dict[str, list[str]]:
    """Parse puzzle input."""
    return {
        device: outputs.split()
        for line in puzzle_input.splitlines()
        for device, outputs in [line.split(":")]
    }


def part1(data: dict[str, list[str]]) -> int:
    """Solve part 1."""

    @functools.cache
    def find_paths(start: str, target: str = "out") -> int:
        if start == target:
            return 1
        return sum(find_paths(start=node, target=target) for node in data[start])

    return find_paths(start="you", target="out")


def part2(data: dict[str, list[str]]) -> int:
    """Solve part 2"""

    @functools.cache
    def find_paths(
        start: str, fft: bool = False, dac: bool = False, target: str = "out"
    ):
        if start == target:
            return 1 if fft and dac else 0
        return sum(
            find_paths(
                start=node,
                fft=fft or node == "fft",
                dac=dac or node == "dac",
                target=target,
            )
            for node in data[start]
        )

    return find_paths(start="svr", target="out")
