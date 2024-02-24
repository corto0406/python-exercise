recipes_list = []
ingredients_list = set()

def take_recipe():
    name = input("Enter recipe name: ")
    cooking_time = int(input("Enter cooking time (in minutes): "))
    ingredients = input("Enter ingredients (comma-separated): ").split(',')
    
    recipe = {'name': name, 'cooking_time': cooking_time, 'ingredients': ingredients}
    
    return recipe

n = int(input("How many recipes would you like to enter? "))

for _ in range(n):
    recipe = take_recipe()
    recipes_list.append(recipe)
    ingredients_list.update(recipe['ingredients'])

print("\nRecipes:")
for idx, recipe in enumerate(recipes_list, start=1):
    print(f"Recipe {idx}: {recipe}")

print("\nUnique Ingredients:", ingredients_list)

recipes_list = []

for _ in range(n):
    recipe = take_recipe()
    
    for ingredient in recipe['ingredients']:
        if ingredient not in ingredients_list:
            ingredients_list.add(ingredient)

    recipes_list.append(recipe)

print("\nRecipes List:", recipes_list)
print("Ingredients List:", ingredients_list)

for recipe in recipes_list:
    cooking_time = recipe['cooking_time']
    num_ingredients = len(recipe['ingredients'])

    if cooking_time < 10 and num_ingredients < 4:
        difficulty = "Easy"
    elif cooking_time < 10 and num_ingredients >= 4:
        difficulty = "Medium"
    elif cooking_time >= 10 and num_ingredients < 4:
        difficulty = "Intermediate"
    else:
        difficulty = "Hard"

    recipe['difficulty'] = difficulty

for recipe in recipes_list:
    print("Recipe:", recipe)

for i, recipe in enumerate(recipes_list, 1):
    print(f"Recipe {i}:")
    print(f"Name: {recipe['name']}")
    print(f"Cooking Time: {recipe['cooking_time']} minutes")
    print("Ingredients:")
    for ingredient in recipe['ingredients']:
        print(f"- {ingredient}")
    print(f"Difficulty: {recipe['difficulty']}")
    print()

ingredients_list = []

for recipe in recipes_list:
    for ingredient in recipe['ingredients']:
        ingredients_list.append(ingredient)

sorted_list = [i for i in sorted(ingredients_list)]

print("\nAll Ingredients:")
for idx, ingredient in enumerate(sorted_list, start=1):
    print(f"{idx}. {ingredient}")
