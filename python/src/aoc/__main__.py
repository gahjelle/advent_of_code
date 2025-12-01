"""Main entrypoint for code runner."""

from pathlib import Path

from gahllenges import cli

root_path = Path(__file__).parent.parent.parent.parent
config_path = root_path / "python" / "src" / "aoc" / "advent_of_code.toml"


def main() -> None:
    """Call the CLI."""
    app = cli.configure_app(root_dir=root_path, config_path=config_path)
    return app()
