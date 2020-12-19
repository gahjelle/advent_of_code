"""Memory Maneuver

Advent of Code 2018, day 8
Solution by Geir Arne Hjelle, 2018-12-09
"""
# Standard library imports
import sys

debug = print if "--debug" in sys.argv else lambda *_: None


def get_meta(node):
    debug(node)
    num_children = node.pop(0)
    num_meta = node.pop(0)

    nodes = list()
    for child in range(num_children):
        nodes.extend(get_meta(node))
    for meta in range(num_meta):
        nodes.append(node.pop(0))
    return nodes


def get_values(node):
    debug(node)
    num_children = node.pop(0)
    num_meta = node.pop(0)
    nodes = [get_values(node) for _ in range(num_children)]

    if num_children == 0:
        return sum(node.pop(0) for _ in range(num_meta))
    else:
        meta = [node.pop(0) - 1 for _ in range(num_meta)]
        return sum(nodes[i] for i in meta if i < len(nodes))


def main(args):
    for filename in args:
        if filename.startswith("--"):
            continue

        print(f"\n{filename}:")
        with open(filename, mode="r") as fid:
            for line in fid:
                tree = [int(f) for f in line.strip().split()]
                metadata = get_meta(tree.copy())
                print(f"Sum of metadata: {sum(metadata)}")

                root_value = get_values(tree.copy())
                print(f"Value of root node: {root_value}")


if __name__ == "__main__":
    main(sys.argv[1:])
