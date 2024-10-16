import aoc
import aoc_2021/day_1
import aoc_2021/day_2
import birdie
import gleeunit

pub fn main() {
  gleeunit.main()
}

pub fn day_01_snapshot_test() {
  aoc.solve(2021, 1, day_1.parse, day_1.pt_1, day_1.pt_2)
  |> birdie.snap("Puzzle 2021-01")
}

pub fn day_02_snapshot_test() {
  aoc.solve(2021, 2, day_2.parse, day_2.pt_1, day_2.pt_2)
  |> birdie.snap("Puzzle 2021-02")
}
