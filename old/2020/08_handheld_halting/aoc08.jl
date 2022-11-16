# Encoding Error
#
# Advent of Code 2020, day 8
# Solution by Geir Arne Hjelle, 2020-12-09

module AOC08

using Pipe


#
# Instructions
#

# Accumulate the given value
function op_acc(argument; mutated=false)
    ReturnValue(1, argument)
end

# Move to the next instruction
function op_nop(argument; mutated=false)
    ReturnValue(if mutated argument else 1 end, 0)
end

# Jump relative
function op_jmp(argument; mutated=false)
    ReturnValue(if mutated 1 else argument end, 0)
end

INSTRUCTIONS = Dict("acc" => op_acc, "nop" => op_nop, "jmp" => op_jmp)

struct Instruction
    operation
    argument::Int32

    function Instruction(line)
        op, arg = split(line)
        new(INSTRUCTIONS[op], parse(Int32, arg))
    end

    function Instruction(op, arg)
        new(op, arg)
    end
end

struct ReturnValue
    d_pointer::Int32
    d_accumulator::Int32
end


#
# Run programs
#

# Execute one instruction
function execute(instruction, pointer, accumulator; mutated=false)
    ret_val = instruction.operation(instruction.argument, mutated=mutated)
    pointer + ret_val.d_pointer, accumulator + ret_val.d_accumulator
end


# Run the full program until an infinite loop is detected
function run(program; mutated_line=-1)
    pointer, accumulator = 1, 0
    visited = vcat(zeros(Bool, length(program)), true)

    while !visited[pointer]
        visited[pointer] = true
        pointer, accumulator = execute(
            program[pointer], pointer, accumulator, mutated=pointer == mutated_line
        )
    end

    accumulator, pointer > length(program)
end


# Solve the problem for one file
function solve(input)
    # Parse input
    instructions = split(input, "\n") .|> Instruction

    # Part 1
    part_1 = instructions |> run |> first

    # Part 2
    part_2 = @pipe (
        1:length(instructions)
        .|> run(instructions, mutated_line=_)
        |> filter(r -> r[2], _)
        |> first
        |> first
    )

    part_1, part_2
end


# Solve the problem for one file
function solve_file(file_path)
    println("\n$(file_path)")
    input = open(file_path) do fid
        read(fid, String) |> strip
    end
    input .|> solve
end

# Solve the problem for each file
[a for a in ARGS if a[1] != '-'] .|> solve_file .|> s -> join(s, "\n") |> println

end  # module
