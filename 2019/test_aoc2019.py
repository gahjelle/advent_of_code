#!/usr/bin/env python
"""Test outputs of Advent of Code puzzle solutions"""
import importlib
import pathlib
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent
PUZZLES = sorted(p.parent.name for p in PUZZLE_DIR.rglob("**/output.txt"))


@pytest.mark.parametrize("puzzle", PUZZLES)
def test_puzzle(puzzle, capsys):
    # Import puzzle
    puzzle_mod = importlib.import_module(f"{puzzle}.aoc{puzzle[:2]}")
    puzzle_func = getattr(puzzle_mod, "main")

    # Capture output from running puzzle on input
    puzzle_func([str(PUZZLE_DIR / puzzle / "input.txt")])
    stdout, stderr = capsys.readouterr()

    # Compare to expected output
    actual = stdout.strip().split("\n")[1:]
    expected = (PUZZLE_DIR / puzzle / "output.txt").read_text().strip().split("\n")[1:]
    assert actual == expected
