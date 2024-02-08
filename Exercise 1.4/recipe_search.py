import pickle

def display_recipe(recipe):
    print(f"\nRecipe Name: {recipe['name']}")
    print(f"Cooking Time: {recipe['cooking_time']} minutes")
    print("Ingredients:")
    for ingredient in recipe['ingredients']:
        print(f"- {ingredient}")
    print(f"Difficulty: {recipe['difficulty']}")

def search_ingredient(data):
    print("\nAvailable Ingredients:")
    for idx, ingredient in enumerate(data['all_ingredients'], start=1):
        print(f"{idx}. {ingredient}")

    try:
        index = int(input("Enter the number corresponding to the ingredient you want to search: "))
        ingredient_searched = data['all_ingredients'][index - 1]
    except (ValueError, IndexError):
        print("Invalid input. Please enter a valid number.")
        return

    found_recipes = []

    for recipe in data['recipes_list']:
        if ingredient_searched in recipe['ingredients']:
            found_recipes.append(recipe)

    if found_recipes:
        print(f"\nRecipes containing {ingredient_searched}:")
        for idx, recipe in enumerate(found_recipes, start=1):
            display_recipe(recipe)
    else:
        print(f"\nNo recipes found containing {ingredient_searched}.")

def main():
    filename = input("Enter the filename: ")
    recipes_list, all_ingredients = load_data(filename)

    n = int(input("How many recipes would you like to enter? "))

    for _ in range(n):
        recipe = take_recipe()
        recipes_list.append(recipe)

        for ingredient in recipe['ingredients']:
            if ingredient not in all_ingredients:
                all_ingredients.append(ingredient)

    save_data(filename, {'recipes_list': recipes_list, 'all_ingredients': all_ingredients})

    print("\nRecipes List:")
    for idx, recipe in enumerate(recipes_list, start=1):
        print(f"Recipe {idx}: {recipe}")

    print("\nAll Ingredients List:", all_ingredients)

    search_option = input("Do you want to search for recipes by ingredient? (yes/no): ")
    if search_option.lower() == "yes":
        search_ingredient({'recipes_list': recipes_list, 'all_ingredients': all_ingredients})
    else:
        print("Exiting the program.")

if __name__ == "__main__":
    main()
