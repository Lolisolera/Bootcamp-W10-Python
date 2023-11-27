 
# create a subroutine
def insert_films():
    # FilmId is auto increment field and not data input is required
 
    # ask user for input for Title, Rating, Genre
    filmTitle = input("Enter film Title: ")
    filmRating = input("Enter film Rating: ")
    filmGenre = input("Enter film Genre: ")
 
    #insert data into the films table
    dbCursor.execute("INSERT INTO films(Title, Rating, Genre) VALUES(?,?,?)",(filmTitle, filmRating, filmGenre))
   
    # Commit the change
    dbCon.commit()
 
    # testing
    print(f"{filmTitle} inserted into songs table")
if __name__ == "__main__":
    insert_films()