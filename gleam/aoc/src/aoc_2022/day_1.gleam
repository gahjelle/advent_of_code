import gleam/int
import gleam/list
import gleam/order
import gleam/result
import gleam/string

type Data =
  List(List(Int))

pub fn parse(input: String) -> Data {
  input
  |> string.trim_right()
  |> string.split(on: "\n\n")
  |> list.map(fn(calories) {
    calories
    |> string.split(on: "\n")
    |> list.map(fn(number) { int.parse(number) |> result.unwrap(or: 0) })
  })
}

pub fn pt_1(input: Data) -> Int {
  input
  |> list.map(int.sum)
  |> list.fold(from: 0, with: int.max)
}

pub fn pt_2(input: Data) -> Int {
  input
  |> list.map(int.sum)
  |> list.sort(by: int.compare |> order.reverse)
  |> list.take(up_to: 3)
  |> int.sum()
}
