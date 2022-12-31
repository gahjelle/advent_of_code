"""Tests for AoC 23, 2017: Coprocessor Conflagration."""

# Standard library imports
import pathlib

# Third party imports
import aoc201723
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc201723.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [
        ("set", "a", 3),
        ("set", "b", 17),
        ("mul", "b", "a"),
        ("mul", "b", 10),
    ]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc201723.part1(example1) == 2
