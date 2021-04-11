
import psycopg2

def read(title,year):
	conn = psycopg2.connect(
		database="movies", user='postgres', password='root', host='127.0.0.1', port= '5432'	
	)
	conn.autocommit = True
	cursor = conn.cursor()
	titulo = "'"+title+"'"
	ano = "'"+year+"'"
	cursor.execute("""SELECT revenue FROM movies_metadata where title="""+titulo+""" and year="""+ano)
	resposta = cursor.fetchall()
	print("Querie correu bem")
	conn.close()
	return resposta
