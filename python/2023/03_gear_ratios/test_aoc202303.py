"""Tests for AoC 3, 2023: Gear Ratios."""

# Standard library imports
import pathlib

# Third party imports
import aoc202303
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc202303.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    assert example1[0] == [
        (
            467,
            {
                (0, 1),
                (2, -1),
                (3, -1),
                (-1, -1),
                (2, 1),
                (3, 1),
                (-1, 1),
                (1, 1),
                (1, -1),
                (3, 0),
                (-1, 0),
                (0, -1),
            },
        ),
        (
            114,
            {
                (7, -1),
                (4, 0),
                (8, -1),
                (7, 1),
                (8, 1),
                (6, 1),
                (5, -1),
                (6, -1),
                (5, 1),
                (8, 0),
                (4, -1),
                (4, 1),
            },
        ),
        (
            35,
            {
                (1, 2),
                (2, 1),
                (4, 3),
                (4, 1),
                (3, 1),
                (1, 1),
                (4, 2),
                (2, 3),
                (3, 3),
                (1, 3),
            },
        ),
        (
            633,
            {
                (7, 1),
                (9, 3),
                (8, 1),
                (6, 1),
                (5, 1),
                (9, 2),
                (7, 3),
                (8, 3),
                (6, 3),
                (5, 3),
                (9, 1),
                (5, 2),
            },
        ),
        (
            617,
            {
                (3, 4),
                (-1, 4),
                (1, 5),
                (0, 3),
                (2, 3),
                (3, 3),
                (-1, 3),
                (0, 5),
                (2, 5),
                (1, 3),
                (3, 5),
                (-1, 5),
            },
        ),
        (
            58,
            {
                (7, 4),
                (8, 4),
                (6, 5),
                (9, 6),
                (6, 4),
                (9, 5),
                (7, 6),
                (8, 6),
                (6, 6),
                (9, 4),
            },
        ),
        (
            592,
            {
                (5, 5),
                (2, 7),
                (1, 5),
                (3, 7),
                (5, 7),
                (1, 7),
                (4, 5),
                (5, 6),
                (1, 6),
                (2, 5),
                (4, 7),
                (3, 5),
            },
        ),
        (
            755,
            {
                (8, 8),
                (5, 8),
                (9, 6),
                (6, 8),
                (5, 7),
                (7, 6),
                (5, 6),
                (9, 8),
                (8, 6),
                (6, 6),
                (9, 7),
                (7, 8),
            },
        ),
        (
            664,
            {
                (4, 10),
                (3, 8),
                (0, 10),
                (4, 9),
                (2, 10),
                (1, 8),
                (0, 9),
                (3, 10),
                (4, 8),
                (1, 10),
                (0, 8),
                (2, 8),
            },
        ),
        (
            598,
            {
                (4, 10),
                (8, 8),
                (5, 8),
                (4, 9),
                (7, 10),
                (6, 8),
                (8, 10),
                (5, 10),
                (8, 9),
                (6, 10),
                (4, 8),
                (7, 8),
            },
        ),
    ]

    assert example1[1] == {
        (3, 1): "*",
        (6, 3): "#",
        (3, 4): "*",
        (5, 5): "+",
        (3, 8): "$",
        (5, 8): "*",
    }


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202303.part1(example1) == 4361


def test_part2_example1(example1):
    """Test part 2 on example input."""
    assert aoc202303.part2(example1) == 467835
