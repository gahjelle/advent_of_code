"""Advent of Code day 10, 2025: Factory."""

import collections

import numpy as np
from scipy.optimize import linprog

type LightDiagram = int
type Button = list[int]
type Joltage = list[int]
type Machine = tuple[LightDiagram, list[Button], Joltage]


def parse_data(puzzle_input: str) -> list[Machine]:
    """Parse puzzle input."""
    return [parse_machine(line) for line in puzzle_input.splitlines()]


def parse_machine(line: str) -> Machine:
    """Parse one machine."""
    light_diagram, *buttons, joltage = line.split()
    return (
        int(
            "".join("01"[char == "#"] for char in light_diagram.strip("[]")[::-1]),
            base=2,  # Convert light diagram to binary number
        ),
        [
            [int(number) for number in button.strip("()").split(",")]
            for button in buttons
        ],
        [int(number) for number in joltage.strip("{}").split(",")],
    )


def part1(data: list[Machine]) -> int:
    """Solve part 1."""
    return sum(configure_light_diagram(machine) for machine in data)


def part2(data: list[Machine]) -> int:
    """Solve part 2."""
    return sum(configure_joltage(machine) for machine in data)


def configure_light_diagram(machine: Machine) -> int:
    """Find minimum number of presses to configure the light diagram."""
    target, buttons, _ = machine
    button_bits = [sum(2**toggle for toggle in button) for button in buttons]
    queue = collections.deque([(0, 0)])
    seen = set()
    while queue:
        num_presses, light_diagram = queue.popleft()
        if light_diagram == target:
            return num_presses
        if light_diagram in seen:
            continue
        seen.add(light_diagram)

        for button in button_bits:
            new_diagram = light_diagram ^ button
            if new_diagram not in seen:
                queue.append((num_presses + 1, new_diagram))
    return 0


def configure_joltage(machine: Machine) -> int:
    """Find minimum number of presses to set the correct joltage.

    Use the scipy linprog optimizer with integer requirements.
    """
    _, buttons, target = machine
    coeffs = [1 for _ in buttons]
    B = np.array(
        [
            [1 if idx in button else 0 for idx in range(len(target))]
            for button in buttons
        ]
    ).T
    integer = [1 for _ in coeffs]
    minimized = linprog(c=coeffs, A_eq=B, b_eq=target, integrality=integer)
    return round(minimized.fun)
