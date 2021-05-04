from flask import Flask, request
from flask_restful import Resource, Api
import os
import sqlalchemy
import psycopg2

app = Flask(__name__)
api = Api(app)

db = None

def read(title):
    conn = psycopg2.connect(
        database = "movies",user = 'postgres', password='root', host='host.docker.internal',port = '5432'
    )
    cursor = conn.cursor()
    titulo = "'"+title+"'"
    cursor.execute("""SELECT AVG(rating) FROM movies_ratings r INNER JOIN movies_metadata ON  r.movieid = movies_metadata.id where movies_metadata.title = """+titulo)
    resposta = cursor.fetchall()
    aux = str(resposta.pop())
    ajuda = aux.split("'")
    print("Querie correu bem")
    conn.close()
    return (ajuda[1])

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world Rating'}
		
class Ratings(Resource):
    def get(self,title):
        return read(title)		

api.add_resource(HelloWorld, '/')
api.add_resource(Ratings,'/api/rating/<string:title>/')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)