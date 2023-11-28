from connect import *
 
def mutltipleInsert():
 
    # create a list []
    recipeData = [
 
    ('Smells Like Teen Spirit', 'Michael Davis', 'metal'),
    ('Hey Ya!', 'John Smith', 'gospel'),
    ('Rolling in the Deep', 'Sophia Martinez', 'r&b'),
    ('Imagine', 'Emma Taylor', 'country'),
    ('Smells Like Teen Spirit', 'Michael Davis', 'indie'),
    ('Rolling in the Deep', 'John Smith', 'metal'),
    ('Don''t Stop Believin''', 'Sophia Martinez', 'r&b'),
    ('Hey Ya!', 'Daniel Thompson', 'folk'),
    ]
 
    dbCursor.executemany("INSERT INTO recipeBook (RecipeName, Ingredients, Instructions) VALUES(?,?,?)",recipeData)
   
    # Commit the change
    dbCon.commit()
 
    print(recipeData[1], "Added to recipeBook table")
 
mutltipleInsert()