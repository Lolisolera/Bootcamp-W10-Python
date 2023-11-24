from connect import *

# create subroutine
def read_songs():

    # select all records
    dbCursor.execute("SELECT * FROM songs")

    # dbCursor.execute("SELECT * FROM songs WHERE SongID = 1 ")

    # fetch the selected records
    allRecords = dbCursor.fetchall()

    # loop through allRecords
    for eachRecord in allRecords:
        print(eachRecord)

if __name__ =="__main__":
    read_songs()
