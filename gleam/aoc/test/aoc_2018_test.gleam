import aoc
import aoc_2018/day_1
import aoc_2018/day_2
import birdie
import gleam/dict
import gleam/list
import gleam/string
import gleeunit
import gleeunit/should

pub fn main() {
  gleeunit.main()
}

pub fn day_02_count_repeats_test() {
  let input =
    ["abcaba", "abcdef", "aaaaaa", "abbaba"]
    |> list.map(string.to_graphemes)

  day_2.count_repeats(input, 1) |> should.equal(2)
  day_2.count_repeats(input, 2) |> should.equal(1)
  day_2.count_repeats(input, 3) |> should.equal(2)
  day_2.count_repeats(input, 4) |> should.equal(0)
}

pub fn day_02_count_letters_test() {
  day_2.count_letters(["a", "b", "c", "a", "b", "a"])
  |> should.equal(dict.from_list([#("a", 3), #("b", 2), #("c", 1)]))
}

pub fn day_02_find_matching_ids_test() {
  ["abcaba", "abcdef", "aaaaaa", "abbaba"]
  |> list.map(string.to_graphemes)
  |> day_2.find_matching_ids()
  |> should.equal("ababa")
}

pub fn day_02_check_similar_test() {
  day_2.check_similar(["a", "b", "c", "d"], ["d", "c", "b", "a"], [], 0)
  |> should.be_error()

  day_2.check_similar(["a", "b", "c", "d"], ["a", "e", "c", "d"], [], 0)
  |> should.equal(Ok("acd"))
}

// SNAPSHOT TESTS
pub fn day_01_snapshot_test() {
  aoc.solve(2018, 1, day_1.parse, day_1.pt_1, day_1.pt_2)
  |> birdie.snap("Puzzle 2018-01")
}

pub fn day_02_snapshot_test() {
  aoc.solve(2018, 2, day_2.parse, day_2.pt_1, day_2.pt_2)
  |> birdie.snap("Puzzle 2018-02")
}
