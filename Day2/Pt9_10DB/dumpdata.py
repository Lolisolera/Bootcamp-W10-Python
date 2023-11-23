from connect import *
 
def dataDump():
    # load the sql script from file
    with open("Week10/Pt9_10DB/songs.sql") as songsData:
        insertScriptdata = songsData.read()
 
 
        #cursor.execure script
        dbCursor.executescript(insertScriptdata)
dataDump()