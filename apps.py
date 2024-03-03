recipes= []
def add_recipe():
    name = input("Enter recipe name: ")
    ingredients = input("Enter ingredients (comma-separated): ").split(",")
    instructions = input("Enter instructions: ")
    recipe = {"name": name, "ingredients": ingredients, "instructions": instructions}
    recipes.append(recipe)
    print(f"Recipe '{name}' added successfully!")
def delete_recipe():
    name = input("Enter recipe name to delete: ")
    for recipe in recipes:
        if recipe["name"] == name:
            recipes.remove(recipe)
            print(f"Recipe '{name}' deleted successfully!")
            break
    else:
        print(f"Recipe '{name}' not found.")

def search_recipe():
    name = input("Enter recipe name to search: ")
    for recipe in recipes:
        if recipe["name"] == name:
            print(f"Recipe '{name}':")
            print(f"Ingredients: {', '.join(recipe['ingredients'])}")
            print(f"Instructions: {recipe['instructions']}")
            break
    else:
        print(f"Recipe '{name}' not found.")

def display_recipes():
    print("\nAll Recipes:")
    for recipe in recipes:
        print(f"*{recipe['name']}")

while True:
    print("\nRecipe Book Menu:")
    print("1. Add Recipe")
    print("2. Delete Recipe")
    print("3. Search Recipe")
    print("4. Display All Recipes")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        add_recipe()
    elif choice == "2":
        delete_recipe()
    elif choice == "3":
        search_recipe()
    elif choice == "4":
        display_recipes()
    elif choice == "5":
        print("Exiting. Have a great day!")
        break
    else:
        print("Invalid choice. Please select a valid option.")