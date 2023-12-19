"""AoC 19, 2023: Aplenty."""

# Standard library imports
import collections
import math
import pathlib
import sys

# Third party imports
import parse

PART_PATTERN = parse.compile("{cat}={value:d}")
WORKFLOW_PATTERN = parse.compile("{cat}{op}{value:d}:{target}")


def parse_data(puzzle_input):
    """Parse input."""
    workflows, parts = puzzle_input.split("\n\n")
    return (
        dict([parse_workflow(line) for line in workflows.split("\n")]),
        [parse_part(line) for line in parts.split("\n")],
    )


def parse_workflow(text):
    """Parse one workflow description.

    ## Example:

    >>> parse_workflow("rfg{s<537:gd,x>2440:R,A}")
    ('rfg', [('s', '<', 537, 'gd'), ('x', '>', 2440, 'R'), ('', '', 0, 'A')])
    """
    name, descriptions = text[:-1].split("{")
    workflows = []
    for description in descriptions.split(","):
        if match := WORKFLOW_PATTERN.parse(description):
            result = match.named
        else:
            result = {"cat": "", "op": "", "value": 0, "target": description}
        workflows.append(
            (result["cat"], result["op"], result["value"], result["target"])
        )
    return (name, workflows)


def parse_part(text):
    """Parse one part description.

    ## Example:

    >>> parse_part("{x=787,m=2655,a=1222,s=2876}")
    {'x': 787, 'm': 2655, 'a': 1222, 's': 2876}
    """
    categories = text[1:-1].split(",")
    return {
        m["cat"]: m["value"]
        for category in categories
        if (m := PART_PATTERN.parse(category))
    }


def part1(data):
    """Solve part 1."""
    workflows, parts = data
    accepted = []
    to_process = collections.deque([("in", part) for part in parts])

    while to_process:
        workflow, part = to_process.popleft()
        new_workflow = process(part, workflows[workflow])
        if new_workflow == "A":
            accepted.append(part)
        elif new_workflow != "R":
            to_process.append((new_workflow, part))

    return sum(sum(part.values()) for part in accepted)


def part2(data):
    """Solve part 2."""
    workflows, _ = data
    accepted = []
    to_process = collections.deque(
        [("in", {"x": (1, 4001), "m": (1, 4001), "a": (1, 4001), "s": (1, 4001)})]
    )

    while to_process:
        workflow, intervals = to_process.popleft()
        for new_workflow, new_intervals in process_intervals(
            intervals, workflows[workflow]
        ):
            if new_workflow == "A":
                accepted.append(new_intervals)
            elif new_workflow != "R":
                to_process.append((new_workflow, new_intervals))

    return sum(
        math.prod(high - low for low, high in interval.values())
        for interval in accepted
    )


def process(part, workflow):
    """Process one part through one workflow."""
    for category, op, value, target in workflow:
        if not op:
            return target
        elif op == "<" and part[category] < value:
            return target
        elif op == ">" and part[category] > value:
            return target


def process_intervals(intervals, workflow):
    """Process an interval of parts through a workflow."""
    for category, op, value, target in workflow:
        if not op:
            yield target, intervals
            continue

        low, high = intervals[category]
        if op == "<" and low < value:
            yield target, intervals | {category: (low, value)}
            intervals |= {category: (value, high)}
        if op == ">" and high > value:
            yield target, intervals | {category: (value + 1, high)}
            intervals |= {category: (low, value + 1)}


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
