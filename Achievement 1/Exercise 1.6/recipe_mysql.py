import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    user='python',
    passwd='bilja'
)

cursor = conn.cursor()
cursor.execute("USE nemanja_database")

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Recipes (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50),
        ingredients VARCHAR(255),
        cooking_time INT,
        difficulty VARCHAR(20)
    )
''')


def update_recipe(conn, cursor):
    print("Updating an existing recipe...")

def delete_recipe(conn, cursor):
    print("Deleting a recipe...")

def main_menu(conn, cursor):
    while True:
        print("\nMain Menu:")
        print("1. Create Recipe")
        print("2. Search Recipe by Ingredient")
        print("3. Update Recipe")
        print("4. Delete Recipe")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_recipe(conn, cursor)
        elif choice == "2":
            search_recipe(conn, cursor)
        elif choice == "3":
            update_recipe(conn, cursor)
        elif choice == "4":
            delete_recipe(conn, cursor)
        elif choice == "0":
            print("Exiting the program. Goodbye!")
            conn.commit()
            break
        else:
            print("Invalid choice. Please try again.")

def create_recipe(conn, cursor):
    print("\nCreating a new recipe...")

    name = input("Enter the name of the recipe: ")
    cooking_time = int(input("Enter the cooking time (in minutes): "))

    ingredients_input = input("Enter the ingredients (comma-separated): ")
    ingredients = [ingredient.strip() for ingredient in ingredients_input.split(',')]

    try:
        cursor.execute("""
            INSERT INTO Recipes (name, cooking_time, ingredients)
            VALUES (%s, %s, %s)
        """, (name, cooking_time, ', '.join(ingredients)))
        conn.commit()
        print("Recipe created successfully!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def calculate_difficulty(cooking_time, ingredients):
    difficulty = ""
    if cooking_time < 10 and len(ingredients) < 4:
        difficulty = "Easy"
    elif cooking_time < 10 and len(ingredients) >= 4:
        difficulty = "Medium"
    elif cooking_time >= 10 and len(ingredients) < 4:
        difficulty = "Intermediate"
    elif cooking_time >= 10 and len(ingredients) >= 4:
        difficulty = "Hard"
    return difficulty

def search_recipe(conn, cursor):
    try:
        cursor.execute("SELECT DISTINCT ingredients FROM Recipes")
        results = cursor.fetchall()

        if not results:
            print("No ingredients found.")
            return

        all_ingredients = []
        for row in results:
            ingredients_str = row[0]
            ingredients_list = ingredients_str.split(', ')
            all_ingredients.extend(ingredients_list)

        print("Available Ingredients:")
        for index, ingredient in enumerate(set(all_ingredients), start=1):
            print(f"{index}. {ingredient}")

        selected_index = int(input("Enter the number corresponding to the ingredient: "))

        if selected_index < 1 or selected_index > len(all_ingredients):
            print("Invalid selection.")
            return

        search_ingredient = all_ingredients[selected_index - 1]

        query = f"SELECT name, ingredients, cooking_time, difficulty FROM Recipes WHERE ingredients LIKE '%{search_ingredient}%'"
        cursor.execute(query)
        search_results = cursor.fetchall()

        if not search_results:
            print(f"No recipes found containing {search_ingredient}.")
        else:
            print("\nSearch Results:")
            for result in search_results:
                print(f"Name: {result[0]}\nIngredients: {result[1]}\nCooking Time: {result[2]} minutes\nDifficulty: {result[3]}\n")

    except mysql.connector.Error as err:
        print(f"Error: {err}")

def display_all_recipes(conn, cursor):
    try:
        cursor.execute("SELECT * FROM Recipes;")
        recipes = cursor.fetchall()

        if recipes:
            print("All Recipes:")
            print("{:<5} {:<50} {:<255} {:<10} {:<20}".format("ID", "Name", "Ingredients", "Cooking Time", "Difficulty"))
            for recipe in recipes:
                print("{:<5} {:<50} {:<255} {:<10} {:<20}".format(recipe[0], recipe[1], recipe[2], recipe[3], recipe[4]))
        else:
            print("No recipes found.")
    except Exception as e:
        print(f"Error displaying recipes: {e}")

def delete_recipe(conn, cursor):
    try:
        display_all_recipes(conn, cursor)

        recipe_id_to_delete = input("Enter the ID of the recipe you want to delete: ")

        delete_query = f"DELETE FROM Recipes WHERE id = {recipe_id_to_delete};"
        cursor.execute(delete_query)

        conn.commit()

        print(f"Recipe with ID {recipe_id_to_delete} has been deleted.")
    except Exception as e:
        print(f"Error deleting recipe: {e}")

# This line executes the main_menu function when the script is run
if __name__ == "__main__":
    main_menu(conn, cursor)
