import gleam/int
import gleam/iterator
import gleam/list.{Continue, Stop}
import gleam/result
import gleam/set
import gleam/string

pub type Data =
  List(Int)

pub fn parse(input: String) -> Data {
  input
  |> string.trim()
  |> string.split(on: "\n")
  |> list.map(fn(d_freq) { int.parse(d_freq) |> result.unwrap(or: 0) })
}

pub fn pt_1(input: Data) -> Int {
  input |> int.sum()
}

pub fn pt_2(input: Data) -> Int {
  input
  |> iterator.from_list()
  |> iterator.cycle()
  |> iterator.fold_until(#(0, set.new()), fn(acc, d_freq) {
    let #(freq, seen) = acc
    case set.contains(seen, freq) {
      True -> Stop(#(freq, seen))
      False -> Continue(#(freq + d_freq, set.insert(seen, freq)))
    }
  })
  |> fn(acc) { acc.0 }
}
