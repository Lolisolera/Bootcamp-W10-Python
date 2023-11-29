from connect1 import dbCursor, dbCon

def update_tblFilms():
    # Use primary key to update a record
    while True:
        idField = input("Enter the film ID of the record you want to update: ")
        if idField.isdigit():  # Check if the input is a valid number
            break
        else:
            print("Invalid input. Film ID should be a number.")

    allowed_field_names = ["title", "year released", "rating", "duration", "genre"]
    while True:
        fieldName = input("Enter title, year released, rating, duration, or genre as field name: ").lower()
        if fieldName in allowed_field_names:
            break
        else:
            print("Invalid input. Please enter one of the stated field names.")

    # Value for the field
    fieldValue = input(f"Enter the value for {fieldName} field: ")

    # Update a record 
    query = f"UPDATE tblFilms SET {fieldName} = ? WHERE filmID = ?"
    dbCursor.execute(query, (fieldValue, idField))

    dbCon.commit()

    print(f"Record {idField} updated ")

if __name__ == "__main__":
    update_tblFilms()

