import aoc_2019/day_1
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
