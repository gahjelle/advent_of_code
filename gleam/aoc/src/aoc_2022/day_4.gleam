import aoc.{to_int}
import gleam/list
import gleam/string

pub type Data =
  List(#(#(Int, Int), #(Int, Int)))

pub fn parse(input: String) -> Data {
  input
  |> string.trim()
  |> string.split(on: "\n")
  |> list.map(fn(line) {
    let assert Ok(#(a_range, b_range)) = line |> string.split_once(",")
    let assert Ok(#(a_start, a_end)) = a_range |> string.split_once("-")
    let assert Ok(#(b_start, b_end)) = b_range |> string.split_once("-")
    #(#(to_int(a_start), to_int(a_end)), #(to_int(b_start), to_int(b_end)))
  })
}

pub fn pt_1(input: Data) -> Int {
  input |> list.count(contain)
}

pub fn pt_2(input: Data) -> Int {
  input |> list.count(overlap)
}

fn contain(ranges: #(#(Int, Int), #(Int, Int))) -> Bool {
  case ranges {
    #(#(a_start, a_end), #(b_start, b_end)) ->
      { a_start <= b_start && a_end >= b_end }
      || { b_start <= a_start && b_end >= a_end }
  }
}

fn overlap(ranges: #(#(Int, Int), #(Int, Int))) -> Bool {
  case ranges {
    #(#(a_start, a_end), #(b_start, b_end)) ->
      !{ a_end < b_start || a_start > b_end }
  }
}
