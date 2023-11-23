from connect import *

def update_songs():
    # use primary key to update a record

    idField = input("ENter the song ID of the record you want to update: ")

    # field to update 
    fieldName = input("Enter Title or Artist or Genre as field name: ").title()

    fieldValue = input(f"Enter the value for {fieldName} field: ")

    
    # (1, 'Bad', 'MJ', 'Pop')

    "method 1"
    fieldValue = "'"+fieldValue+"'"
    
    # "method 2"
    # tuple(fieldValue)
    # print(fieldvalue)
    # num = "2"
    # int(mum)

    # update a record 
    dbCursor.execute(f"UPDATE songs SET {fieldName}  = {fieldValue} WHERE SongID = {idField} ")

    dbCon.commit()

    print(f"Record {idField} updated ")

if __name__ == "__main__":
    update_songs()
