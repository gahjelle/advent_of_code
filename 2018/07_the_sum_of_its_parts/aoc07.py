"""The Sum of its Parts

Advent of Code 2018, day 7
Solution by Geir Arne Hjelle, 2018-12-11
"""
import itertools
import re
import sys

debug = print if "--debug" in sys.argv else lambda *_: None


class Task:
    def __init__(self, name, step_time=None):
        self.name = name
        if step_time is not None:
            self.remaining = step_time + ord(name) - (ord("A") - 1)
        else:
            self.remaining = 0

    @classmethod
    def empty(cls):
        return cls("")

    def tick(self):
        self.remaining -= 1

    @property
    def done(self):
        return self.remaining <= 0

    def __bool__(self):
        return not self.done

    def __repr__(self):
        return f"({self.name:<1}, {'' if self.done else self.remaining:>3})"


def parse_tree(lines):
    pattern = re.compile(r"Step (\w) must be finished before step (\w) can begin.")
    tree = dict()
    for num, line in enumerate(lines, start=1):
        match = pattern.match(line)
        if match:
            dependant, step = match.groups()
            tree.setdefault(dependant, set())
            tree.setdefault(step, set()).add(dependant)
        else:
            print(f"Could not parse line {num}: {line!r}")

    return tree


def find_order(tree):
    while tree:
        next_step = sorted(n for n, d in tree.items() if not d).pop(0)
        tree = {n: d - {next_step} for n, d in tree.items() if n != next_step}
        yield next_step


def time_workers(tree, num_workers, step_time):
    workers = [Task.empty()] * num_workers
    done = list()

    for time in itertools.count(start=0):
        available = [id for id, w in enumerate(workers) if w.done]
        for worker_id in available:
            finished_step = workers[worker_id].name
            if finished_step:
                workers[worker_id] = Task.empty()
                tree = {n: d - {finished_step} for n, d in tree.items()}
                done.append(finished_step)

        if not tree and all(w.done for w in workers):
            break

        for worker_id in available:
            steps = sorted(n for n, d in tree.items() if not d)
            if not steps:
                continue
            next_step = steps.pop(0)
            tree = {n: d for n, d in tree.items() if n != next_step}
            workers[worker_id] = Task(next_step, step_time=step_time)

        debug(f"{time:4d}  {workers}  {''.join(done)}")
        [w.tick() for w in workers]

    return time, "".join(done)


def main(args):
    for filename in args:
        if filename.startswith("--"):
            continue

        print(f"\n{filename}:")
        with open(filename, mode="r") as fid:
            tree = parse_tree(line.strip() for line in fid)
        print(f"Order: {''.join(find_order(tree))}")
        time, order = time_workers(tree, num_workers=5, step_time=60)
        print(f"Time: {time} seconds ({order})")


if __name__ == "__main__":
    main(sys.argv[1:])
