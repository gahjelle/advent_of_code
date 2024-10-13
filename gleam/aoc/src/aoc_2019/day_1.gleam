import gleam/int
import gleam/list
import gleam/result
import gleam/string

type Data =
  List(Int)

pub fn parse(input: String) -> Data {
  input
  |> string.trim_right()
  |> string.split(on: "\n")
  |> list.map(fn(number) { int.parse(number) |> result.unwrap(or: 0) })
}

pub fn pt_1(input: Data) {
  input |> list.map(fuel) |> int.sum()
}

pub fn pt_2(input: Data) {
  input |> list.map(all_fuel) |> int.sum()
}

pub fn fuel(mass: Int) -> Int {
  mass / 3 - 2
}

pub fn all_fuel(mass: Int) -> Int {
  case fuel(mass) {
    fuel if fuel <= 0 -> 0
    fuel -> fuel + all_fuel(fuel)
  }
}
