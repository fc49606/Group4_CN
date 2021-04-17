import psycopg2

conn = psycopg2.connect(
   database="postgres", user='postgres', password='root', host='127.0.0.1', port= '5432'
   #database="postgres", user='postgres', password='root', host='35.246.65.193', port= '5432'
)
conn.autocommit = True

cursor = conn.cursor()

movies = ''' CREATE database movies'''

cursor.execute(movies)

print("Database [movies] created successfully........")

conn.close()


conn = psycopg2.connect(
   database="movies", user='postgres', password='root', host='127.0.0.1', port= '5432'
   #database="movies", user='postgres', password='root', host='35.246.65.193', port= '5432'
)
conn.autocommit = True

cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS movies_metadata")
cursor.execute("""

CREATE TABLE movies_metadata
(
id DECIMAL NULL,
budget DECIMAL NULL,
original_language TEXT NULL,
year DECIMAL NULL,
revenue DECIMAL NULL,
runtime DECIMAL NULL,
title TEXT NULL
)
""")
print("Table [movies_metadata] created successfully........")

cursor.execute("DROP TABLE IF EXISTS movies_ratings")
cursor.execute("""

CREATE TABLE movies_ratings
(
movieId DECIMAL NULL,
rating DECIMAL NULL
)
""")
print("Table [movies_ratings] created successfully........")

conn.close()