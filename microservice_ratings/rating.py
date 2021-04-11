
import psycopg2

def read(title):
	conn = psycopg2.connect(
		database="movies", user='postgres', password='root', host='127.0.0.1', port= '5432'	
	)
	conn.autocommit = True
	cursor = conn.cursor()
	titulo = "'"+title+"'"
	cursor.execute("""SELECT AVG(rating) FROM movies_ratings r INNER JOIN movies_metadata ON  r.movieid = movies_metadata.id where movies_metadata.title = """+titulo)
	resposta = cursor.fetchall()
	print("Querie correu bem")
	conn.close()
	return resposta
