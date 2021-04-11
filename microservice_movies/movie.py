
import psycopg2

def read(year,streamPlat):
	conn = psycopg2.connect(
		database="movies_streaming_plataform", user='postgres', password='root', host='127.0.0.1', port= '5432'	
	)
	conn.autocommit = True
	cursor = conn.cursor()
	aux=""
	print("TESTE: "+streamPlat)
	if streamPlat == "netflix":
		aux+=" and netflix=1"
	if streamPlat == "hulu":
		aux+=" and hulu=1"
	if streamPlat == "prime_video":
		aux+=" and prime_video=1"
	if streamPlat == "disneyplus":
		aux+=" and disneyplus=1"
	cursor.execute("""SELECT title from streaming_plataform where year="""+year+aux)
	resposta = cursor.fetchall()
	print("Querie correu bem")
	conn.close()
	return resposta
