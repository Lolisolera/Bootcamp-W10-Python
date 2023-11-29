from connect import *

def update_songs():
    # Use primary key to update a record
    idField = input("Enter the song ID of the record you want to update: ")

    # Field to update 
    fieldName = input("Enter Title or Artist or Genre as field name: ").title()

    # Value for the field
    fieldValue = input(f"Enter the value for {fieldName} field: ")

      # (1, 'Bad', 'MJ', 'Pop')

   # "method 1"
    fieldValue = "'"+fieldValue+"'"
    
    # "method 2"
    # tuple(fieldValue)
    # print(fieldvalue)
    # num = "2"
    # int(mum)

    # Update a record 
    query = f"UPDATE songs SET {fieldName} = ? WHERE SongID = ?"
    dbCursor.execute(query, (fieldValue, idField))

    dbCon.commit()

    print(f"Record {idField} updated ")

if __name__ == "__main__":
    update_songs()

