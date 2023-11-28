from connect import dbCursor, dbCon
 
# create subroutine
def reports():
    #dbCursor.execute("SELECT title FROM recipeBook ORDER BY title DESC ")
    #dbCursor.execute("SELECT * FROM recipeBook WHERE recipeName = 'Rice pudding' OR 'Chocolate Cake' ")
    #dbCursor.execute("SELECT * FROM trecipeBook  WHERE recipeName LIKE 'r%' ")
    dbCursor.execute("SELECT * FROM recipeBook  WHERE recipeName NOT LIKE 'r%' ")
    #dbCursor.execute("SELECT * FROM recipeBook  WHERE recipeName LIKE '%r' ")
    reportsData = dbCursor.fetchall()
 
    for records in reportsData:
        print(records)
if __name__ == "__main__":
    reports()