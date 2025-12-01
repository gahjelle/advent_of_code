"""AoC 20, 2023: Pulse Propagation."""

# Standard library imports
import collections
import itertools
import math
import pathlib
import string
import sys


def parse_data(puzzle_input):
    """Parse input."""
    modules = {}
    for line in puzzle_input.split("\n"):
        full_name, _, targets = line.partition(" -> ")
        name = "".join(ch for ch in full_name if ch in string.ascii_letters)
        kind = full_name.removesuffix(name)
        modules[name] = (kind, targets.split(", "))
    return modules


def part1(modules):
    """Solve part 1."""
    pulses = []
    state = initial_state(modules)
    for _ in range(1000):
        state, pulse_count, _ = push_button(modules, state)
        pulses.append(pulse_count)

    return math.prod([sum(pulse) for pulse in list(zip(*pulses))])


def part2(modules):
    """Solve part 2.

    rx only has one input. That input has several conjuntion inputs. To trigger
    the pulse to rx, we need all those conjunction modules to line up. Find
    their individual cycle lengths and use LCM to find the combined cycle
    length.
    """
    (feed_to_rx,) = [name for name, (_, targets) in modules.items() if "rx" in targets]
    num_inputs = len(
        [name for name, (_, targets) in modules.items() if feed_to_rx in targets]
    )

    cycles = {}
    state = initial_state(modules)
    for count in itertools.count(start=1):
        state, _, trigger = push_button(
            modules, state, monitor=feed_to_rx, ignore=list(cycles)
        )
        if trigger:
            cycles[trigger] = count
            if len(cycles) == num_inputs:
                break

    return math.lcm(*cycles.values())


def initial_state(modules):
    """Set up initial state for the given modules."""
    return {name: False for name, (kind, _) in modules.items() if kind == "%"} | {
        name: {
            input: False for input, (_, targets) in modules.items() if name in targets
        }
        for name, (kind, _) in modules.items()
        if kind == "&"
    }


def push_button(modules, state, monitor=None, ignore=None):
    """Simulate one push of a button."""
    queue = collections.deque([(("broadcaster", False, ""))])
    num_low_pulse, num_high_pulse = 0, 0

    while queue:
        module, pulse, from_module = queue.popleft()
        if pulse:
            num_high_pulse += 1
        else:
            num_low_pulse += 1

        if module == monitor and pulse and from_module not in ignore:
            return state, (num_low_pulse, num_high_pulse), from_module

        kind, targets = modules.get(module, ("X", []))
        if kind == "":
            for target in targets:
                queue.append((target, pulse, module))
        elif kind == "%":
            if pulse:
                continue
            state[module] = not state[module]
            for target in targets:
                queue.append((target, state[module], module))
        elif kind == "&":
            state[module][from_module] = pulse
            out_pulse = not all(state[module].values())
            for target in targets:
                queue.append((target, out_pulse, module))

    return state, (num_low_pulse, num_high_pulse), None


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
