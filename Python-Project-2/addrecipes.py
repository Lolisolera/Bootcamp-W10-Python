from connect import dbCursor, dbCon

def insert_recipeBook():
    # RecipeId is an auto-increment field, and no data input is required

    # Ask the user for input for Recipe Name, Ingredients, Instructions
    while True:
        recipeName = input("Enter recipe name: ")
        if not recipeName.isnumeric():  # Check if the input contains only text
            break
        else:
            print("Invalid input. Please enter a valid recipe name (text only).")

    Ingredients = input("Enter recipe ingredients: ")
    Instructions = input("Enter recipe instructions: ")

    # Insert data into the recipe book table
    dbCursor.execute("INSERT INTO recipeBook(RecipeName, Ingredients, Instructions) VALUES(?,?,?)", (recipeName, Ingredients, Instructions))

    # Commit the change
    dbCon.commit()

    # Testing
    print(f"{recipeName} inserted into recipeBook table")

if __name__ == "__main__":
    insert_recipeBook()
