import codecs

import psycopg2

DB_NAME = "movies"
DB_USER = "postgres"
DB_PASS = "root"
DB_HOST = "127.0.0.1"
DB_PORT = "5432"

conn = psycopg2.connect(
    database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT
)

print("[movies] database connected successfully! ..... ;)")

cur = conn.cursor()

types_of_encoding = ["utf8"] # "cp1252"
for encoding_type in types_of_encoding:
    with codecs.open('movies_metadata_corrigido_final.csv', encoding = encoding_type, errors ='replace') as csvfile:
        next(csvfile)
        cur.copy_from(csvfile, 'movies_metadata', sep=';')

print("movies_metadata populated successfully! ..... ;)")

conn.commit()

conn.close()

