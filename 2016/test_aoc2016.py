#!/usr/bin/env python
"""Test outputs of Advent of Code puzzle solutions"""

# Standard library imports
import importlib
import pathlib

# Third party imports
import pytest
from codetiming import Timer

PUZZLE_DIR = pathlib.Path(__file__).parent
PUZZLES = sorted(p.parent.name for p in PUZZLE_DIR.rglob("**/output.txt"))

TIME_UNITS = (("m", 60), ("s", 1), ("ms", 1e-3), ("μs", 1e-6), ("ns", 1e-9))
TIMINGS_LOG = PUZZLE_DIR / "timings.py.md"
TIMINGS_LOG.write_text("| Day | Puzzle | Python | Time |\n|:---|:---|:---|---:|\n")


def prettytime(seconds):
    """Pretty-print number of seconds"""
    for unit, threshold in TIME_UNITS:
        if seconds > threshold:
            return f"{seconds / threshold:.3f} {unit}"


@pytest.mark.parametrize("puzzle", PUZZLES)
def test_puzzle(puzzle, capsys):
    # Import puzzle
    day = puzzle[:2]
    puzzle_mod = importlib.import_module(f"{puzzle}.aoc{day}")
    puzzle_func = getattr(puzzle_mod, "main")

    # Capture output from running puzzle on input
    with Timer(logger=None) as timer:
        puzzle_func([str(PUZZLE_DIR / puzzle / "input.txt")])
    stdout, stderr = capsys.readouterr()

    # Compare to expected output
    actual = stdout.strip().split("\n")[1:]
    expected = (PUZZLE_DIR / puzzle / "output.txt").read_text().strip().split("\n")[1:]
    assert actual == expected

    # Log elapsed time
    puzzle_name = puzzle[3:].replace("_", " ").title()
    link = f"[aoc{day}.py]({puzzle}/aoc{day}.py)"
    time = prettytime(timer.last)
    with TIMINGS_LOG.open(mode="a") as fid:
        fid.write(f"| {int(day)} | {puzzle_name} | {link} | {time} |\n")
