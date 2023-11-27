from connect import *
 
# create subroutine
def read_tblFilms():
 
    # select all records
    dbCursor.execute("SELECT * FROM tblFilms")
 
    # fetch the selected records
    allRecords = dbCursor.fetchall()
 
    # loop through allRecords
    for eachRecord in allRecords:
        print(eachRecord)
 
if __name__ =="__main__":
    read_tblFilms()