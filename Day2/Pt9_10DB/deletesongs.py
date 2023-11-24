from connect import *
 
def delete_songs():
    # use primary key to update a record
 
    idField = input("ENter the song ID of the record you want to delete: ")
 
    dbCursor.execute(f"DELETE FROM songs WHERE SongID= {idField}")
    # or
    # dbCursor.execute("DELETE FROM songs WHERE SongID=?", (idField,))
    dbCon.commit()
 
    print(f"{idField} deleted from songs table")
 
if __name__ == "__main__":
    delete_songs()