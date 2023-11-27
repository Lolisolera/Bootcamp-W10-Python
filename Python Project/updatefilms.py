from connect import dbCursor, dbCon

def update_tblFilms():
    # Use primary key to update a record
    idField = input("Enter the film ID of the record you want to update: ")

    # Field to update 
    fieldName = input("Enter title or year released or rating or duration or genre as field name: ").title()

    # Value for the field
    fieldValue = input(f"Enter the value for {fieldName} field: ")

      # (1, 'Lost', '1999', 'PG', '90', 'Adventure')

   # "method 1"
    fieldValue = fieldValue
    
    # "method 2"
    # tuple(fieldValue)
    # print(fieldvalue)
    # num = "2"
    # int(mum)

    # Update a record 
    query = f"UPDATE tblFilms SET {fieldName} = ? WHERE filmID = ?"
    dbCursor.execute(query, (fieldValue, idField))

    dbCon.commit()

    print(f"Record {idField} updated ")

if __name__ == "__main__":
    update_tblFilms()
