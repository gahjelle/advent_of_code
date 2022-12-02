"""Tests for AoC 2, 2022: Rock Paper Scissors."""

# Standard library imports
import pathlib

# Third party imports
import aoc202202
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().strip()
    return aoc202202.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [
        ("rock", "paper", "draw"),
        ("paper", "rock", "lose"),
        ("scissors", "scissors", "win"),
    ]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202202.part1(example1) == 15


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc202202.part2(example1) == 12
