# Encoding Error
#
# Advent of Code 2020, day 9
# Solution by Geir Arne Hjelle, 2020-12-09

module AOC09

using Pipe


# Find two numbers that add up to target. Will return all numbers that are part
# of such pairs.
function find_adders(numbers, target)
    lookup = Set(numbers)
    [n for n in numbers if target - n in lookup]
end


# Find 2 or more contiguous numbers adding up to target. Work backwards to
# avoid working through long runs of small numbers
function find_contiguous(numbers, target)
    idx = length(numbers)
    while idx > 2
        for run_length in 2:idx
            run_sum = sum(numbers[idx - run_length:idx])
            if run_sum > target
                break
            elseif run_sum == target
                return numbers[idx - run_length:idx]
            end
        end
        idx -= 1
    end
end

# Check run of numbers for first error in encoding
function check_numbers(numbers, preamble)
    for idx in preamble + 1:length(numbers)
        if isempty(find_adders(numbers[idx - preamble:idx], numbers[idx]))
            return numbers[idx]
        end
    end
end


# Solve the problem for one file
function solve(input)
    # Parse input, length of preamble has been manually added on first line
    input = split(input, "\n") .|> ln -> parse(Int64, ln)
    preamble, numbers = input[1], input[2:end]

    # Part 1
    part_1 = check_numbers(numbers, preamble)

    # Part 2
    run = find_contiguous(numbers, part_1)
    part_2 = run |> extrema |> sum

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
