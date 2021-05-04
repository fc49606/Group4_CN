from flask import Flask, request
from flask_restful import Resource, Api
import os
import sqlalchemy
import psycopg2

app = Flask(__name__)
api = Api(app)

db = None

def read(year,streamPlat):

    conn = psycopg2.connect(
        database = "movies_streaming_plataform",user = 'postgres', password='root', host='host.docker.internal',port = '5432'
    )
    cursor = conn.cursor()
    aux = ""
    #print("TESTE: "+streamPlat)
    if streamPlat == "netflix":	
        aux +=" and netflix=1"
    if streamPlat == "hulu":
        aux+=" and hulu=1"
    if streamPlat == "prime_video":
        aux+=" and prime_video=1"
    if streamPlat == "disneyplus":
        aux+=" and disneyplus=1"
    cursor.execute("""SELECT title from streaming_plataform where year="""+year+aux)
    resposta = cursor.fetchall()
    #print("Querie correu bem")
    conn.close()
    return resposta

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}
		
class Movie(Resource):
    def get(self,year,streamPlat):
        return read(year,streamPlat)		

api.add_resource(HelloWorld, '/')
api.add_resource(Movie,'/api/movie/<string:year>/<string:streamPlat>/')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)