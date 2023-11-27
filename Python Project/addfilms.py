from connect1 import dbCursor, dbCon
# create a subroutine
def insert_tblFilms():
    # FilmId is auto increment field and not data input is required
 
    # ask user for input for Title, Rating, Genre
    filmTitle = input("Enter film title: ")
    filmYearReleased = input("Enter film year released: ")
    filmRating = input("Enter film rating: ")
    filmDuration = input("Enter film duration: ")
    filmGenre = input("Enter film genre: ")
 
    #insert data into the films table
    dbCursor.execute("INSERT INTO tblFilms(Title, YearReleased, Rating, Duration, Genre) VALUES(?,?,?,?,?)",(filmTitle, filmYearReleased, filmRating, filmDuration, filmGenre))
   
    # Commit the change
    dbCon.commit()
 
    # testing
    print(f"{filmTitle} inserted into songs table")
if __name__ == "__main__":
    insert_tblFilms()



 