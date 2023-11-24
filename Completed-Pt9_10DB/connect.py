import sqlite3 as sql # import sqlite3 mode and assigned an alias 'sql'

# from sqlite3 import connect

# use sqlite(sql) module to create and/or connect to a database
dbCon = sql.connect('Week10/Pt9_10DB/dfe2.db')


# create a cursor variable and assigned it to the cursor method to execute sql statements
dbCursor = dbCon.cursor()
