"""Tests for AoC 16, 2020: Ticket Translation"""

# Standard library imports
import pathlib

# Third party imports
import aoc202016
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc202016.parse(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc202016.parse(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == {
        "rules": {
            "class": set(range(1, 3 + 1)) | set(range(5, 7 + 1)),
            "row": set(range(6, 11 + 1)) | set(range(33, 44 + 1)),
            "seat": set(range(13, 40 + 1)) | set(range(45, 50 + 1)),
        },
        "ticket": [7, 1, 14],
        "tickets": [[7, 3, 47], [40, 4, 50], [55, 2, 20], [38, 6, 12]],
    }


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc202016.part1(example1) == 71


def test_part2_example2(example2):
    """Test part 2 on example input"""
    assert aoc202016.part2(example2) == 11 * 13
