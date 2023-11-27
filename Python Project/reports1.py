from connect1 import dbCursor, dbCon
 
# create subroutine
def reports1():
    #dbCursor.execute("SELECT title FROM tblFilms ORDER BY title DESC ")
    #dbCursor.execute("SELECT * FROM tblFilms WHERE Genre = 'Crime' OR Genre ='Action' ")
    #dbCursor.execute("SELECT * FROM tblFilms WHERE Genre LIKE 'r%' ")
    dbCursor.execute("SELECT * FROM tblFilms WHERE Genre NOT LIKE 'r%' ")
    #dbCursor.execute("SELECT * FROM tblFilms WHERE genre LIKE '%r' ")
    reportsData = dbCursor.fetchall()
 
    for records in reportsData:
        print(records)
if __name__ == "__main__":
    reports1()