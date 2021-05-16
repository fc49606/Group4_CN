from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import os
import sqlalchemy
import psycopg2
import json
from decimal import Decimal

app = Flask(__name__)
api = Api(app)

db = None

def tcp_connection_engine():

    # pool = sqlalchemy.create_engine('postgresql+pg8000://postgres:root@127.0.0.1:5432/movies') 

    db_user = os.environ["DB_USER"]
    db_pass = os.environ["DB_PASS"]
    db_name = os.environ["DB_NAME"]
    db_host = os.environ["DB_HOST"]

    host_args = db_host.split(":")
    db_hostname, db_port = host_args[0], int(host_args[1])

    pool = sqlalchemy.create_engine(
            sqlalchemy.engine.url.URL(
                drivername="postgresql+pg8000",
                username=db_user,  # e.g. "my-database-user"
                password=db_pass,  # e.g. "my-database-password"
                host=db_hostname,  # e.g. "127.0.0.1"
                port=db_port,  # e.g. 5432
                database=db_name  # e.g. "my-database-name"
            )
    )
    
    return pool

def default(obj):
    if isinstance(obj, Decimal):
        return str(obj)
    raise TypeError("Object of type '%s' is not JSON serializable" % type(obj).__name__)

def read(title):
    #print("TESTE: ")
    db = tcp_connection_engine()
    with db.connect() as conn:
        titulo = "'"+title+"'"
        teste = conn.execute("""SELECT AVG(rating) FROM movies_ratings r INNER JOIN movies_metadata ON  r.movieid = movies_metadata.id where movies_metadata.title = """+titulo)
        print("Querie correu bem")
        conn.close()
        return jsonify(json.dumps({'result': [dict(row) for row in teste]}, default=default))

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world Rating'}
		
class Ratings(Resource):
    def get(self,title):
        return read(title)		

api.add_resource(HelloWorld, '/')
api.add_resource(Ratings,'/api/rating/<string:title>/')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)