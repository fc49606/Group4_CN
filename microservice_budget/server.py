from flask import Flask, request
from flask_restful import Resource, Api
import psycopg2

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class Budget(Resource):
    def get(self, title,year):
        conn = psycopg2.connect(
		database="movies", user='postgres', password='root', host='host.docker.internal', port= '5432'	
	    )
        conn.autocommit = True
        cursor = conn.cursor()
        titulo = "'"+title+"'"
        ano = "'"+year+"'"
        cursor.execute("""SELECT budget FROM movies_metadata where title="""+titulo+""" and year="""+ano)
        resposta = cursor.fetchall()
        aux = str(resposta.pop())
        ajuda = aux.split("'")
        print("Querie correu bem")
        conn.close()
        return (ajuda[1])

api.add_resource(HelloWorld, '/')
api.add_resource(Budget,'/api/budget/<string:title>/<string:year>/')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
