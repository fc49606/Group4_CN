from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import os
import sqlalchemy
import psycopg2

app = Flask(__name__)
api = Api(app)

db = None

def tcp_connection_engine():

    #pool = sqlalchemy.create_engine('postgresql+pg8000://postgres:root@127.0.0.1:5432/movies_streaming_plataform')

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

def read(year,streamPlat):
    #print("TESTE: ")
    db = tcp_connection_engine()
    with db.connect() as conn:
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
        teste = conn.execute("""SELECT title from streaming_plataform where year="""+year+aux)
        print("Querie correu bem")
        conn.close()
        return jsonify({'result': [dict(row) for row in teste]})

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world Movies'}
		
class Movie(Resource):
    def get(self,year,streamPlat):
        return read(year,streamPlat)		

api.add_resource(HelloWorld, '/')
api.add_resource(Movie,'/api/movie/<string:year>/<string:streamPlat>/')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
