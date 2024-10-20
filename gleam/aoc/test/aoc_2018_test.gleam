import aoc
import aoc_2018/day_1
import birdie
import gleeunit

pub fn main() {
  gleeunit.main()
}

// SNAPSHOT TESTS
pub fn day_01_snapshot_test() {
  aoc.solve(2018, 1, day_1.parse, day_1.pt_1, day_1.pt_2)
  |> birdie.snap("Puzzle 2018-01")
}
