dbCursor.execute("""
CREATE TABLE tblFilms
    (
    filmID integer,
    title text,
    yearReleased integer,
    rating text,
    duration integer,
    genre text,
    primary key (filmID)
  )""")