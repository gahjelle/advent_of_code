"""AoC 19, 2021: Beacon Scanner."""

# Standard library imports
import itertools
import pathlib
import sys

# Third party imports
import numpy as np

# Cache information between parts
CACHE = {}


def parse_data(puzzle_input):
    """Parse input."""
    reports = {}
    for report in puzzle_input.split("\n\n"):
        reports |= parse_report(report)

    return reports


def parse_report(report):
    """Parse the report from one scanner.

    >>> parse_report("--- scanner 0 ---\\n0,2,0\\n4,1,0\\n3,3,0")
    {0: array([[0, 2, 0], [4, 1, 0], [3, 3, 0]])}
    """
    scanner_string, *beacons = report.split("\n")
    scanner = int(scanner_string.split()[2])
    return {
        scanner: np.array(
            [[int(pos) for pos in beacon.split(",")] for beacon in beacons]
        )
    }


def part1(data):
    """Solve part 1."""
    # Build map and store results to cache for use in part 2
    CACHE["scanners", len(data)], beacons = build_map(data)

    return len(beacons)


def part2(data):
    """Solve part 2."""
    positions = np.array(list(CACHE["scanners", len(data)].values()))
    return np.max(manhattan_distance(positions))


def build_map(reports, min_match=12):
    """Build a map of beacons based on the reports.

    >>> build_map(
    ...     {0: np.array([[0, 2, 0], [4, 1, 0], [3, 3, 0], [1, 2, 3]]),
    ...      1: np.array([[1, -5, 4], [4, -2, 3], [4, -7, 7], [1, 2, 3]]),
    ...      2: np.array([[-1, -1, 0], [-5, 0, 0], [-2, 1, 0], [1, 2, 3]]),
    ...     }, min_match=3)
    ({0: array([0, 0, 0]), 2: array([ 4, 0, -1]), 1: array([5, 5, 5])},
     array([[ 0, 2, 0], [ 4, 1, 0], [ 3, 3, 0], [ 1, 2, 3], [ 1, -2, -2], [ 4, 2, 7]]))
    """
    remaining_scanners = set(reports.keys())

    # Initialize with one of the scanners
    initial_scanner = remaining_scanners.pop()
    scanners = {initial_scanner: np.array([0, 0, 0])}
    known_beacons = reports[initial_scanner]

    # Iteratively add beacons from the remaining scanners
    while remaining_scanners:
        change = False
        for scanner in sorted(remaining_scanners):
            scanner_pos, new_beacons = match_beacons(
                known_beacons, reports[scanner], min_match=min_match
            )
            if scanner_pos is None:
                continue

            change = change or (new_beacons is not None)
            scanners[scanner] = scanner_pos
            known_beacons = np.concatenate((known_beacons, new_beacons))
            remaining_scanners.remove(scanner)
        if not change:
            break

    return scanners, known_beacons


def fingerprint(beacons):
    """Create a fingerprint matrix for the given beacons.

    Use distance between beacons to get fingerprint values that are independent
    of scanner locations.

    >>> fps = fingerprint(np.array([[0, 2, 0], [4, 1, 0], [3, 3, 0], [-1, 2, -3]]))
    >>> [sorted(fp) for fp in fps]
    [[0, 10, 17], [0, 5, 17, 35], [0, 5, 10, 26], [0, 10, 26, 35]]
    """
    return [set(fp) for fp in np.square(beacons[:, None, :] - beacons).sum(axis=2)]


def manhattan_distance(positions):
    """Calculate the Manhattan distance between the given positions.

    >>> manhattan_distance(np.array([[0, 2, 0], [4, 1, 0], [3, 3, 0], [-1, 2, -3]]))
    array([[0, 5, 4, 4], [5, 0, 3, 9], [4, 3, 0, 8], [4, 9, 8, 0]])
    """
    return np.abs(positions[:, None, :] - positions).sum(axis=2)


def match_beacons(known_beacons, new_beacons, min_match=12):
    """Match new beacons to list of known beacons.

    >>> match_beacons(
    ...     np.array([[0, 2, 0], [4, 1, 0], [3, 3, 0], [1, 2, 3]]),
    ...     np.array([[-1, -1, 0], [-5, 0, 0], [-2, 1, 0], [1, 2, 3]]),
    ...     min_match=3)
    (array([ 4, 0, -1]), array([[ 1, -2, -2]]))
    """
    known_fingerprints = fingerprint(known_beacons)
    new_fingerprints = fingerprint(new_beacons)

    # Check if enough beacons overlap
    new_inds, known_inds = [], []
    for new_idx, new_fingerprint in enumerate(new_fingerprints):
        matching_idx = [
            idx
            for idx, known in enumerate(known_fingerprints)
            if len(known & new_fingerprint) >= min_match
        ]
        if matching_idx:
            new_inds.append(new_idx)
            known_inds.append(matching_idx[0])

    if len(new_inds) < min_match:
        return None, None

    # Find orientation of new scanner
    for orientation in orientations():
        offsets = known_beacons[known_inds] - rotate(new_beacons[new_inds], orientation)
        if np.all(np.diff(offsets, axis=0) == 0):
            break

    # Return positions of unknown beacons
    scanner_position = offsets[0]
    unknown_inds = [idx for idx in range(len(new_beacons)) if idx not in new_inds]
    return (
        scanner_position,
        scanner_position + rotate(new_beacons[unknown_inds], orientation),
    )


def rotate(coords, orientation):
    """Rotate coordinates with the given orientation.

    >>> rotate(np.array([[1, 2, 3], [-3, -2, -1]]), np.array([[0, 1, 0], [-1, 0, 0], [0, 0, 1]]))
    array([[ 2, -1, 3], [-2,  3, -1]])
    """
    return (orientation @ coords[:, :, None])[:, :, 0]


def orientations():
    """Iterate through rotation matrices for all possible orientations."""
    for idx in itertools.permutations((0, 1, 2)):
        yield np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])[tuple([idx])]
        yield np.array([[-1, 0, 0], [0, 1, 0], [0, 0, 1]])[tuple([idx])]
        yield np.array([[1, 0, 0], [0, -1, 0], [0, 0, 1]])[tuple([idx])]
        yield np.array([[-1, 0, 0], [0, -1, 0], [0, 0, 1]])[tuple([idx])]
        yield np.array([[1, 0, 0], [0, 1, 0], [0, 0, -1]])[tuple([idx])]
        yield np.array([[-1, 0, 0], [0, 1, 0], [0, 0, -1]])[tuple([idx])]
        yield np.array([[1, 0, 0], [0, -1, 0], [0, 0, -1]])[tuple([idx])]
        yield np.array([[-1, 0, 0], [0, -1, 0], [0, 0, -1]])[tuple([idx])]


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse_data(puzzle_input)
    yield part1(data)
    yield part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(puzzle_input=pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
