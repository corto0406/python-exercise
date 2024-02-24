recipe_1 = {
    "name": "Tea",
    "cooking_time": 5,
    "ingredients": ["Tea leaves", "Sugar", "Water"]
}

recipe_2 = {
    "name": "Spaghetti Bolognese",
    "cooking_time": 30,
    "ingredients": ["Spaghetti", "Ground beef", "Tomato sauce", "Onion", "Garlic"]
}

recipe_3 = {
    "name": "Vegetarian Stir-Fry",
    "cooking_time": 20,
    "ingredients": ["Broccoli", "Carrots", "Bell peppers", "Tofu", "Soy sauce"]
}

recipe_4 = {
    "name": "Chicken Curry",
    "cooking_time": 45,
    "ingredients": ["Chicken", "Curry powder", "Coconut milk", "Potatoes", "Coriander"]
}

recipe_5 = {
    "name": "Chocolate Chip Cookies",
    "cooking_time": 15,
    "ingredients": ["Flour", "Butter", "Sugar", "Chocolate chips", "Vanilla extract"]
}

all_recipes = [recipe_1, recipe_2, recipe_3, recipe_4, recipe_5]

ingredients_recipe_1 = all_recipes[0]["ingredients"]
ingredients_recipe_2 = all_recipes[1]["ingredients"]
ingredients_recipe_3 = all_recipes[2]["ingredients"]
ingredients_recipe_4 = all_recipes[3]["ingredients"]
ingredients_recipe_5 = all_recipes[4]["ingredients"]

print("Ingredients for Recipe 1:", ingredients_recipe_1)
print("Ingredients for Recipe 2:", ingredients_recipe_2)
print("Ingredients for Recipe 3:", ingredients_recipe_3)
print("Ingredients for Recipe 4:", ingredients_recipe_4)
print("Ingredients for Recipe 5:", ingredients_recipe_5)
