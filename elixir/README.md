# Advent of Code in Elixir

Solutions to [Advent of Code](https://adventofcode.com/) in [Elixir](https://elixir-lang.org/) (66⭐):

|   Day | [2015](lib/2015)                                         | [2016](lib/2016)                           | [2017](lib/2017)                      | [2018](lib/2018)                              | [2019](lib/2019)                                     | [2020](lib/2020)                      | [2021](lib/2021)                          |
|------:|:---------------------------------------------------------|:-------------------------------------------|:--------------------------------------|:----------------------------------------------|:-----------------------------------------------------|:--------------------------------------|:------------------------------------------|
|     1 | [⭐⭐](lib/2015/01_not_quite_lisp)                         | [⭐⭐](lib/2016/01_no_time_for_a_taxicab)    | [⭐⭐](lib/2017/01_inverse_captcha)     | [⭐⭐](lib/2018/01_chronal_calibration)         | [⭐⭐](lib/2019/01_the_tyranny_of_the_rocket_equation) | [⭐⭐](lib/2020/01_report_repair)       | [⭐⭐](lib/2021/01_sonar_sweep)             |
|     2 | [⭐⭐](lib/2015/02_i_was_told_there_would_be_no_math)      | [⭐⭐](lib/2016/02_bathroom_security)        | [⭐⭐](lib/2017/02_corruption_checksum) | [⭐⭐](lib/2018/02_inventory_management_system) | [⭐⭐](lib/2019/02_1202_program_alarm)                 | [⭐⭐](lib/2020/02_password_philosophy) | [⭐⭐](lib/2021/02_dive)                    |
|     3 | [⭐⭐](lib/2015/03_perfectly_spherical_houses_in_a_vacuum) | [⭐⭐](lib/2016/03_squares_with_three_sides) |                                       |                                               |                                                      |                                       | [⭐⭐](lib/2021/03_binary_diagnostic)       |
|     4 | [⭐⭐](lib/2015/04_the_ideal_stocking_stuffer)             |                                            |                                       |                                               |                                                      |                                       | [⭐⭐](lib/2021/04_giant_squid)             |
|     5 | [⭐⭐](lib/2015/05_doesnt_he_have_intern-elves_for_this)   |                                            |                                       |                                               |                                                      |                                       | [⭐⭐](lib/2021/05_hydrothermal_venture)    |
|     6 | [⭐⭐](lib/2015/06_probably_a_fire_hazard)                 |                                            |                                       | [⭐⭐](lib/2018/06_chronal_coordinates)         |                                                      |                                       | [⭐⭐](lib/2021/06_lanternfish)             |
|     7 | [⭐⭐](lib/2015/07_some_assembly_required)                 |                                            |                                       |                                               |                                                      |                                       | [⭐⭐](lib/2021/07_the_treachery_of_whales) |
|     8 |                                                          |                                            |                                       |                                               |                                                      |                                       | [⭐⭐](lib/2021/08_seven_segment_search)    |
|     9 |                                                          |                                            |                                       |                                               |                                                      |                                       | [⭐⭐](lib/2021/09_smoke_basin)             |
|    10 |                                                          |                                            |                                       |                                               |                                                      |                                       | [⭐⭐](lib/2021/10_syntax_scoring)          |
|    11 |                                                          |                                            |                                       |                                               |                                                      |                                       | [⭐⭐](lib/2021/11_dumbo_octopus)           |
|    12 |                                                          |                                            |                                       |                                               |                                                      |                                       |                                           |
|    13 |                                                          |                                            |                                       |                                               |                                                      |                                       |                                           |
|    14 |                                                          |                                            |                                       |                                               |                                                      |                                       | [⭐⭐](lib/2021/14_extended_polymerization) |
|    15 |                                                          |                                            |                                       |                                               |                                                      |                                       |                                           |
|    16 |                                                          |                                            |                                       |                                               |                                                      |                                       |                                           |
|    17 |                                                          |                                            |                                       |                                               |                                                      |                                       | [⭐⭐](lib/2021/17_trick_shot)              |
|    18 |                                                          |                                            |                                       |                                               |                                                      |                                       | [⭐⭐](lib/2021/18_snailfish)               |
|    19 |                                                          |                                            |                                       |                                               |                                                      |                                       |                                           |
|    20 |                                                          |                                            |                                       |                                               |                                                      |                                       |                                           |
|    21 |                                                          |                                            |                                       |                                               |                                                      |                                       |                                           |
|    22 |                                                          |                                            |                                       |                                               |                                                      |                                       |                                           |
|    23 |                                                          |                                            |                                       |                                               |                                                      |                                       |                                           |
|    24 |                                                          |                                            |                                       |                                               |                                                      |                                       |                                           |
|    25 |                                                          |                                            |                                       |                                               |                                                      |                                       |                                           |

## Run the Solutions

There are two special Advent of Code mix tasks:

- `mix solve 2015 1` solves the given puzzle, in this case Puzzle 1, 2015.
- `mix benchmark 2015 1` benchmarks the given puzzle, in this case Puzzle 1, 2015.

You can also run the solutions manually inside a `iex -S mix` session:

```elixir
iex> import AOC2015.Day01
iex> AOC.solve("lib/2015/01_not_quite_lisp/input.txt", &parse/1, &part1/1, &part2/1)
```

Alternatively, you can only read and parse the data, and work with them manually from there:

```elixir
iex> import AOC2015.Day01
iex> data = AOC.read_text("lib/2015/01_not_quite_lisp/input.txt") |> parse()
```

## Bootstrap a Puzzle Solution

Use `copier` to invoke the Elixir template and set up files for a new solution:

```console
$ copier path/to/template-aoc-elixir/ .
```

Answer the questions and allow the hook to download your personal input.


## Test a Solution

Each puzzle comes with a test file that can be run with `mix test`:

```console
$ mix test test/aoc201501_test.exs
```

You can run all tests by not specifying a particular test file:

```console
$ mix test
```

This will run all tests except those marked as `slow` or `solution`. The
`solution` tests run the full solution and compare the result to the correct
solution. You can run them by including them:

```console
$ mix test --include solution
```

There are also a few other tags you can use:

```console
$ mix test --only solution
$ mix test --only year2015
$ mix test --include solution --exclude year2015
```


## Adding a Solution to GitHub

Follow these steps after solving a puzzle:

1. Store the solution to an output file:

    ```console
    $ mix solve 2015 1 > lib/2015/01_not_quite_lisp/output.ex.txt
    ```

2. Run benchmarks and add them to the README:

    ```console
    $ mix benchmark 2015 1
    ```

3. Update READMEs across all projects:

    ```console
    $ cd ..
    $ make
    ```
