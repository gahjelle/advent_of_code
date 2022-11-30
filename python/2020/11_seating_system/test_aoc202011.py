"""Tests for AoC 11, 2020: Seating System"""

# Standard library imports
import pathlib

# Third party imports
import aoc202011
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc202011.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    # fmt: off
    assert example1 == {
        (0, 0),         (0, 2), (0, 3),         (0, 5), (0, 6),         (0, 8), (0, 9),
        (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6),         (1, 8), (1, 9),
        (2, 0),         (2, 2),         (2, 4),                 (2, 7),
        (3, 0), (3, 1), (3, 2), (3, 3),         (3, 5), (3, 6),         (3, 8), (3, 9),
        (4, 0),         (4, 2), (4, 3),         (4, 5), (4, 6),         (4, 8), (4, 9),
        (5, 0),         (5, 2), (5, 3), (5, 4), (5, 5), (5, 6),         (5, 8), (5, 9),
                        (6, 2),         (6, 4),
        (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (7, 9),
        (8, 0),         (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7),         (8, 9),
        (9, 0),         (9, 2), (9, 3), (9, 4), (9, 5), (9, 6),         (9, 8), (9, 9),
    }  # fmt: on


def test_part1_example1(example1):
    """Test part 1 on example input"""
    assert aoc202011.part1(example1) == 37


def test_part2_example1(example1):
    """Test part 2 on example input"""
    assert aoc202011.part2(example1) == 26
