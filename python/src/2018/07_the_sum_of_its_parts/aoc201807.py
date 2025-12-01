"""AoC 7, 2018: The Sum of Its Parts."""

# Standard library imports
import collections
import pathlib
import sys

# Third party imports
import parse

DEPS_PATTERN = parse.compile(
    "Step {first} must be finished before step {next} can begin."
)


def parse_data(puzzle_input):
    """Parse input."""
    dependencies = collections.defaultdict(set)
    for line in puzzle_input.split("\n"):
        if match := DEPS_PATTERN.parse(line):
            dependencies[match["next"]].add(match["first"])
    return dependencies


def part1(dependencies):
    """Solve part 1."""
    return "".join(find_step_order(dependencies))


def part2(dependencies, num_workers=5, basetime=60):
    """Solve part 2."""
    return time_all_steps(dependencies, num_workers, basetime)


def find_step_order(dependencies):
    """Find the order of the steps"""
    remaining = set(dependencies) | set.union(*dependencies.values())
    while remaining:
        next_step = sorted(
            remaining
            - {step for step, deps in dependencies.items() if deps & remaining}
        )[0]
        remaining = remaining - {next_step}
        yield next_step


def time_all_steps(dependencies, num_workers, basetime):
    """Build the sleigh and report the time taken"""
    remaining = set(dependencies) | set.union(*dependencies.values())
    time_per_step = {step: ord(step) - 64 + basetime for step in remaining}
    total_time = 0
    workers = {worker: ("", 0) for worker in range(num_workers)}
    while remaining:
        # Add available steps to idle workers
        next_steps = sorted(
            remaining
            - {step for step, deps in dependencies.items() if deps & remaining}
            - {step for step, _ in workers.values() if step}
        )
        workers = workers | {
            worker: (step, time_per_step[step])
            for step, worker in zip(
                next_steps,
                [worker for worker, (step, _) in workers.items() if not step],
            )
        }

        # Finish the next step
        time_step = min(time for step, time in workers.values() if step)
        total_time += time_step
        workers = workers | {
            worker: (step, time - time_step)
            for worker, (step, time) in workers.items()
            if step
        }

        # Report steps done and set workers idle again
        for worker, step in [
            (worker, step)
            for worker, (step, time) in workers.items()
            if step and time == 0
        ]:
            remaining = remaining - {step}
            workers = workers | {worker: ("", 0)}

    return total_time


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
