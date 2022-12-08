"""AoC 7, 2022: No Space Left On Device."""

# Standard library imports
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    tree = cwd = {}
    parents = []
    for command in puzzle_input.split("\n"):
        match command.split():
            case ["$", "cd", "/"]:
                cwd = tree
                parents = []
            case ["$", "cd", ".."]:
                cwd = parents.pop()
            case ["$", "cd", dir]:
                parents.append(cwd)
                cwd = cwd.setdefault(dir, {})
            case ["$", "ls"] | ["dir", _]:
                pass
            case [size, file]:
                cwd[file] = int(size)
            case _:
                raise ValueError(f"{command!r} not parsed")
    return tree


def part1(tree):
    """Solve part 1."""
    return sum(size for size in dir_sizes(tree) if size <= 100_000)


def part2(tree):
    """Solve part 2."""
    sizes = dir_sizes(tree)
    target_size = max(sizes) - 40_000_000
    return min(size for size in sizes if size >= target_size)


def dir_sizes(tree, prefix=""):
    """Recursively calculate the size of each directory."""
    dirs = []
    total_size = 0
    for name, content in tree.items():
        if isinstance(content, dict):
            path = f"{prefix}/{name}"
            dirs.extend(dir_sizes(content, prefix=path))
            total_size += dirs[-1]
        else:
            total_size += content
    dirs.append(total_size)
    return dirs


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().rstrip())
        print("\n".join(str(solution) for solution in solutions))
