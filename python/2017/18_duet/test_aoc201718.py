"""Tests for AoC 18, 2017: Duet."""

# Standard library imports
import pathlib

# Third party imports
import aoc201718
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc201718.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().rstrip()
    return aoc201718.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1 == [
        ("set", "a", 1),
        ("add", "a", 2),
        ("mul", "a", "a"),
        ("mod", "a", 5),
        ("snd", "a"),
        ("set", "a", 0),
        ("rcv", "a"),
        ("jgz", "a", -1),
        ("set", "a", 1),
        ("jgz", "a", -2),
    ]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc201718.part1(example1) == 4


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc201718.part2(example1) == 1


def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc201718.part2(example2) == 3
