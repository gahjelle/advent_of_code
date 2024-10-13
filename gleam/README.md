# Advent of Code in Gleam

Solutions to [Advent of Code](https://adventofcode.com/) in [Gleam](https://gleam.run/) (6⭐):

|   Day | [2015](aoc/src/aoc_2015)                 | [2019](aoc/src/aoc_2019)                 | [2022](aoc/src/aoc_2022)                 |
|------:|:-----------------------------------------|:-----------------------------------------|:-----------------------------------------|
|     1 | [⭐⭐](aoc/src/aoc_2015/README_day_1.md) | [⭐⭐](aoc/src/aoc_2019/README_day_1.md) | [⭐⭐](aoc/src/aoc_2022/README_day_1.md) |
|     2 |                                          |                                          |                                          |
|     3 |                                          |                                          |                                          |
|     4 |                                          |                                          |                                          |
|     5 |                                          |                                          |                                          |
|     6 |                                          |                                          |                                          |
|     7 |                                          |                                          |                                          |
|     8 |                                          |                                          |                                          |
|     9 |                                          |                                          |                                          |
|    10 |                                          |                                          |                                          |
|    11 |                                          |                                          |                                          |
|    12 |                                          |                                          |                                          |
|    13 |                                          |                                          |                                          |
|    14 |                                          |                                          |                                          |
|    15 |                                          |                                          |                                          |
|    16 |                                          |                                          |                                          |
|    17 |                                          |                                          |                                          |
|    18 |                                          |                                          |                                          |
|    19 |                                          |                                          |                                          |
|    20 |                                          |                                          |                                          |
|    21 |                                          |                                          |                                          |
|    22 |                                          |                                          |                                          |
|    23 |                                          |                                          |                                          |
|    24 |                                          |                                          |                                          |
|    25 |                                          |                                          |                                          |

## Running the Solutions

We use the great [`gladvent`](https://github.com/TanklesXL/gladvent/) project to run the AoC Gleam solutions

```console
$ gleam run run 1 --year=2015
```

You can also run on example input:

```console
$ gleam run run 1 --year=2015 --example
```

## Bootstrap a Puzzle Solution

Use `gladvent` to invoke the Gleam template and set up files for a new solution:

```console
$ gleam run new 1 --year=2015
```

Add input and example input files inside the relevant `input` subdirectory

## Test a solution

You can run tests with `gleam test`:

```console
$ gleam test
```

Additionally, `gladvent` uses expectations registered in `gleam.toml` to check
that each solution gives the correct answer.

## Adding a Solution to GitHub

Follow these steps after solving a puzzle:

1. Store the solution to an output file:

    ```console
    $ gleam run run 1 --year=2015.txt > output/2015/1.gleam.txt
    ```

2. Store the expected results in the `gleam.toml` project file.

3. Update READMEs across all projects:

    ```console
    $ cd ..
    $ make
    ```
