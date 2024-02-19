from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql://python:bilja@localhost/nemanja_database")

Base = declarative_base()

class Recipe(Base):
    __tablename__ = 'final_recipes'
    id = Column(Integer, Sequence('recipe_id_seq'), primary_key=True)
    name = Column(String(50))
    ingredients = Column(String(255))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))

    def __repr__(self):
        return f"<Recipe(id={self.id}, name={self.name}, difficulty={self.difficulty})>"

    def __str__(self):
        return (
            f"Recipe ID: {self.id}\n"
            f"Name: {self.name}\n"
            f"Difficulty: {self.difficulty}\n"
            f"Ingredients: {', '.join(self.return_ingredients_as_list())}\n"
            f"Cooking Time: {self.cooking_time} minutes"
        )

    def calculate_difficulty(self):
        if self.cooking_time < 10 and len(self.return_ingredients_as_list()) < 4:
            self.difficulty = "Easy"
        elif self.cooking_time < 10 and len(self.return_ingredients_as_list()) >= 4:
            self.difficulty = "Medium"
        elif self.cooking_time >= 10 and len(self.return_ingredients_as_list()) < 4:
            self.difficulty = "Intermediate"
        elif self.cooking_time >= 10 and len(self.return_ingredients_as_list()) >= 4:
            self.difficulty = "Hard"

    def return_ingredients_as_list(self):
        if not self.ingredients:
            return []
        return [ingredient.strip() for ingredient in self.ingredients.split(',')]

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def create_recipe():
    name, ingredients, cooking_time = collect_recipe_details()

    # Validate inputs
    if not validate_input(name, max_length=50, alpha=True) or \
            not validate_input(cooking_time, numeric=True):
        print("Invalid input. Please check your recipe details.")
        return

    recipe_entry = Recipe(name=name, ingredients=ingredients, cooking_time=int(cooking_time))
    recipe_entry.calculate_difficulty()
    session.add(recipe_entry)
    session.commit()
    print("Recipe created successfully!")

def view_all_recipes():
    recipes = session.query(Recipe).all()

    if not recipes:
        print("No recipes found in the database.")
        return

    for recipe in recipes:
        print(recipe)

def search_by_ingredients():
    if session.query(Recipe).count() == 0:
        print("No recipes found in the database.")
        return

    results = session.query(Recipe.ingredients).all()
    all_ingredients = []

    for result in results:
        ingredients_str = result[0]
        ingredients_list = ingredients_str.split(', ')
        all_ingredients.extend(ingredients_list)

    all_ingredients = set(all_ingredients)

    print("All Ingredients:")
    for i, ingredient in enumerate(all_ingredients, start=1):
        print(f"{i}. {ingredient}")

    selected_numbers = input("Enter the numbers of ingredients (separated by spaces): ")
    selected_numbers = [int(num) for num in selected_numbers.split()]

    if not all(1 <= num <= len(all_ingredients) for num in selected_numbers):
        print("Invalid ingredient number. Please try again.")
        return

    selected_ingredients = [list(all_ingredients)[num - 1] for num in selected_numbers]
    print("Selected Ingredients:", ', '.join(selected_ingredients))

    search_ingredients = selected_ingredients
    conditions = []

    for ingredient in search_ingredients:
        like_term = f"%{ingredient}%"
        conditions.append(Recipe.ingredients.like(like_term))

    recipes = session.query(Recipe).filter(*conditions).all()

    if not recipes:
        print("No recipes found with the selected ingredients.")
    else:
        print("\nRecipes Found:")
        for recipe in recipes:
            print(recipe)

def edit_recipe():
    if session.query(Recipe).count() == 0:
        print("No recipes found in the database.")
        return

    results = session.query(Recipe.id, Recipe.name).all()

    print("\nRecipes Available:")
    for result in results:
        recipe_id, recipe_name = result
        print(f"{recipe_id}. {recipe_name}")

    recipe_id = int(input("Enter the ID of the recipe you want to edit: "))
    recipe_to_edit = session.query(Recipe).filter(Recipe.id == recipe_id).first()

    if not recipe_to_edit:
        print("Recipe not found.")
        return

    print(f"\nCurrent Details for Recipe ID {recipe_id}:")
    print(recipe_to_edit)

    print("\nAttributes:")
    print("1. Name")
    print("2. Ingredients")
    print("3. Cooking Time")

    attribute_choice = input("Enter the number corresponding to the attribute you want to edit: ")

    if attribute_choice == "1":
        new_name = input("Enter the new name for the recipe: ")
        recipe_to_edit.name = new_name
    elif attribute_choice == "2":
        new_ingredients = collect_ingredients()
        recipe_to_edit.ingredients = new_ingredients
    elif attribute_choice == "3":
        new_cooking_time = input("Enter the new cooking time (in minutes): ")
        if not validate_input(new_cooking_time, numeric=True):
            print("Invalid input for cooking time. Please try again.")
            return
        recipe_to_edit.cooking_time = int(new_cooking_time)
    else:
        print("Invalid attribute choice. Exiting update.")
        return

    recipe_to_edit.calculate_difficulty()
    session.commit()
    print("Recipe updated successfully!")

def delete_recipe():
    if session.query(Recipe).count() == 0:
        print("No recipes found in the database.")
        return

    results = session.query(Recipe.id, Recipe.name).all()

    print("\nRecipes Available:")
    for result in results:
        recipe_id, recipe_name = result
        print(f"{recipe_id}. {recipe_name}")

    recipe_id_to_delete = int(input("Enter the ID of the recipe you want to delete: "))

    if session.query(Recipe).filter(Recipe.id == recipe_id_to_delete).count() == 0:
        print("Invalid recipe ID. No such recipe found.")
        return

    recipe_to_delete = session.query(Recipe).filter(Recipe.id == recipe_id_to_delete).first()

    confirmation = input(f"Are you sure you want to delete {recipe_to_delete.name}? (yes/no): ")

    if confirmation.lower() == "yes":
        session.delete(recipe_to_delete)
        session.commit()
        print("Recipe deleted successfully!")
    else:
        print("Delete operation canceled.")

def collect_recipe_details():
    name = input("Enter the name of the recipe: ")
    ingredients = collect_ingredients()
    cooking_time = input("Enter the cooking time (in minutes): ")
    return name, ingredients, cooking_time

def collect_ingredients():
    ingredients = []
    num_ingredients = int(input("How many ingredients would you like to enter? "))

    for _ in range(num_ingredients):
        ingredient = input("Enter an ingredient: ")
        ingredients.append(ingredient)

    return ', '.join(ingredients)

def validate_input(line, max_length=None, numeric=False, alpha=False):
    if max_length is not None and len(line) > max_length:
        return False
    if numeric and not line.replace(".", "").isdigit():
        return False
    if alpha and not line.isalpha():
        return False
    return True


def main():
    while True:
        print("\nMain Menu:")
        print("1. Create Recipe")
        print("2. View All Recipes")
        print("3. Search Recipes by Ingredients")
        print("4. Edit Recipe")
        print("5. Delete Recipe")
        print("6. Quit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            create_recipe()

        elif choice == "2":
            view_all_recipes()

        elif choice == "3":
            search_by_ingredients()

        elif choice == "4":
            edit_recipe()

        elif choice == "5":
            delete_recipe()

        elif choice.lower() == "quit" or choice == "6":
            print("Exiting the program. Goodbye!")
            session.close()
            engine.dispose()
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
