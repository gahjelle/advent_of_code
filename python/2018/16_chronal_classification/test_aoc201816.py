"""Tests for AoC 16, 2018: Chronal Classification."""

# Standard library imports
import pathlib

# Third party imports
import aoc201816
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc201816.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    tests, program = example1
    assert tests == [
        ({0: 3, 1: 2, 2: 1, 3: 1}, [9, 2, 1, 2], {0: 3, 1: 2, 2: 2, 3: 1}),
        ({0: 3, 1: 2, 2: 1, 3: 1}, [9, 2, 3, 2], {0: 3, 1: 2, 2: 4, 3: 1}),
    ]
    assert program == [[9, 1, 2, 0]]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc201816.part1(example1) == 1
