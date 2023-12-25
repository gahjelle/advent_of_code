"""Tests for AoC 25, 2023: Snowverload."""

# Standard library imports
import pathlib

# Third party imports
import aoc202325
import networkx as nx
import pytest

PUZZLE_DIR = pathlib.Path(__file__).parent


@pytest.fixture
def example1():
    puzzle_input = (PUZZLE_DIR / "example1.txt").read_text().rstrip()
    return aoc202325.parse_data(puzzle_input)


def test_parse_example1(example1):
    """Test that input is parsed properly."""
    graph = nx.Graph(
        {
            "jqt": {"rhn", "ntq", "nvd", "xhk"},
            "rhn": {"bvb", "jqt", "hfx", "xhk"},
            "xhk": {"rhn", "hfx", "jqt", "ntq", "bvb"},
            "nvd": {"qnr", "jqt", "lhk", "pzl", "cmg"},
            "rsh": {"rzs", "frs", "pzl", "lsr"},
            "frs": {"lsr", "lhk", "rsh", "qnr"},
            "pzl": {"lsr", "hfx", "rsh", "nvd"},
            "lsr": {"rzs", "lhk", "rsh", "frs", "pzl"},
            "hfx": {"rhn", "xhk", "ntq", "bvb", "pzl"},
            "cmg": {"rzs", "qnr", "nvd", "lhk", "bvb"},
            "qnr": {"rzs", "frs", "nvd", "cmg"},
            "lhk": {"lsr", "frs", "nvd", "cmg"},
            "bvb": {"rhn", "hfx", "xhk", "ntq", "cmg"},
            "ntq": {"bvb", "jqt", "hfx", "xhk"},
            "rzs": {"lsr", "rsh", "qnr", "cmg"},
        }
    )
    assert example1.nodes == graph.nodes
    assert example1.edges == graph.edges


def test_part1_example1(example1):
    """Test part 1 on example input."""
    assert aoc202325.part1(example1) == 54
