"""Universal Orbit Map

Advent of Code 2019, day 6
Solution by Geir Arne Hjelle, 2019-12-06
"""
# Standard library imports
import pathlib
import sys


def build_orbit_map(children, start="COM"):
    orbits = {start: []}

    child_objs = children.copy()
    while child_objs:
        available = set(orbits) & set(child_objs)
        if not available:
            # Third party imports
            import IPython

            IPython.embed()

        for from_obj in available:
            for to_obj in child_objs[from_obj]:
                orbits[to_obj] = [from_obj] + orbits[from_obj]
            del child_objs[from_obj]

    return orbits


def find_distance(orbits, from_obj="YOU", to_obj="SAN"):
    from_orbits = orbits[from_obj]
    to_orbits = orbits[to_obj]
    transfer_objs = set(from_orbits) ^ set(to_orbits)

    self_in_orbit = (from_obj in transfer_objs) + (to_obj in transfer_objs)
    return len(transfer_objs) - 2 * self_in_orbit


def main(args):
    for file_path in [pathlib.Path(p) for p in args if not p.startswith("-")]:
        print(f"\n{file_path}:")
        children = {}
        for line in file_path.read_text().split():
            from_obj, _, to_obj = line.partition(")")
            children.setdefault(from_obj, set()).add(to_obj)
        orbit_map = build_orbit_map(children)

        # Part 1
        num_orbits = sum(len(o) for o in orbit_map.values())
        print(f"Found {num_orbits} direct and indirect orbits")

        # Part 2
        if "YOU" not in orbit_map or "SAN" not in orbit_map:
            continue
        dist = find_distance(orbit_map, "YOU", "SAN")
        print(f"Doing {dist} orbit transitions from YOU to SAN")


if __name__ == "__main__":
    debug = print if "--debug" in sys.argv else lambda *_: None
    main(sys.argv[1:])
