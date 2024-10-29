import aoc
import aoc_2023/day_1
import birdie
import gleeunit
import gleeunit/should

pub fn main() {
  gleeunit.main()
}

pub fn day_01_find_digits_test() {
  day_1.find_digits("a12b3c") |> should.equal(13)
  day_1.find_digits("7") |> should.equal(77)
  day_1.find_digits("0thequickfoxjumped1") |> should.equal(1)
}

pub fn day_01_words_to_digits_test() {
  day_1.words_to_digits("nothinghere") |> should.equal("nothinghere")
  day_1.words_to_digits("oneightwo") |> should.equal("o1e8t2o")
  day_1.words_to_digits("stuffouroast") |> should.equal("stuff4roast")
}

// SNAPSHOT TESTS
pub fn day_01_snapshot_test() {
  aoc.solve(2023, 1, day_1.parse, day_1.pt_1, day_1.pt_2)
  |> birdie.snap("Puzzle 2023-01")
}
