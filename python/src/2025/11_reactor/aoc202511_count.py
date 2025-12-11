"""Advent of Code day 11, 2025: Reactor."""

import collections


def parse_data(puzzle_input: str) -> dict[str, set[str]]:
    """Parse puzzle input."""
    return {
        device: set(outputs.split())
        for line in puzzle_input.splitlines()
        for device, outputs in [line.split(":")]
    }


def part1(data: dict[str, set[str]]) -> int:
    """Solve part 1."""
    return find_paths(data, start="you", target="out")


def part2(data: dict[str, set[str]]) -> int:
    """Solve part 2.

    Calculate sub paths:

        svr -> fft -> dac -> out
        svr -> dac -> fft -> out
    """
    no_fft = {node: outs - {"fft"} for node, outs in data.items() if node != "fft"}
    no_dac = {node: outs - {"dac"} for node, outs in data.items() if node != "dac"}

    svr_fft = find_paths(no_dac, start="svr", target="fft")
    fft_dac = find_paths(data, start="fft", target="dac")
    dac_out = find_paths(no_fft, start="dac", target="out")

    svr_dac = find_paths(no_fft, start="svr", target="dac")
    dac_fft = find_paths(data, start="dac", target="fft")
    fft_out = find_paths(no_dac, start="fft", target="out")

    return svr_fft * fft_dac * dac_out + svr_dac * dac_fft * fft_out


def find_paths(graph: dict[str, set[str]], start: str, target: str) -> int:
    """Find the paths through the graph"""
    num_paths = {"out": 0, target: 1}  # target overwrites "out" when necessary
    while start not in num_paths:
        for node, outputs in graph.items():
            if node in num_paths:
                continue
            if not outputs - set(num_paths):
                num_paths |= {node: sum(num_paths[output] for output in outputs)}
    return num_paths[start]
