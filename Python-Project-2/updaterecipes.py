from connect import dbCursor, dbCon

def update_recipeBook():
    # Use primary key to update a record
    while True:
        idField = input("Enter the recipe ID of the recipe you want to update: ")
        if idField.isdigit():  # Check if the input is a valid number
            break
        else:
            print("Invalid input. Recipe ID should be a number.")

    allowed_field_names = ["RecipeName", "Ingredients", "Instructions"]
    while True:
        fieldName = input("Enter RecipeName, Ingredients, or Instructions as field name: ").title()
        if fieldName.lower() in map(str.lower, allowed_field_names):
            break
        else:
            print("Invalid input. Please enter one of the stated field names.")

    # Value for the field
    fieldValue = input(f"Enter the value for {fieldName} field: ")

    # Update a record 
    query = f"UPDATE recipeBook SET {fieldName} = ? WHERE recipeID = ?"
    dbCursor.execute(query, (fieldValue, idField))

    dbCon.commit()

    print(f"Record {idField} updated ")

if __name__ == "__main__":
    update_recipeBook()


    

    