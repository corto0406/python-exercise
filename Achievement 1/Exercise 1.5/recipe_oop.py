class Recipe:
    all_ingredients = set()

    def __init__(self, name, cooking_time, ingredients=None):
        self.name = name
        self.cooking_time = cooking_time
        self.ingredients = ingredients or []
        self.difficulty = None
        self.calculate_difficulty()
        self.update_all_ingredients()

    def add_ingredients(self, *ingredients):
        self.ingredients.extend(ingredients)
        self.update_all_ingredients()

    def calculate_difficulty(self):
        if self.cooking_time < 10 and len(self.ingredients) < 4:
            self.difficulty = "Easy"
        elif self.cooking_time < 10 and len(self.ingredients) >= 4:
            self.difficulty = "Medium"
        elif self.cooking_time >= 10 and len(self.ingredients) < 4:
            self.difficulty = "Intermediate"
        else:
            self.difficulty = "Hard"

    def search_ingredient(self, ingredient):
        return ingredient in self.ingredients

    def update_all_ingredients(self):
        Recipe.all_ingredients.update(self.ingredients)

    def __str__(self):
        return f"Recipe: {self.name}\nCooking Time: {self.cooking_time} minutes\nIngredients: {', '.join(self.ingredients)}\nDifficulty: {self.difficulty}"

def recipe_search(data, search_term):
    for recipe in data:
        if recipe.search_ingredient(search_term):
            print(recipe)


tea = Recipe(name="Tea", cooking_time=5, ingredients=["Tea Leaves", "Sugar", "Water"])
coffee = Recipe(name="Coffee", cooking_time=5, ingredients=["Coffee Powder", "Sugar", "Water"])
cake = Recipe(name="Cake", cooking_time=50, ingredients=["Sugar", "Butter", "Eggs", "Vanilla Essence", "Flour", "Baking Powder", "Milk"])
banana_smoothie = Recipe(name="Banana Smoothie", cooking_time=5, ingredients=["Bananas", "Milk", "Peanut Butter", "Sugar", "Ice Cubes"])

recipes_list = [tea, coffee, cake, banana_smoothie]

recipe_search(recipes_list, "Water")
recipe_search(recipes_list, "Sugar")
recipe_search(recipes_list, "Bananas")
