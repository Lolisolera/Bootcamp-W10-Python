from connect import *
 
# create a subroutine
def insert_songs():
    # SongId is auto increment field and not data input is required
 
    # ask user for input for Title, Artist, Genre
    songTitle = input("Enter song Title: ")
    songArtist = input("Enter song Artist: ")
    songGenre = input("Enter song Genre: ")
 
    #insert data into the songs table
    dbCursor.execute("INSERT INTO songs(Title, Artist, Genre) VALUES(?,?,?)",(songTitle, songArtist, songGenre))
   
    # Commit the change
    dbCon.commit()
 
    # testing
    print(f"{songTitle} inserted into songs table")
if __name__ == "__main__":
    insert_songs()


    #QUESTION FOR ABDUL:
    #How do we make changes to my table "songs", for example?
    #do we need to alter the table?delete data based on ID, etc?
    #Do we do that by creating a new file to make the changes,
    #e.g. altersongs.py?