"""Custom configuration of pytest."""

# Standard library imports
import pathlib

# Third party imports
import pytest


def pytest_configure(config):
    """Add custom markers from the configuration."""
    years = [p.name for p in pathlib.Path(__file__).parent.glob("2*")]

    for year in years:
        config.addinivalue_line("markers", f"year{year}: Puzzles for year {year}")


def pytest_collection_modifyitems(config, items):
    """Add marks based the year of the puzzle."""
    for item in items:
        try:
            year = item.callspec.getparam("puzzle_path").parent.name
        except (AttributeError, ValueError):
            year = pathlib.Path(item.fspath.dirname).parent.name

        if year.startswith("2"):
            item.add_marker(getattr(pytest.mark, f"year{year}"))
