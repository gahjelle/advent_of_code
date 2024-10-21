import aoc
import aoc_2017/day_1
import birdie
import gleeunit

pub fn main() {
  gleeunit.main()
}

pub fn day_01_snapshot_test() {
  aoc.solve(2017, 1, day_1.parse, day_1.pt_1, day_1.pt_2)
  |> birdie.snap("Puzzle 2017-01")
}
