"""Tests for AoC 4, 2021: Giant Squid"""

# Standard library imports
import pathlib
from collections import deque

# Third party imports
import aoc202104
import pytest
from aoc202104 import BingoBoard, BingoBoards

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc202104.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().strip()
    return aoc202104.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly"""
    assert example1 == BingoBoards(
        [
            BingoBoard(
                moves=deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
                board={
                    0: (0, 0),
                    1: (1, 0),
                    2: (0, 1),
                    3: (1, 1),
                    5: (1, 2),
                    6: (2, 2),
                    7: (2, 1),
                    8: (2, 0),
                    9: (0, 2),
                },
            )
        ]
    )


def test_part1_example2(example2):
    """Test part 1 on example input"""
    assert aoc202104.part1(example2) == 4512


def test_part2_example2(example2):
    """Test part 2 on example input"""
    assert aoc202104.part2(example2) == 1924
