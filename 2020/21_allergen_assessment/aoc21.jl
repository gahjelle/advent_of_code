# Allergen Assessment
#
# Advent of Code 2020, day 21
# Solution by Geir Arne Hjelle, 2020-12-21

using Pipe


function parse_food(lines)
    ingredients, allergens = [], []
    for line in lines
        m = match(r"(?<ingredients>.+) \(contains (?<allergens>.+)\)", line)
        food_ingredients = Set()
        for ingredient in split(m[:ingredients], " ")
            push!(food_ingredients, ingredient)
        end
        push!(ingredients, food_ingredients)

        food_allergens = Set()
        for allergen in split(m[:allergens], ", ")
            push!(food_allergens, allergen)
        end
        push!(allergens, food_allergens)
    end
    (ingredients = ingredients, allergens = allergens)
end


function find_candidates(ingredients, allergens)
    candidates = Dict()
    for allergen in foldl(union, allergens)
        ingredient_candidates = foldl(union, ingredients)
        for (food_ingredients, food_allergens) in zip(ingredients, allergens)
            if allergen ∈ food_allergens
                ingredient_candidates = intersect(ingredient_candidates, food_ingredients)
            end
        end
        candidates[allergen] = ingredient_candidates
    end
    
    candidates
end


function prune_candidates(candidates)
    allergens = Dict(a => i |> first for (a, i) in candidates if i |> length == 1)
    leftover = filter(c -> c.second |> length > 1, candidates)

    while !isempty(leftover)
        for (allergen, ingredients) in leftover
            unknown = setdiff(ingredients, allergens |> values)
            if unknown |> length == 1
                allergens[allergen] = unknown |> first
                pop!(leftover, allergen)
            end
        end
    end
    
    allergens
end


function list_safe_ingredients(ingredients, allergens)
    [i for fi in ingredients for i in fi if i ∉ allergens |> values]
end


function list_dangerous_ingredients(allergens)
    @pipe allergens |> collect |> sort |> map(a -> a.second, _)
end


# Solve the problem for one file
function solve(filename)
    println("\n$(filename)")

    # Read from file
    ingredients, allergens = open(filename) do fid
        fid |> readlines |> parse_food
    end

    # Part 1
    allergens_by_ingredient = find_candidates(ingredients, allergens) |> prune_candidates
    list_safe_ingredients(ingredients, allergens_by_ingredient) |> length |> println

    # Part 2
    @pipe list_dangerous_ingredients(allergens_by_ingredient) |> join(_, ",") |> println
end


# Solve the problem for each file
ARGS .|> solve
