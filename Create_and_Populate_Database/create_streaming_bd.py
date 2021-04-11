import psycopg2

conn = psycopg2.connect(
   database="postgres", user='postgres', password='root', host='127.0.0.1', port= '5432'
)
conn.autocommit = True

cursor = conn.cursor()

movies = ''' CREATE database movies_streaming_plataform'''

cursor.execute(movies)

print("Database [movies_streaming_plataform] created successfully........")

conn.close()


conn = psycopg2.connect(
   database="movies_streaming_plataform", user='postgres', password='root', host='127.0.0.1', port= '5432'
)
conn.autocommit = True

cursor = conn.cursor()

cursor.execute("DROP TABLE IF EXISTS streaming_plataform")
cursor.execute("""

CREATE TABLE streaming_plataform
(
ID DECIMAL NULL,
Title TEXT NULL,
Year DECIMAL NULL,
IMDb DECIMAL NULL,
Netflix DECIMAL NULL,
Hulu DECIMAL NULL,
Prime_Video DECIMAL NULL,
DisneyPlus DECIMAL NULL,
Directors TEXT NULL,
Genres TEXT NULL,
Country TEXT NULL,
Language TEXT NULL,
runtime DECIMAL NULL
)
""")
print("Table [streaming_plataform] created successfully........")

conn.close()