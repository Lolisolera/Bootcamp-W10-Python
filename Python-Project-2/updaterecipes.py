from connect import dbCursor, dbCon

def update_recipeBook():
    #Use primary key to update a record
    while True:
        idField = input("Enter the recipe ID of the record you want to update: ")
        if idField.isdigit():  # Check if the input is a valid number
            break
        else:
            print("Invalid input. Recipe ID should be a number.")

    # Field to update 
    fieldName = input("Enter RecipeName or Ingredients or Instructions as field name: ").title()

    # Value for the field
    fieldValue = input(f"Enter the value for {fieldName} field: ")

      # (1, 'Chocolate Cake', 'Flour, Sugar, Cocoa Powder, Eggs, Milk', '1. Mix dry ingredients. 2. Add wet ingredients. 3. Bake at 350°F.')

   # "method 1"
    fieldValue = fieldValue
    
    # "method 2"
    # tuple(fieldValue)
    # print(fieldvalue)
    # num = "2"
    # int(mum)

    # Update a record 
    query = f"UPDATE recipeBook SET {fieldName} = ? WHERE recipeID = ?"
    dbCursor.execute(query, (fieldValue, idField))

    dbCon.commit()

    print(f"Record {idField} updated ")

if __name__ == "__main__":
    update_recipeBook()
    