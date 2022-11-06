"""Tests for AoC 15, 2015: Science for Hungry People"""

# Standard library imports
import pathlib

# Third party imports
import aoc201515
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc201515.parse(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == [
        {
            "capacity": -1,
            "durability": -2,
            "flavor": 6,
            "texture": 3,
            "calories": 8,
        },
        {
            "capacity": 2,
            "durability": 3,
            "flavor": -2,
            "texture": -1,
            "calories": 3,
        },
    ]


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc201515.part1(example1) == 62_842_880


def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc201515.part2(example1) == 57_600_000
