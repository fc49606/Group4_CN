from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import os
import sqlalchemy
import psycopg2
from decimal import Decimal
import json

app = Flask(__name__)
api = Api(app)

db = None

def default(obj):
    if isinstance(obj, Decimal):
        return str(obj)
    raise TypeError("Object of type '%s' is not JSON serializable" % type(obj).__name__)

def read(title,year):
    conn = psycopg2.connect(
        database = "movies",user = 'postgres', password='root', host='host.docker.internal',port = '5432'
    )
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

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world Budget'}
		
class Budget(Resource):
    def get(self,title,year):
        return read(title,year)		

api.add_resource(HelloWorld, '/')
api.add_resource(Budget,'/api/budget/<string:title>/<string:year>/')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)