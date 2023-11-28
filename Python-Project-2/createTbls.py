from connect import * 

dbCursor.execute("""
CREATE TABLE "recipeBook" (
    "RecipeID"    INTEGER NOT NULL UNIQUE,
    "RecipeName" TEXT,
    "Ingredients" TEXT,
    "Instructions" TEXT,
    PRIMARY KEY("RecipeID" AUTOINCREMENT)
)""")

