from connect import dbCursor, dbCon
# create a subroutine
def insert_recipeBook():
    # RecipeId is auto increment field and not data input is required
 
    # ask user for input for Recipe Name, Ingredients, Instructions
    recipeName = input("Enter recipe name: ")
    Ingredients = input("Enter recipe ingredients: ")
    Instructions = input("Enter recipe instructions: ")
   
 
    #insert data into the recipe book table
    dbCursor.execute("INSERT INTO recipeBook(recipeName, Ingredients, Instructions) VALUES(?,?,?)",(recipeName, Ingredients, Instructions ))
   
    # Commit the change
    dbCon.commit()
 
    # testing
    print(f"{recipeName} inserted into recipeBook table")
if __name__ == "__main__":
    insert_recipeBook()