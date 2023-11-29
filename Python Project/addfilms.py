from connect1 import dbCursor, dbCon
# create a subroutine
def insert_tblFilms():
    # FilmId is auto increment field and not data input is required
 
    # ask user for input for Title, Rating, Genre
    while True:
        filmTitle = input("Enter film title: ")
        if not filmTitle.isnumeric():  # Check if the input contains only text
            break
        else:
            print("Invalid input. Please enter a valid film title(text only).")

    filmYearReleased = input("Enter film year released: ")

    while True:
       filmRating = input("Enter film rating: ")
       if not filmRating.isnumeric():  # Check if the input contains only text
         break
       else:
            print("Invalid input. Please enter a valid film rating(text only).")

    filmDuration = input("Enter film duration: ")


    while True:
      filmGenre = input("Enter film genre: ")
      if not filmGenre.isnumeric():  # Check if the input contains only text
         break
      else:
            print("Invalid input. Please enter a valid film genre(text only).")
 
    #insert data into the films table
    dbCursor.execute("INSERT INTO tblFilms(Title, YearReleased, Rating, Duration, Genre) VALUES(?,?,?,?,?)",(filmTitle, filmYearReleased, filmRating, filmDuration, filmGenre))
   
    # Commit the change
    dbCon.commit()
 
    # testing
    print(f"{filmTitle} inserted into FilmFlix table")
if __name__ == "__main__":
    insert_tblFilms()



  
   