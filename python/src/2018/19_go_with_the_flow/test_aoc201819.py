"""Tests for AoC 19, 2018: Go With The Flow."""

# Standard library imports
import pathlib

# Third party imports
import aoc201819
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc201819.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [
        ["#ip", 0],
        ["seti", 5, 0, 1],
        ["seti", 6, 0, 2],
        ["addi", 0, 1, 0],
        ["addr", 1, 2, 3],
        ["setr", 1, 0, 0],
        ["seti", 8, 0, 4],
        ["seti", 9, 0, 5],
    ]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc201819.part1(example1) == 6


@pytest.mark.skip(reason="Not implemented")
def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc201819.part2(example1) == ...
