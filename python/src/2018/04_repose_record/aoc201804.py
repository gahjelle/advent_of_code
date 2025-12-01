"""AoC 4, 2018: Repose Record."""

# Standard library imports
import pathlib
import sys

# Third party imports
import parse

TIMESTAMP = "[{date:%Y-%m-%d} {time:%H:%M}] "
BEGINS_SHIFT = parse.compile(TIMESTAMP + "Guard #{guard:d} begins shift")
FALLS_ASLEEP = parse.compile(TIMESTAMP + "falls asleep")
WAKES_UP = parse.compile(TIMESTAMP + "wakes up")


def parse_data(puzzle_input):
    """Parse input."""
    guards = {}
    for line in sorted(puzzle_input.split("\n")):
        if match := BEGINS_SHIFT.parse(line):
            sleep_schedule = guards.setdefault(match["guard"], {})
        elif match := FALLS_ASLEEP.parse(line):
            start_min = time.minute if (time := match["time"]).hour == 0 else 0
        elif match := WAKES_UP.parse(line):
            end_min = time.minute if (time := match["time"]).hour == 0 else 60
            for minute in range(start_min, end_min):
                sleep_schedule.setdefault(minute, 0)
                sleep_schedule[minute] += 1
    return guards


def part1(guards):
    """Solve part 1."""
    _, sleeper = max(
        (sum(asleep.values()), guard) for guard, asleep in guards.items() if asleep
    )
    _, minute = max((count, minute) for minute, count in guards[sleeper].items())
    return sleeper * minute


def part2(guards):
    """Solve part 2."""
    _, sleeper = max(
        (max(asleep.values()), guard) for guard, asleep in guards.items() if asleep
    )
    _, minute = max((count, minute) for minute, count in guards[sleeper].items())
    return sleeper * minute


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
