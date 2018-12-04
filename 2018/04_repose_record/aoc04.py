"""Repose Record

Advent of Code 2018, day 4
Solution by Geir Arne Hjelle, 2018-12-04
"""
from datetime import datetime
import sys

import numpy as np


def parse_records(records):
    guards = dict()
    for record in records:
        time = datetime.strptime(record[1:17], "%Y-%m-%d %H:%M")
        action = record[19:].lower()
        if action.startswith("guard "):
            guard = action.split()[1]
            guards.setdefault(guard, np.zeros(60, dtype=int))
        elif action.startswith("falls asleep"):
            start_min = time.minute if time.hour == 0 else 0
        elif action.startswith("wakes up"):
            end_min = time.minute if time.hour == 0 else 60
            guards[guard][start_min:end_min] += 1

    return guards


def strategy_1(guards):
    result = list()
    for guard, sleep in guards.items():
        total_sleep = sum(sleep)
        guard_id = int(guard[1:])
        max_min = np.argmax(sleep)
        result.append((total_sleep, guard_id, max_min, guard_id * max_min))

    return max(result)


def strategy_2(guards):
    result = list()
    for guard, sleep in guards.items():
        num_sleep = max(sleep)
        guard_id = int(guard[1:])
        max_min = np.argmax(sleep)
        result.append((num_sleep, guard_id, max_min, guard_id * max_min))

    return max(result)


def main():
    for filename in sys.argv[1:]:
        if filename.startswith("--"):
            continue

        print(f"\n{filename}:")
        with open(filename, mode="r") as fid:
            records = sorted(f.strip() for f in fid)
            guards = parse_records(records)
            print(f"Strategy 1: {strategy_1(guards)}")
            print(f"Strategy 2: {strategy_2(guards)}")


if __name__ == "__main__":
    debug = print if "--debug" in sys.argv else lambda *_: None
    main()
