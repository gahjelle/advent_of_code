"""Tests for AoC 11, 2022: Monkey in the Middle."""

# Standard library imports
import pathlib

# Third party imports
import aoc202211
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc202211.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == {
        0: {
            "items": [79, 98],
            "operation": "* 19",
            "operate": example1[0]["operate"],
            "divisible_by": 23,
            "to_monkey": (3, 2),
        },
        1: {
            "items": [54, 65, 75, 74],
            "operation": "+ 6",
            "operate": example1[1]["operate"],
            "divisible_by": 19,
            "to_monkey": (0, 2),
        },
        2: {
            "items": [79, 60, 97],
            "operation": "^2",
            "operate": example1[2]["operate"],
            "divisible_by": 13,
            "to_monkey": (3, 1),
        },
        3: {
            "items": [74],
            "operation": "+ 3",
            "operate": example1[3]["operate"],
            "divisible_by": 17,
            "to_monkey": (1, 0),
        },
    }


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202211.part1(example1) == 10_605


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc202211.part2(example1) == 2_713_310_158
