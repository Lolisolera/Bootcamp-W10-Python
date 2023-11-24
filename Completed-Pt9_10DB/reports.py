from connect import *

# create subroutine
def reports():
    # dbCursor.execute("SELECT Artist, Title FROM songs ORDER BY Artist DESC ")
    dbCursor.execute("SELECT * FROM songs WHERE Genre = 'rock' OR Genre = 'pop' ")
    # dbCursor.execute("SELECT  * FROM songs WHERE Genre LIKE 'r%' ")
    # dbCursor.execute("SELECT * FROM songs WHERE Genre NOT LIKE 'r%' ")
    # dbCursor.execute("SELECT  * FROM songs WHERE Genre LIKE '%r%' ")
    # dbCursor.execute("SELECT ")
    # dbCursor.execute("SELECT ")
    # dbCursor.execute("SELECT ")
    # dbCursor.execute("SELECT ")
    # dbCursor.execute("SELECT ")
    # dbCursor.execute("SELECT ")

    reportsData = dbCursor.fetchall()

    for records in reportsData:
        print(records)
if __name__ == "__main__":
    reports()