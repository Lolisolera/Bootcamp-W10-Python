from connect import *
 
def delete_recipeBook():
    # use primary key to update a record
 
    idField = input("Enter the recipe ID of the record you want to delete: ")
 
    dbCursor.execute(f"DELETE FROM recipeBook WHERE recipeID= {idField}")
    # or
    # dbCursor.execute("DELETE FROM recipeBook WHERE recipeID=?", (idField,))
    dbCon.commit()
 
    print(f"{idField} deleted from recipeBook table")
 
if __name__ == "__main__":
    delete_recipeBook()