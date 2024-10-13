import gleam/int
import gleam/list
import gleam/string

type Data =
  List(Int)

pub fn parse(input: String) -> Data {
  input
  |> string.to_graphemes()
  |> list.map(fn(paren) {
    case paren {
      "(" -> 1
      ")" -> -1
      symbol -> panic as { "Not a parenthesis: " <> symbol }
    }
  })
}

pub fn pt_1(input: Data) {
  input |> int.sum()
}

pub fn pt_2(input: Data) {
  input
  |> list.scan(from: 0, with: fn(acc, elem) { acc + elem })
  |> list.take_while(satisfying: fn(acc) { acc >= 0 })
  |> list.length()
  |> fn(len) { len + 1 }
}
