"""Tests for AoC 15, 2024: Warehouse Woes."""

# Standard library imports
import pathlib

# Third party imports
import aoc202415
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc202415.parse_data(puzzle_input)


@pytest.fixture
def example2():
    puzzle_input = (PUZZLE_DIR / "example2.txt").read_text().rstrip()
    return aoc202415.parse_data(puzzle_input)


@pytest.fixture
def example3():
    puzzle_input = (PUZZLE_DIR / "example3.txt").read_text().rstrip()
    return aoc202415.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    grid, moves = example1
    assert grid == {
        (0, 0): "#",
        (0, 1): "#",
        (0, 2): "#",
        (0, 3): "#",
        (0, 4): "#",
        (0, 5): "#",
        (0, 6): "#",
        (0, 7): "#",
        (1, 0): "#",
        (1, 1): ".",
        (1, 2): ".",
        (1, 3): "O",
        (1, 4): ".",
        (1, 5): "O",
        (1, 6): ".",
        (1, 7): "#",
        (2, 0): "#",
        (2, 1): "#",
        (2, 2): "@",
        (2, 3): ".",
        (2, 4): "O",
        (2, 5): ".",
        (2, 6): ".",
        (2, 7): "#",
        (3, 0): "#",
        (3, 1): ".",
        (3, 2): ".",
        (3, 3): ".",
        (3, 4): "O",
        (3, 5): ".",
        (3, 6): ".",
        (3, 7): "#",
        (4, 0): "#",
        (4, 1): ".",
        (4, 2): "#",
        (4, 3): ".",
        (4, 4): "O",
        (4, 5): ".",
        (4, 6): ".",
        (4, 7): "#",
        (5, 0): "#",
        (5, 1): ".",
        (5, 2): ".",
        (5, 3): ".",
        (5, 4): "O",
        (5, 5): ".",
        (5, 6): ".",
        (5, 7): "#",
        (6, 0): "#",
        (6, 1): ".",
        (6, 2): ".",
        (6, 3): ".",
        (6, 4): ".",
        (6, 5): ".",
        (6, 6): ".",
        (6, 7): "#",
        (7, 0): "#",
        (7, 1): "#",
        (7, 2): "#",
        (7, 3): "#",
        (7, 4): "#",
        (7, 5): "#",
        (7, 6): "#",
        (7, 7): "#",
    }
    assert moves == [
        (0, -1),
        (-1, 0),
        (-1, 0),
        (0, 1),
        (0, 1),
        (0, 1),
        (1, 0),
        (1, 0),
        (0, -1),
        (1, 0),
        (0, 1),
        (0, 1),
        (1, 0),
        (0, -1),
        (0, -1),
    ]


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202415.part1(example1) == 2_028


def test_part1_example2(example2):
    """Test part 1 on example input."""
    assert aoc202415.part1(example2) == 10_092


def test_part2_example2(example2):
    """Test part 2 on example input."""
    assert aoc202415.part2(example2) == 9_021


def test_part2_example3(example3):
    """Test part 2 on example input."""
    assert aoc202415.part2(example3) == 618
