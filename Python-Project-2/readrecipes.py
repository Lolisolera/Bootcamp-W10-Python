from connect import *
 
# create subroutine
def read_recipeBook():
 
    # select all records
    dbCursor.execute("SELECT * FROM recipeBook")
 
    # fetch the selected records
    allRecords = dbCursor.fetchall()
 
    # loop through allRecords
    for eachRecord in allRecords:
        print(eachRecord)
 
if __name__ =="__main__":
    read_recipeBook()