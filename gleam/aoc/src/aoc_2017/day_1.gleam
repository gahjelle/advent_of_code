import gleam/int
import gleam/list
import gleam/result
import gleam/string

pub type Data =
  List(Int)

pub fn parse(input: String) -> Data {
  input
  |> string.trim()
  |> string.split(on: "")
  |> list.map(fn(digit) { digit |> int.parse() |> result.unwrap(or: 0) })
}

pub fn pt_1(input: Data) -> Int {
  input
  |> pair_neighbors()
  |> filter_equal_pairs()
  |> int.sum()
}

pub fn pt_2(input: Data) -> Int {
  input
  |> pair_half()
  |> filter_equal_pairs()
  |> int.sum()
}

fn pair_neighbors(input: List(Int)) -> List(#(Int, Int)) {
  case input {
    [first, ..rest] -> [first, ..list.reverse([first, ..list.reverse(rest)])]
    [] -> []
  }
  |> list.window_by_2()
}

fn pair_half(input: List(Int)) -> List(#(Int, Int)) {
  list.sized_chunk(input, into: list.length(input) / 2)
  |> fn(lists) {
    case lists {
      [first, second] -> list.zip(input, list.concat([second, first]))
      _ -> panic
    }
  }
}

fn filter_equal_pairs(pairs: List(#(Int, Int))) -> List(Int) {
  pairs
  |> list.filter_map(fn(pair) {
    case pair {
      #(first, second) if first == second -> Ok(first)
      _ -> Error(Nil)
    }
  })
}
