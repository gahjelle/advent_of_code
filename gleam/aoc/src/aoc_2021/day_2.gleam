import gleam/int
import gleam/list
import gleam/result
import gleam/string

pub type Command {
  Forward(Int)
  Down(Int)
  Up(Int)
}

pub type Data =
  List(Command)

pub fn parse(input: String) -> Data {
  input
  |> string.trim()
  |> string.split(on: "\n")
  |> list.map(fn(line) {
    case line |> string.split(" ") {
      ["forward", step] ->
        step |> int.parse() |> result.unwrap(or: 0) |> Forward()
      ["down", step] -> step |> int.parse() |> result.unwrap(or: 0) |> Down()
      ["up", step] -> step |> int.parse() |> result.unwrap(or: 0) |> Up()
      _ -> panic
    }
  })
}

pub fn pt_1(input: Data) -> Int {
  let #(depth, pos) =
    input
    |> list.fold(from: #(0, 0), with: fn(acc, command) {
      case command, acc {
        Forward(step), #(depth, pos) -> #(depth, pos + step)
        Down(step), #(depth, pos) -> #(depth + step, pos)
        Up(step), #(depth, pos) -> #(depth - step, pos)
      }
    })
  depth * pos
}

pub fn pt_2(input: Data) -> Int {
  let #(_aim, depth, pos) =
    input
    |> list.fold(from: #(0, 0, 0), with: fn(acc, command) {
      case command, acc {
        Forward(step), #(aim, depth, pos) -> #(
          aim,
          depth + step * aim,
          pos + step,
        )
        Down(step), #(aim, depth, pos) -> #(aim + step, depth, pos)
        Up(step), #(aim, depth, pos) -> #(aim - step, depth, pos)
      }
    })
  depth * pos
}
