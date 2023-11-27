from connect1 import *
 
def delete_tblFilms():
    # use primary key to update a record
 
    idField = input("Enter the film ID of the record you want to delete: ")
 
    dbCursor.execute(f"DELETE FROM tblFilms WHERE FilmID= {idField}")
    # or
    # dbCursor.execute("DELETE FROM films WHERE FilmID=?", (idField,))
    dbCon.commit()
 
    print(f"{idField} deleted from tblFilms table")
 
if __name__ == "__main__":
    delete_tblFilms()