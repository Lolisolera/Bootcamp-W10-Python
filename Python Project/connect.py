import sqlite3 as sql #import sqlite3 mode and assigned as alias'sql'

#from sqlite3 import connect 

#use sqlite (sql) module to create and/or connect to a database
dbCon = sql.connect('Python Project/filmflix.db')


#create a cursor variable and assigned it to the cursor method to execute sql statements
dbCursor = dbCon.cursor()