# Rain Risk
#
# Advent of Code 2020, day 12
# Solution by Geir Arne Hjelle, 2020-12-12

using Pipe


Directions = Dict('N' => [1, 0], 'E' => [0, 1], 'S' => [-1, 0], 'W' => [0, -1])
Bearings = Dict(0 => 'N', 90 => 'E', 180 => 'S', 270 => 'W')
Rotations = Dict(
    90 => (n, e) -> (-e, n),
    180 => (n, e) -> (-n, -e),
    270 => (n, e) -> (e, -n),
)

struct Position
    northing::Int32
    easting::Int32
    bearing::Int16
    waypoint_north::Int32
    waypoint_east::Int32

    # Initialize position without waypoint
    function Position(northing::Number, easting::Number, bearing::Number)
        new(northing, easting, (bearing + 360) % 360, 0, 0)
    end

    # Initialize position with waypoint
    function Position(northing::Number, easting::Number, bearing::Number, wpn::Number, wpe::Number)
        new(northing, easting, (bearing + 360) % 360, wpn, wpe)
    end
    
    # Initialize position relative to previous
    function Position(position::Position, dn::Number, de::Number, db::Number)
        new(
            position.northing + dn,
            position.easting + de,
            (position.bearing + db + 360) % 360,
            position.waypoint_north,
            position.waypoint_east,
        )
    end

    # Initialize position with waypoint by rotating waypoint
    function Position(position::Position, dn::Number, de::Number, rotation)
        wpn, wpe = rotation(position.waypoint_north, position.waypoint_east)
        new(
            position.northing + dn,
            position.easting + de,
            position.bearing,
            wpn,
            wpe,
        )
    end

    # Initialize position with waypoint relative to previous position
    function Position(position::Position, dn::Number, de::Number, dwpn::Number, dwpe::Number)
        new(
            position.northing + dn,
            position.easting + de,
            position.bearing,
            position.waypoint_north + dwpn,
            position.waypoint_east + dwpe,
        )
    end
end

struct Instruction
    action::Char
    value::Int32

    # Parse instruction from a line of text input
    function Instruction(instruction::String)
        new(instruction[1], @pipe instruction[2:end] |> parse(Int32, _))
    end
end


function move_ship(position, instruction)
    if instruction.action == 'R'
        Position(position, 0, 0, instruction.value)
    elseif instruction.action == 'L'
        Position(position, 0, 0, -instruction.value)
    elseif instruction.action == 'F'
        Position(
            position,
            (Directions[Bearings[position.bearing]] * instruction.value)...,
            0,
        )
    else
        Position(
            position,
            (Directions[instruction.action] * instruction.value)...,
            0,
        )
    end
end


function move_waypoint(position, instruction)
    if instruction.action == 'R'
        Position(position, 0, 0, Rotations[instruction.value])
    elseif instruction.action == 'L'
        Position(position, 0, 0, Rotations[360 - instruction.value])
    elseif instruction.action == 'F'
        Position(
            position,
            ([position.waypoint_north, position.waypoint_east] * instruction.value)...,
            0,
        )
    else
        Position(
            position,
            [0, 0]...,
            (Directions[instruction.action] * instruction.value)...,
        )
    end
end


function manhattan_distance(position)
    [position.northing, position.easting] .|> abs |> sum
end


# Solve the problem for one file
function solve(filename)
    println("\n$(filename)")

    # Read from file
    input = open(filename) do fid
        fid |> readlines .|> Instruction
    end

    # Part 1
    @pipe (
        input
        |> foldl(move_ship, _, init=Position(0, 0, 90))
        |> manhattan_distance
        |> println
    )

    # Part 2
    @pipe (
        input
        |> foldl(move_waypoint, _, init=Position(0, 0, 90, 1, 10))
        |> manhattan_distance
        |> println
    )
end


# Solve the problem for each file
ARGS .|> solve
