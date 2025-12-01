"""AoC 9, 2024: Disk Fragmenter."""

# Standard library imports
import pathlib
import sys


def parse_data(puzzle_input):
    """Parse input."""
    return [
        (int(file), int(free))
        for file, free in zip(puzzle_input[::2], puzzle_input[1::2] + "0")
    ]


def part1(data):
    """Solve part 1."""
    return sum(idx * file for idx, file in enumerate(fragment(data)))


def part2(data):
    """Solve part 2."""
    return sum(idx * file for idx, file in enumerate(compact(data)))


def fragment(data):
    """Fragment files on disk to remove free spaces.

    Build up the disk from the beginning, filling in free space from the end.

    ## Example:

    >>> fragment([(1, 2), (3, 4), (5, 0)])
    [0, 2, 2, 1, 1, 1, 2, 2, 2]
    """
    disk = []
    start_idx, end_idx = 0, len(data) - 1
    end_len, _ = data[end_idx]
    while start_idx < end_idx:
        file_len, free_len = data[start_idx]
        disk.extend([start_idx] * file_len)
        while free_len > 0:
            disk.append(end_idx)
            free_len, end_len = free_len - 1, end_len - 1
            if end_len == 0:
                end_idx -= 1
                if end_idx == start_idx:
                    break
                end_len, _ = data[end_idx]
        start_idx += 1
    else:
        disk.extend([start_idx] * end_len)
    return disk


def compact(data):
    """Compact disk use by moving files where there is enough space.

    Create the full disk and tables of indices. Then move files from the back
    into the first available free space.

    ## Example

        00000....111..2
        000002...111...
        000002111......

    >>> compact([(5, 4), (3, 2), (1, 0)])
    [0, 0, 0, 0, 0, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0]
    """
    disk, files, free_space = [], [], []
    idx = 0
    for file_id, (file_len, free_len) in enumerate(data):
        disk += [file_id] * file_len + [0] * free_len
        files.append((file_id, idx, file_len))
        free_space.append((idx + file_len, free_len))
        idx += file_len + free_len

    for file_id, file_idx, file_len in files[::-1]:
        for to_idx, (free_idx, free_len) in enumerate(free_space[:file_id]):
            if file_len <= free_len:
                disk[free_idx : free_idx + file_len] = [file_id] * file_len
                disk[file_idx : file_idx + file_len] = [0] * file_len
                free_space[to_idx] = (free_idx + file_len, free_len - file_len)
                break
    return disk


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
