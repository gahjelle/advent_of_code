import gleam/int
import gleam/list
import gleam/string

pub type Present {
  Box(length: Int, width: Int, height: Int)
}

pub type Data =
  List(Present)

pub fn parse(input: String) -> Data {
  input
  |> string.trim()
  |> string.split(on: "\n")
  |> list.map(fn(input) {
    input
    |> string.split("x")
    |> list.map(int.parse)
    |> fn(present) {
      case present {
        [Ok(length), Ok(width), Ok(height)] -> Box(length, width, height)
        _ -> panic as { "Bad present: " <> input }
      }
    }
  })
}

pub fn pt_1(input: Data) -> Int {
  input
  |> list.map(fn(present) { surface_area(present) + smallest_side(present) })
  |> int.sum()
}

pub fn pt_2(input: Data) -> Int {
  input
  |> list.map(fn(present) { smallest_perimeter(present) + volume(present) })
  |> int.sum()
}

fn shortest_sides(box: Present) -> #(Int, Int) {
  case box.length, box.width, box.height {
    ln, wd, ht if ln >= wd && ln >= ht -> #(wd, ht)
    ln, wd, ht if wd >= ln && wd >= ht -> #(ht, ln)
    ln, wd, ht if ht >= ln && ht >= wd -> #(ln, wd)
    _, _, _ -> panic as "bad box"
  }
}

pub fn surface_area(box: Present) -> Int {
  let Box(length, width, height) = box
  2 * { length * width + width * height + height * length }
}

pub fn smallest_side(box: Present) -> Int {
  let #(first, second) = box |> shortest_sides
  first * second
}

pub fn smallest_perimeter(box: Present) -> Int {
  let #(first, second) = box |> shortest_sides
  2 * { first + second }
}

pub fn volume(box: Present) -> Int {
  box.length * box.width * box.height
}
