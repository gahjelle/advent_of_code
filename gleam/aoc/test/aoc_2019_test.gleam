import aoc
import aoc_2019/day_1
import birdie
import gleeunit
import gleeunit/should

pub fn main() {
  gleeunit.main()
}

pub fn day_01_fuel_test() {
  day_1.fuel(1969)
  |> should.equal(654)
}

pub fn day_01_all_fuel_test() {
  day_1.all_fuel(1969)
  |> should.equal(966)
}

pub fn day_01_snapshot_test() {
  aoc.solve(2019, 1, day_1.parse, day_1.pt_1, day_1.pt_2)
  |> birdie.snap("Puzzle 2019-01")
}
