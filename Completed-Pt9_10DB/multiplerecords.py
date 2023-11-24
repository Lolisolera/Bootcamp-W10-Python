from connect import *

def mutltipleInsert():

    # create a list []
    songsData = [

    ('Smells Like Teen Spirit', 'Michael Davis', 'metal'),
    ('Hey Ya!', 'John Smith', 'gospel'),
    ('Rolling in the Deep', 'Sophia Martinez', 'r&b'),
    ('Imagine', 'Emma Taylor', 'country'),
    ('Smells Like Teen Spirit', 'Michael Davis', 'indie'),
    ('Rolling in the Deep', 'John Smith', 'metal'),
    ('Don''t Stop Believin''', 'Sophia Martinez', 'r&b'),
    ('Hey Ya!', 'Daniel Thompson', 'folk'),

    #or

    # ['Livin'' on a Prayer', 'Michael Davis', 'rap'],
    # ['Livin'' on a Prayer', 'Daniel Thompson', 'pop'],
    # ['Hey Ya!', 'Emma Taylor', 'latin'],
    # ['Sweet Child O'' Mine', 'John Smith', 'folk'],

    ]

    dbCursor.executemany("INSERT INTO songs(Title, Artist, Genre) VALUES(?,?,?)",songsData)
    
    # Commit the change
    dbCon.commit()

    print(songsData[0], "Added to songs table")

mutltipleInsert()