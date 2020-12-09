# Encoding Error
#
# Advent of Code 2020, day 8
# Solution by Geir Arne Hjelle, 2020-12-09

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
function solve(filename)
    println("\n$(filename)")

    # Read from file
    input = open(filename) do fid
        fid |> readlines .|> Instruction
    end

    # Part 1
    input |> run |> first |> println

    # Part 2
    @pipe (
        1:length(input)
        .|> run(input, mutated_line=_)
        |> filter(r -> r[2], _)
        |> first
        |> first
        |> println
    )
end


# Solve the problem for each file
ARGS .|> solve
