import gleam/int
import gleam/list
import gleam/result
import gleam/string

pub type Data =
  List(Int)

pub fn parse(input: String) -> Data {
  input
  |> string.trim()
  |> string.split(on: "\n")
  |> list.map(fn(line) { line |> int.parse() |> result.unwrap(or: 0) })
}

pub fn pt_1(input: Data) {
  input
  |> list.window_by_2()
  |> list.count(fn(depths) {
    case depths {
      #(first, second) -> first < second
    }
  })
}

pub fn pt_2(input: Data) -> Int {
  input |> list.window(by: 3) |> list.map(int.sum) |> pt_1()
}
